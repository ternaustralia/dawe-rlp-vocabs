from pathlib import Path

import pytest
from rdflib import Graph, URIRef
from rdflib.namespace import SKOS

from dawe_nrm import api


@pytest.fixture
def path():
    return Path("tests/categorical_values_outputs")


@pytest.fixture
def output_path(path: Path):
    path.mkdir(exist_ok=True, parents=True)
    api.categorical_values.write_all(path, show_progress=False)
    yield path

    # Clean up.
    files = [file for file in path.glob("**/*")]
    for file in files:
        file.unlink()
    path.rmdir()


@pytest.mark.slow
def test(output_path: Path, path: Path):
    files = list(output_path.glob("**/*.ttl"))

    collection_members_file = path / Path("collection-members.ttl")

    assert collection_members_file in files

    collection_uri = URIRef(
        "https://linked.data.gov.au/def/test/dawe-cv/05f83f99-1998-4d11-8837-bb4a68788521"
    )

    graph = Graph()
    for file in files:
        graph.parse(file)

    categorical_collections = list(graph.objects(collection_uri, SKOS.member))

    assert len(categorical_collections) == len(files) - 1
    assert len(categorical_collections) == len(api.categorical_values.endpoints)
