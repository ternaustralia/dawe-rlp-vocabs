from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class LUTSchema:
    """Config details used to generate categorical value collection."""

    endpoint_url: str
    label: str
    description: str
    collection_url: str
    uuid_namespace: str
