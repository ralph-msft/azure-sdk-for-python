# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models import (  # type: ignore
    AtlasAttributeDef,
    AtlasBusinessMetadataDef,
    AtlasClassification,
    AtlasClassificationDef,
    AtlasClassifications,
    AtlasConstraintDef,
    AtlasEntitiesWithExtInfo,
    AtlasEntity,
    AtlasEntityDef,
    AtlasEntityHeader,
    AtlasEntityHeaders,
    AtlasEntityWithExtInfo,
    AtlasEnumDef,
    AtlasEnumElementDef,
    AtlasErrorResponse,
    AtlasGlossary,
    AtlasGlossaryCategory,
    AtlasGlossaryExtInfo,
    AtlasGlossaryHeader,
    AtlasGlossaryTerm,
    AtlasLineageInfo,
    AtlasObjectId,
    AtlasRelatedCategoryHeader,
    AtlasRelatedObjectId,
    AtlasRelatedTermHeader,
    AtlasRelationship,
    AtlasRelationshipAttributeDef,
    AtlasRelationshipDef,
    AtlasRelationshipEndDef,
    AtlasRelationshipWithExtInfo,
    AtlasStruct,
    AtlasStructDef,
    AtlasTermAssignmentHeader,
    AtlasTermCategorizationHeader,
    AtlasTypeDef,
    AtlasTypeDefHeader,
    AtlasTypesDef,
    AutoCompleteOptions,
    AutoCompleteResult,
    AutoCompleteResultValue,
    BulkImportResult,
    BusinessMetadataOptions,
    ClassificationAssociateOptions,
    ContactInfo,
    ContactSearchResultValue,
    DateFormat,
    EntityMutationResult,
    ImportInfo,
    LineageRelation,
    MoveEntitiesOptions,
    NumberFormat,
    ParentRelation,
    PurviewObjectId,
    QueryOptions,
    QueryResult,
    ResourceLink,
    SearchFacetItem,
    SearchFacetItemValue,
    SearchFacetResultValue,
    SearchFacetSort,
    SearchHighlights,
    SearchResultValue,
    SearchTaxonomySetting,
    SuggestOptions,
    SuggestResult,
    SuggestResultValue,
    TermSearchResultValue,
    TermTemplateDef,
    TimeBoundary,
    TimeZone,
)

from ._enums import (  # type: ignore
    AtlasTermAssignmentStatus,
    AtlasTermRelationshipStatus,
    BusinessAttributeUpdateBehavior,
    CardinalityValue,
    EntityStatus,
    ImportStatus,
    LineageDirection,
    RelationshipCategory,
    RoundingMode,
    SearchSortOrder,
    SortType,
    StatusAtlasRelationship,
    TermStatus,
    TypeCategory,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AtlasAttributeDef",
    "AtlasBusinessMetadataDef",
    "AtlasClassification",
    "AtlasClassificationDef",
    "AtlasClassifications",
    "AtlasConstraintDef",
    "AtlasEntitiesWithExtInfo",
    "AtlasEntity",
    "AtlasEntityDef",
    "AtlasEntityHeader",
    "AtlasEntityHeaders",
    "AtlasEntityWithExtInfo",
    "AtlasEnumDef",
    "AtlasEnumElementDef",
    "AtlasErrorResponse",
    "AtlasGlossary",
    "AtlasGlossaryCategory",
    "AtlasGlossaryExtInfo",
    "AtlasGlossaryHeader",
    "AtlasGlossaryTerm",
    "AtlasLineageInfo",
    "AtlasObjectId",
    "AtlasRelatedCategoryHeader",
    "AtlasRelatedObjectId",
    "AtlasRelatedTermHeader",
    "AtlasRelationship",
    "AtlasRelationshipAttributeDef",
    "AtlasRelationshipDef",
    "AtlasRelationshipEndDef",
    "AtlasRelationshipWithExtInfo",
    "AtlasStruct",
    "AtlasStructDef",
    "AtlasTermAssignmentHeader",
    "AtlasTermCategorizationHeader",
    "AtlasTypeDef",
    "AtlasTypeDefHeader",
    "AtlasTypesDef",
    "AutoCompleteOptions",
    "AutoCompleteResult",
    "AutoCompleteResultValue",
    "BulkImportResult",
    "BusinessMetadataOptions",
    "ClassificationAssociateOptions",
    "ContactInfo",
    "ContactSearchResultValue",
    "DateFormat",
    "EntityMutationResult",
    "ImportInfo",
    "LineageRelation",
    "MoveEntitiesOptions",
    "NumberFormat",
    "ParentRelation",
    "PurviewObjectId",
    "QueryOptions",
    "QueryResult",
    "ResourceLink",
    "SearchFacetItem",
    "SearchFacetItemValue",
    "SearchFacetResultValue",
    "SearchFacetSort",
    "SearchHighlights",
    "SearchResultValue",
    "SearchTaxonomySetting",
    "SuggestOptions",
    "SuggestResult",
    "SuggestResultValue",
    "TermSearchResultValue",
    "TermTemplateDef",
    "TimeBoundary",
    "TimeZone",
    "AtlasTermAssignmentStatus",
    "AtlasTermRelationshipStatus",
    "BusinessAttributeUpdateBehavior",
    "CardinalityValue",
    "EntityStatus",
    "ImportStatus",
    "LineageDirection",
    "RelationshipCategory",
    "RoundingMode",
    "SearchSortOrder",
    "SortType",
    "StatusAtlasRelationship",
    "TermStatus",
    "TypeCategory",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
