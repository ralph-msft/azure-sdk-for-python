# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._serialization import Serializer

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_communication_identity_create_request(
    **kwargs: Any,
) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/identities"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_communication_identity_delete_request(id: str, **kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/identities/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_communication_identity_revoke_access_tokens_request(  # pylint: disable=name-too-long
    id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/identities/{id}/:revokeAccessTokens"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_communication_identity_exchange_teams_user_access_token_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/teamsUser/:exchangeAccessToken"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_communication_identity_issue_access_token_request(  # pylint: disable=name-too-long
    id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/identities/{id}/:issueAccessToken"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class CommunicationIdentityOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.communication.identity.CommunicationIdentityClient`'s
        :attr:`communication_identity` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def create(
        self,
        body: Optional[_models.CommunicationIdentityCreateRequest] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any,
    ) -> _models.CommunicationIdentityAccessTokenResult:
        """Create a new identity, and optionally, an access token.

        Create a new identity, and optionally, an access token.

        :param body: If specified, creates also a Communication Identity access token associated with
         the identity and containing the requested scopes. Default value is None.
        :type body: ~azure.communication.identity.models.CommunicationIdentityCreateRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CommunicationIdentityAccessTokenResult
        :rtype: ~azure.communication.identity.models.CommunicationIdentityAccessTokenResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self,
        body: Optional[IO] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any,
    ) -> _models.CommunicationIdentityAccessTokenResult:
        """Create a new identity, and optionally, an access token.

        Create a new identity, and optionally, an access token.

        :param body: If specified, creates also a Communication Identity access token associated with
         the identity and containing the requested scopes. Default value is None.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CommunicationIdentityAccessTokenResult
        :rtype: ~azure.communication.identity.models.CommunicationIdentityAccessTokenResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create(
        self,
        body: Optional[Union[_models.CommunicationIdentityCreateRequest, IO]] = None,
        **kwargs: Any,
    ) -> _models.CommunicationIdentityAccessTokenResult:
        """Create a new identity, and optionally, an access token.

        Create a new identity, and optionally, an access token.

        :param body: If specified, creates also a Communication Identity access token associated with
         the identity and containing the requested scopes. Is either a
         CommunicationIdentityCreateRequest type or a IO type. Default value is None.
        :type body: ~azure.communication.identity.models.CommunicationIdentityCreateRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: CommunicationIdentityAccessTokenResult
        :rtype: ~azure.communication.identity.models.CommunicationIdentityAccessTokenResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CommunicationIdentityAccessTokenResult] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            if body is not None:
                _json = self._serialize.body(body, "CommunicationIdentityCreateRequest")
            else:
                _json = None

        request = build_communication_identity_create_request(
            content_type=content_type,
            api_version=self._config.api_version,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("CommunicationIdentityAccessTokenResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace
    def delete(self, id: str, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Delete the identity, revoke all tokens for the identity and delete all associated data.

        Delete the identity, revoke all tokens for the identity and delete all associated data.

        :param id: Identifier of the identity to be deleted. Required.
        :type id: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_communication_identity_delete_request(
            id=id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def revoke_access_tokens(self, id: str, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Revoke all access tokens for the specific identity.

        Revoke all access tokens for the specific identity.

        :param id: Identifier of the identity. Required.
        :type id: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_communication_identity_revoke_access_tokens_request(
            id=id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    @overload
    def exchange_teams_user_access_token(
        self,
        body: _models.TeamsUserExchangeTokenRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any,
    ) -> _models.CommunicationIdentityAccessToken:
        """Exchange an Azure Active Directory (Azure AD) access token of a Teams user for a new
        Communication Identity access token with a matching expiration time.

        Exchange an Azure Active Directory (Azure AD) access token of a Teams user for a new
        Communication Identity access token with a matching expiration time.

        :param body: Request payload for the token exchange. Required.
        :type body: ~azure.communication.identity.models.TeamsUserExchangeTokenRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CommunicationIdentityAccessToken
        :rtype: ~azure.communication.identity.models.CommunicationIdentityAccessToken
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def exchange_teams_user_access_token(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CommunicationIdentityAccessToken:
        """Exchange an Azure Active Directory (Azure AD) access token of a Teams user for a new
        Communication Identity access token with a matching expiration time.

        Exchange an Azure Active Directory (Azure AD) access token of a Teams user for a new
        Communication Identity access token with a matching expiration time.

        :param body: Request payload for the token exchange. Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CommunicationIdentityAccessToken
        :rtype: ~azure.communication.identity.models.CommunicationIdentityAccessToken
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def exchange_teams_user_access_token(
        self, body: Union[_models.TeamsUserExchangeTokenRequest, IO], **kwargs: Any
    ) -> _models.CommunicationIdentityAccessToken:
        """Exchange an Azure Active Directory (Azure AD) access token of a Teams user for a new
        Communication Identity access token with a matching expiration time.

        Exchange an Azure Active Directory (Azure AD) access token of a Teams user for a new
        Communication Identity access token with a matching expiration time.

        :param body: Request payload for the token exchange. Is either a TeamsUserExchangeTokenRequest
         type or a IO type. Required.
        :type body: ~azure.communication.identity.models.TeamsUserExchangeTokenRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: CommunicationIdentityAccessToken
        :rtype: ~azure.communication.identity.models.CommunicationIdentityAccessToken
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CommunicationIdentityAccessToken] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _json = self._serialize.body(body, "TeamsUserExchangeTokenRequest")

        request = build_communication_identity_exchange_teams_user_access_token_request(
            content_type=content_type,
            api_version=self._config.api_version,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("CommunicationIdentityAccessToken", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @overload
    def issue_access_token(
        self,
        id: str,
        body: _models.CommunicationIdentityAccessTokenRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any,
    ) -> _models.CommunicationIdentityAccessToken:
        """Issue a new token for an identity.

        Issue a new token for an identity.

        :param id: Identifier of the identity to issue token for. Required.
        :type id: str
        :param body: Requested scopes for the new token. Required.
        :type body: ~azure.communication.identity.models.CommunicationIdentityAccessTokenRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CommunicationIdentityAccessToken
        :rtype: ~azure.communication.identity.models.CommunicationIdentityAccessToken
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def issue_access_token(
        self,
        id: str,
        body: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any,
    ) -> _models.CommunicationIdentityAccessToken:
        """Issue a new token for an identity.

        Issue a new token for an identity.

        :param id: Identifier of the identity to issue token for. Required.
        :type id: str
        :param body: Requested scopes for the new token. Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CommunicationIdentityAccessToken
        :rtype: ~azure.communication.identity.models.CommunicationIdentityAccessToken
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def issue_access_token(
        self,
        id: str,
        body: Union[_models.CommunicationIdentityAccessTokenRequest, IO],
        **kwargs: Any,
    ) -> _models.CommunicationIdentityAccessToken:
        """Issue a new token for an identity.

        Issue a new token for an identity.

        :param id: Identifier of the identity to issue token for. Required.
        :type id: str
        :param body: Requested scopes for the new token. Is either a
         CommunicationIdentityAccessTokenRequest type or a IO type. Required.
        :type body: ~azure.communication.identity.models.CommunicationIdentityAccessTokenRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: CommunicationIdentityAccessToken
        :rtype: ~azure.communication.identity.models.CommunicationIdentityAccessToken
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CommunicationIdentityAccessToken] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _json = self._serialize.body(body, "CommunicationIdentityAccessTokenRequest")

        request = build_communication_identity_issue_access_token_request(
            id=id,
            content_type=content_type,
            api_version=self._config.api_version,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("CommunicationIdentityAccessToken", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
