from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class LUTSchema:
    """Config details used to generate categorical value collection."""

    endpoint_url: str
    label: str
    description: str
    collection_uuid: str
    uuid_namespace: str


@dataclass(eq=True, frozen=True)
class ExcelVocab:
    """Excel vocab schema."""

    path: str
    id: str


@dataclass
class InfoNeeded:
    """The information needed when creating vocabularies for properties and attributes."""

    name: str
    attribute_collection_uri: str
    property_collection_uri: str
    method_uri: str
    attribute_file_name: str
    property_file_name: str
