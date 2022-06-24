from rdflib import DCTERMS, RDF, SKOS, Graph, Literal, Namespace, URIRef

from dawe_vocabs.namespaces import TERN


def create(base_uri: Namespace, g: Graph) -> None:
    # Create feature types collection.
    # Members of this collection are based on the values of tern:hasFeatureType predicate.
    feature_types_uri = base_uri["31a9f83d-9c8b-4d68-8dd7-d1b7a9a4197b"]
    g.add((feature_types_uri, RDF.type, SKOS.Collection))
    g.add((feature_types_uri, SKOS.prefLabel, Literal("Feature types")))
    g.add(
        (
            feature_types_uri,
            DCTERMS.description,
            Literal("A Profile of TERN's Feature Types vocabulary."),
        )
    )
    g.add(
        (
            feature_types_uri,
            DCTERMS.source,
            URIRef(
                "http://linked.data.gov.au/def/tern-cv/68af3d25-c801-4089-afff-cf701e2bd61d"
            ),
        )
    )
    features = g.objects(None, TERN.hasFeatureType)
    for feature in features:
        g.add((feature_types_uri, SKOS.member, feature))
