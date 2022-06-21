"""create_local_files.py

This script generates a local copy of the DAWE NRM vocabularies in the remote
GraphDB repository. It writes each collection and concepts into directories
and files.

This script is intended to be run only once in June 2022 to generate the local copy
of the RDF files in this repository. Further changes to the data should be
done directly in the generated source files.
"""


import re
from pathlib import Path

import requests
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, SDO, SKOS

from dawe_vocabs import settings
from dawe_vocabs.vocabs import categorical_values_collection
from src.graph import create_graph

SPARQL_ENDPOINT = "https://graphdb.tern.org.au/repositories/dawe_vocabs_core"
REG = Namespace("http://purl.org/linked-data/registry/")
NRM = Namespace("https://linked.data.gov.au/def/test/dawe-cv/")
vocab_files_dir = Path("vocab_files")
DASHES = re.compile(r"-+")
VOCAB_FILES_DIR_GITHUB = "https://github.com/ternaustralia/dawe-rlp-vocabs/tree/master/"


def fetch_remote_cbd(uri: str, graph: Graph):
    query = f"""
        CONSTRUCT {{
            ?s ?p ?o .
        }}
        WHERE {{
            BIND(<{uri}> as ?s)
            ?s ?p ?o .
        }}
    """

    response = requests.post(
        SPARQL_ENDPOINT,
        data=query,
        headers={"content-type": "application/sparql-query", "accept": "text/turtle"},
    )

    graph.parse(data=response.text, format="turtle")
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


def create_feature_types():
    feature_types_dir = vocab_files_dir / "feature_types"
    feature_types_dir.mkdir(exist_ok=True)

    query = "DESCRIBE <https://linked.data.gov.au/def/test/dawe-cv/31a9f83d-9c8b-4d68-8dd7-d1b7a9a4197b>"

    response = requests.post(
        SPARQL_ENDPOINT,
        data=query,
        headers={"content-type": "application/sparql-query", "accept": "text/turtle"},
    )
    response.raise_for_status()

    graph = create_graph()
    graph.parse(data=response.text, format="turtle")
    serialize(feature_types_dir / "collection.ttl", graph)


def clean_label(label: str):
    label = (
        label.replace(" Observable Properties", "")
        .replace(" Properties", "")
        .lower()
        .replace(" ", "-")
        .replace("/", "-")
    )
    label = DASHES.sub("-", label)
    return label


def create_instance(uri: str, path: Path, graph: Graph, filter_by: str):
    types_ = set(graph.objects(URIRef(uri), RDF.type))
    if SKOS.Collection in types_:
        serialize(path / "collection.ttl", graph.cbd(URIRef(uri)))
    elif SKOS.Concept in types_:
        label = graph.value(uri, SKOS.prefLabel)
        label = clean_label(label) + ".ttl"
        serialize(path / label, graph.cbd(URIRef(uri)))
    else:
        raise ValueError(f"Don't know how to handle types in {types_}.")

    create_collection(uri, path, graph, filter_by)


def create_collection(uri: str, parent_dir: Path, graph: Graph, filter_by: str):
    query = f"""
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT DISTINCT ?uri ?label ?type
        WHERE {{
            <{uri}> skos:member ?uri .
            ?uri a ?type ;
                    skos:prefLabel ?label .
            
            FILTER(?type IN ({filter_by}))
        }}
        ORDER by ?label
    """

    results = graph.query(query)

    for row in results:
        label = graph.value(row["uri"], SKOS.prefLabel)
        label = clean_label(label)

        path = parent_dir / label
        path.mkdir(exist_ok=True)
        create_instance(row["uri"], path, graph, filter_by)


