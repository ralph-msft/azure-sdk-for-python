# cSpell:ignore PULLREQUEST
# cSpell:ignore TARGETBRANCH
[CmdletBinding()]
Param (
  [Parameter(Mandatory=$True)]
  [string] $ArtifactPath,
  [Parameter(Mandatory=$True)]
  [string] $PullRequestNumber,
  [Parameter(Mandatory=$True)]
  [string] $BuildId,
  [Parameter(Mandatory=$True)]
  [string] $CommitSha,
  [string] $APIViewUri,
  [string] $RepoFullName = "",
  [string] $ArtifactName = "packages",
  [string] $TargetBranch = ("origin/${env:SYSTEM_PULLREQUEST_TARGETBRANCH}" -replace "refs/heads/"),
  [string] $DevopsProject = "internal"
)

. (Join-Path $PSScriptRoot common.ps1)

$configFileDir = Join-Path -Path $ArtifactPath "PackageInfo"

# Submit API review request and return status whether current revision is approved or pending or failed to create review
function Submit-Request($filePath, $packageName)
{
    $repoName = $RepoFullName
    if (!$repoName) {
        $repoName = "azure/azure-sdk-for-$LanguageShort"
    }
    $reviewFileName = "$($packageName)_$($LanguageShort).json"
    $query = [System.Web.HttpUtility]::ParseQueryString('')
    $query.Add('artifactName', $ArtifactName)
    $query.Add('buildId', $BuildId)
    $query.Add('filePath', $filePath)
    $query.Add('commitSha', $CommitSha)
    $query.Add('repoName', $repoName)
    $query.Add('pullRequestNumber', $PullRequestNumber)
    $query.Add('packageName', $packageName)
    $query.Add('language', $LanguageShort)
    $query.Add('project', $DevopsProject)
    $reviewFileFullName = Join-Path -Path $ArtifactPath $packageName $reviewFileName
    if (Test-Path $reviewFileFullName)
    {
        $query.Add('codeFile', $reviewFileName)
    }
    $uri = [System.UriBuilder]$APIViewUri
    $uri.query = $query.toString()
    Write-Host "Request URI: $($uri.Uri.OriginalString)"
    try
    {
        $Response = Invoke-WebRequest -Method 'GET' -Uri $uri.Uri -MaximumRetryCount 3
        $StatusCode = $Response.StatusCode
    }
    catch
    {
        Write-Host "Error $StatusCode - Exception details: $($_.Exception.Response)"
        $StatusCode = $_.Exception.Response.StatusCode
    }

    return $StatusCode
}

function Should-Process-Package($pkgPath, $packageName)
{
    $pkg = Split-Path -Leaf $pkgPath
    $pkgPropPath = Join-Path -Path $configFileDir "$packageName.json"
    if (!(Test-Path $pkgPropPath))
    {
        Write-Host " Package property file path $($pkgPropPath) is invalid."
        return $False
    }
    # Get package info from json file created before updating version to daily dev
    $pkgInfo = Get-Content $pkgPropPath | ConvertFrom-Json
    $packagePath = $pkgInfo.DirectoryPath
    $modifiedFiles  = @(Get-ChangedFiles -DiffPath "$packagePath/*" -DiffFilterType '')
    $filteredFileCount = $modifiedFiles.Count
    Write-Host "Number of modified files for package: $filteredFileCount"
    return ($filteredFileCount -gt 0 -and $pkgInfo.IsNewSdk)
}

function Log-Input-Params()
{
    Write-Host "Artifact Path: $($ArtifactPath)"
    Write-Host "Artifact Name: $($ArtifactName)"
    Write-Host "PullRequest Number: $($PullRequestNumber)"
    Write-Host "BuildId: $($BuildId)"
    Write-Host "Language: $($Language)"
    Write-Host "Commit SHA: $($CommitSha)"
    Write-Host "Repo Name: $($RepoFullName)"
    Write-Host "Project: $($DevopsProject)"
}

Log-Input-Params

if (!($FindArtifactForApiReviewFn -and (Test-Path "Function:$FindArtifactForApiReviewFn")))
{
    Write-Host "The function for 'FindArtifactForApiReviewFn' was not found.`
    Make sure it is present in eng/scripts/Language-Settings.ps1 and referenced in eng/common/scripts/common.ps1.`
    See https://github.com/Azure/azure-sdk-tools/blob/main/doc/common/common_engsys.md#code-structure"
    exit 1
}

$responses = @{}

$packageProperties = Get-ChildItem -Recurse -Force "$configFileDir" `
  | Where-Object { 
      $_.Extension -eq '.json' -and ($_.FullName.Substring($configFileDir.Length + 1) -notmatch '^_.*?[\\\/]')
    }

foreach ($packagePropFile in $packageProperties)
{
    $packageMetadata = Get-Content $packagePropFile | ConvertFrom-Json
    $pkgArtifactName = $packageMetadata.ArtifactName ?? $packageMetadata.Name

    Write-Host "Processing $($pkgArtifactName)"

    $packages = &$FindArtifactForApiReviewFn $ArtifactPath $pkgArtifactName

    if ($packages)
    {
        $pkgPath = $packages.Values[0]
        $isRequired = Should-Process-Package -pkgPath $pkgPath -packageName $pkgArtifactName
        Write-Host "Is API change detect required for $($pkgArtifactName):$($isRequired)"
        if ($isRequired -eq $True)
        {
            $filePath = $pkgPath.Replace($ArtifactPath , "").Replace("\", "/")
            $respCode = Submit-Request -filePath $filePath -packageName $pkgArtifactName
            if ($respCode -ne '200')
            {
                $responses[$pkgArtifactName] = $respCode
            }
        }
        else
        {
            Write-Host "Pull request does not have any change for $($pkgArtifactName)). Skipping API change detect."
        }
    }
    else
    {
        Write-Host "No package is found in artifact path to find API changes for $($pkgArtifactName)"
    }
}

foreach($pkg in $responses.keys)
{
    Write-Host "API detection request status for $($pkg) : $($responses[$pkg])"
}
