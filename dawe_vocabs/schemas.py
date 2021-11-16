from dataclasses import dataclass


@dataclass
class LUTSchema:
    """Config details used to generate categorical value collection."""

    endpoint_url: str
    label: str
    description: str
    collection_uuid: str
    uuid_namespace: str


@dataclass
class ExcelVocab:
    """Excel vocab schema."""

    path: str
    id: str