def create_collections_by_module(
    parent_collection_uri: str, parent_dir: Path, graph: Graph, filter_by: str
):
    parent_dir.mkdir(exist_ok=True)

    query = f"""
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        CONSTRUCT {{
            ?uri ?p ?o .
        }}
        WHERE {{
            SELECT ?uri ?p ?o
            {{
                {{
                    BIND(<{parent_collection_uri}> as ?uri)
                    ?uri ?p ?o .
                }}
                UNION {{
                    <{parent_collection_uri}> skos:member+ ?uri .
                    ?uri ?p ?o .
                    ?uri a ?type .
                    FILTER(?type in ({filter_by}))
                }}
            }}
        }}
    """

    response = requests.post(
        SPARQL_ENDPOINT,
        data=query,
        headers={"content-type": "application/sparql-query", "accept": "text/turtle"},
    )
    response.raise_for_status()

    graph.parse(data=response.text, format="turtle")

    cbd = graph.cbd(URIRef(parent_collection_uri))

    serialize(
        parent_dir / "collection.ttl",
        cbd,
    )

    create_collection(parent_collection_uri, parent_dir, graph, filter_by)


def create_concepts(uri: str, path: Path, graph: Graph):
    path.mkdir(exist_ok=True)

    query = f"""
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        CONSTRUCT {{
            ?uri ?p ?o .   
        }}
        WHERE {{
            BIND(?concept AS ?uri)
            ?uri ?p ?o .
            {{
                SELECT ?concept
                WHERE
                {{
                    <{uri}> skos:member+ ?concept .
                    ?concept a ?type
                    FILTER(?type = skos:Concept)
                }}
            }}
        }}
    """

    query = f"""
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        CONSTRUCT {{
            ?uri ?p ?o .
        }}
        WHERE {{
            BIND(?member as ?uri)
            ?uri ?p ?o .
            ?uri a ?type .
            FILTER(?type = skos:Concept)
            {{
                SELECT ?member
                WHERE {{
                    <{uri}> skos:member+ ?member .        
                }}  
            }}
        }}
    """

    response = requests.post(
        SPARQL_ENDPOINT,
        data=query,
        headers={"content-type": "application/sparql-query", "accept": "text/turtle"},
    )
    response.raise_for_status()

    graph.parse(data=response.text, format="turtle")

    query = """
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT DISTINCT ?uri
        WHERE {
            ?uri a skos:Concept .
        }
    """

    results = graph.query(query)

    for row in results:
        uri = row["uri"]
        label = graph.value(uri, SKOS.prefLabel)
        orig_label = label
        label = label.strip()
        graph.remove((uri, SKOS.prefLabel, orig_label))
        graph.add((uri, SKOS.prefLabel, Literal(label)))
        label = clean_label(label)
        serialize(path / f"{label}.ttl", graph.cbd(uri))


def create_index():
    index_data = """
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX sdo: <https://schema.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

<https://linked.data.gov.au/def/nrm>
    a
        owl:Ontology ,
        skos:ConceptScheme ;
    dcterms:provenance "The controlled vocabularies are the digital RDF representation of concepts extracted from the DAWE NRM field collection protocols." ;
    skos:definition "The DAWE NRM controlled vocabularies support the data representation of field survey data collected using the NRM collection protocols." ;
    skos:prefLabel "DAWE NRM Controlled Vocabularies" ;
    sdo:codeRepository "https://github.com/ternaustralia/dawe-rlp-vocabs"^^xsd:anyURI ;
    sdo:contributor <https://w3id.org/tern/resources/3da2112b-74c0-4d9c-bc39-d8dad6e80808> ;
    sdo:creator
        <https://orcid.org/0000-0002-6047-9864> ,
        <https://orcid.org/0000-0002-8481-9069> ,
        <https://orcid.org/0000-0002-9143-5514> ,
        <https://w3id.org/tern/resources/cbd72114-5fa0-410a-b6c1-73a3fd8f111e> ;
    sdo:dateCreated "2022-05-19"^^xsd:date ;
    sdo:dateIssued "2022-05-19"^^xsd:date ;
    sdo:dateModified "2022-05-19"^^xsd:date ;
    sdo:license "https://creativecommons.org/licenses/by/4.0/"^^xsd:anyURI ;
    sdo:publisher <https://ror.org/030c92375> ;
.

<https://orcid.org/0000-0002-6047-9864>
    a sdo:Person ;
    sdo:email "e.chuc@uq.edu.au"^^xsd:anyURI ;
    sdo:name "Edmond Chuc" ;
.

<https://orcid.org/0000-0002-8481-9069>
    a sdo:Person ;
    sdo:email "t.parkhurst@uq.edu.au"^^xsd:anyURI ;
    sdo:name "Tina Parkhurst" ;
.

<https://orcid.org/0000-0002-9143-5514>
    a sdo:Person ;
    sdo:email "a.singhramesh@uq.edu.au"^^xsd:anyURI ;
    sdo:name "Arun Singh Ramesh" ;
.

<https://ror.org/030c92375>
    a sdo:Organization ;
    sdo:name "Department of Agriculture, Water and the Environment" ;
    sdo:url "https://www.awe.gov.au/"^^xsd:anyURI ;
.

<https://w3id.org/tern/resources/3da2112b-74c0-4d9c-bc39-d8dad6e80808>
    a sdo:Person ;
    sdo:email "andrew.tokmakoff@adelaide.edu.au"^^xsd:anyURI ;
    sdo:name "Andrew Tokmakoff" ;
.

<https://w3id.org/tern/resources/cbd72114-5fa0-410a-b6c1-73a3fd8f111e>
    a sdo:Person ;
    sdo:email "junrong.yu@uq.edu.au"^^xsd:anyURI ;
    sdo:name "Junrong Yu" ;
.
    """

    graph = create_graph()
    graph.parse(data=index_data, format="turtle")
    serialize(vocab_files_dir / "index.ttl", graph)


