from pathlib import Path

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDFS, SDO

from src.settings import VOCAB_FILES_DIR_GITHUB

REG = Namespace("http://purl.org/linked-data/registry/")
NRM = Namespace("https://linked.data.gov.au/def/test/dawe-cv/")


def create_graph():
    graph = Graph()
    graph.bind("tern", "https://w3id.org/tern/ontologies/tern/")
    return graph


def add_is_defined_by(graph: Graph):
    query = """
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT DISTINCT ?uri
        WHERE {
            {
                ?uri a skos:Concept .
            }
            UNION {
                ?uri a skos:Collection .
            }
        }
    """

    rows = graph.query(query)

    for row in rows:
        graph.add(
            (row["uri"], RDFS.isDefinedBy, URIRef("https://linked.data.gov.au/def/nrm"))
        )

    return graph


def serialize(path: Path, graph: Graph):
    graph.remove(
        (
            None,
            REG.register,
            URIRef(
                "https://linked.data.gov.au/def/test/dawe-cv/616c7c18-3309-472d-a38d-8106a1b6ff9b"
            ),
        )
    )

    add_is_defined_by(graph)

    subjects = graph.subjects()
    for subject in subjects:
        graph.add((subject, SDO.url, Literal(VOCAB_FILES_DIR_GITHUB + str(path))))

    graph.serialize(path, format="longturtle")
