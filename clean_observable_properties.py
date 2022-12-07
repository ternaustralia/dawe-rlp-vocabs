from pathlib import Path

from rdflib import Graph, Namespace
from ontotools.functions.normalize_file import normalize_file


if __name__ == "__main__":
    path = "vocab_files/observable_property_concepts"
    vocab_files_dir = Path(path)
    files = list(vocab_files_dir.glob("**/*.ttl"))

    TERN = Namespace("https://w3id.org/tern/ontologies/tern/")

    for file in files:
        graph = Graph()
        graph.parse(file, format="turtle")
        graph.remove((None, TERN.hasFeatureType, None))
        graph.remove((None, TERN.hasMethod, None))
        graph.remove((None, TERN.valueType, None))
        graph.remove((None, TERN.hasCategoricalValuesCollection, None))
        graph.serialize(file, format="turtle")

        normalize_file(file, False, False, file)