def create_custom_vocabs():
    data = """
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
    @prefix dcterms: <http://purl.org/dc/terms/> .
    @prefix tern: <https://w3id.org/tern/ontologies/tern/> .

    <https://linked.data.gov.au/def/test/dawe-cv/0ba17555-8c8f-435a-b16f-62773561207b>
        a skos:Collection ;
        skos:prefLabel "Basal sweep hit type codes" ;
        dcterms:description "These codes were created for the full and lite versions of the Basal Area module's DBH protocols. The categorical values model the collection app's JSON schema." ;
        skos:member <https://linked.data.gov.au/def/test/dawe-cv/57b9fb25-e075-4e18-8c7f-167e09318c94>,
            <https://linked.data.gov.au/def/test/dawe-cv/3e0a5d97-c623-477e-98fe-8fe120907530> ;
    .

    <https://linked.data.gov.au/def/test/dawe-cv/57b9fb25-e075-4e18-8c7f-167e09318c94>
        a skos:Concept ;
        skos:prefLabel "in" ;
        skos:definition "Trees where the trunk or stem at breast height (1.3 m above ground level) is wider than the aperture of the BAF used on a TERN Basal Wedge. " ;
    .

    <https://linked.data.gov.au/def/test/dawe-cv/3e0a5d97-c623-477e-98fe-8fe120907530>
        a skos:Concept ;
        skos:prefLabel "borderline" ;
        skos:definition "Trees where the trunk or stem at breast height (1.3 m above ground level) is the exact width of the aperture of the BAF used on a TERN Basal Wedge. " ;
    .

    <https://linked.data.gov.au/def/test/dawe-cv/05f83f99-1998-4d11-8837-bb4a68788521> skos:member <https://linked.data.gov.au/def/test/dawe-cv/0ba17555-8c8f-435a-b16f-62773561207b> .

    <https://linked.data.gov.au/def/test/dawe-cv/43178892-92a6-434f-9895-340700e299e6>
        a skos:Concept ;
        skos:prefLabel "basal area sweep hit type" ;
        skos:definition "The type of hit of a plant during a basal area sweep." ;
        dcterms:source "Ecological Field Monitoring protocols - Basal area module, draft v0.1, 30/11/2021" ;
        tern:hasFeatureType <http://linked.data.gov.au/def/tern-cv/ae71c3f6-d430-400f-a1d4-97a333b4ee02> ;
        tern:hasMethod <https://linked.data.gov.au/def/test/dawe-cv/a7d605e0-7d90-473e-aac0-21cdf380576f> ;
        tern:valueType tern:IRI ;
        tern:hasCategoricalCollection <https://linked.data.gov.au/def/test/dawe-cv/0ba17555-8c8f-435a-b16f-62773561207b> ;
    .

    <https://linked.data.gov.au/def/test/dawe-cv/ab7c4569-312c-4450-b413-9b11c4d2577b> skos:member <https://linked.data.gov.au/def/test/dawe-cv/43178892-92a6-434f-9895-340700e299e6> .
    """

    graph = create_graph()
    graph.parse(data=data, format="turtle")
    path = vocab_files_dir / "custom_vocabs"
    path.mkdir(exist_ok=True)
    serialize(path / "basal-sweep-hit-types.ttl", graph)


def create_categorical_collection():
    path = vocab_files_dir / "categorical_collections/luts"
    path.mkdir(exist_ok=True)

    top_level_collection_graph = create_graph()
    top_level_collection_uri = URIRef(
        "https://linked.data.gov.au/def/test/dawe-cv/05f83f99-1998-4d11-8837-bb4a68788521"
    )
    top_level_data = """
        @prefix dcterms: <http://purl.org/dc/terms/> .
        @prefix ns1: <http://purl.org/linked-data/registry/> .
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix schema: <https://schema.org/> .
        @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
        <https://linked.data.gov.au/def/test/dawe-cv/05f83f99-1998-4d11-8837-bb4a68788521> a skos:Collection ;
            dcterms:description "A collection of collections of categorical values." ;
            skos:prefLabel "Collections of categorical values" .
    """
    top_level_collection_graph.parse(data=top_level_data, format="turtle")
    top_level_collection_member_graph = create_graph()

    for lut_config in settings.lut_configs:
        try:
            graph = create_graph()

            categorical_values_collection.create(
                settings.base_uri, graph, lut_config, settings.parent_collection_uri
            )

            label = lut_config.uuid_namespace.replace(" ", "-") + ".ttl"
            if label == "collection.ttl":
                raise ValueError(
                    "Categorical values collection cannot be named collection.ttl as it is already reserved for the top-level collection."
                )
            serialize(path / label, graph)

            top_level_collection_member_graph.add(
                (top_level_collection_uri, SKOS.member, NRM[lut_config.collection_uuid])
            )
        except categorical_values_collection.NoDataInAPIException as err:
            raise Exception(err) from err

    serialize(path / "collection.ttl", top_level_collection_graph)
    serialize(path / "collection_members.ttl", top_level_collection_member_graph)


if __name__ == "__main__":
    vocab_files_dir.mkdir(exist_ok=True)

    create_feature_types()

    graph = create_graph()
    create_collections_by_module(
        "https://linked.data.gov.au/def/test/dawe-cv/e8e10807-baea-4c9b-8d1c-d77ced9df1e9",
        vocab_files_dir / "observable_properties_by_module",
        graph,
        "skos:Collection",
    )

    graph = create_graph()
    create_collections_by_module(
        "https://linked.data.gov.au/def/test/dawe-cv/dba9fde2-34ba-4a1d-92e0-63846105fc87",
        vocab_files_dir / "attributes_by_module",
        graph,
        "skos:Collection",
    )

    graph = create_graph()
    create_collections_by_module(
        "https://linked.data.gov.au/def/test/dawe-cv/f46fcbc6-0660-4e12-bcd4-c5642459b630",
        vocab_files_dir / "methods_by_module",
        graph,
        "skos:Collection, skos:Concept",
    )

    graph = create_graph()
    to_be_added = [
        "https://linked.data.gov.au/def/test/dawe-cv/fadc6db3-9474-45f5-a052-5b5002580c0a"
    ]
    for item in to_be_added:
        fetch_remote_cbd(item, graph)
    create_concepts(
        "https://linked.data.gov.au/def/test/dawe-cv/e8e10807-baea-4c9b-8d1c-d77ced9df1e9",
        vocab_files_dir / "observable_property_concepts",
        graph,
    )

    graph = create_graph()
    create_concepts(
        "https://linked.data.gov.au/def/test/dawe-cv/dba9fde2-34ba-4a1d-92e0-63846105fc87",
        vocab_files_dir / "attribute_concepts",
        graph,
    )

    create_index()
    create_custom_vocabs()
    create_categorical_collection()
