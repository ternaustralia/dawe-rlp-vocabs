from rdflib import Graph


def add_observable_property_relationships(graph: Graph, new_data_graph: Graph):
    result = graph.query(
        """
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX urnc: <urn:class:>
        PREFIX urnp: <urn:property:>
        PREFIX tern: <https://w3id.org/tern/ontologies/tern/>

        CONSTRUCT {
            ?observable_property tern:hasFeatureType ?featureType ;
                        tern:hasMethod ?method ;
                        tern:valueType ?valueType ;
                        tern:hasCategoricalValuesCollection ?categoricalValuesCollection .
        }
        WHERE {
            ?_concept_metadata a urnc:ObservablePropertyMeta ;
                            urnp:observableProperty ?observable_property ;
                            urnp:featureType ?featureType ;
                            urnp:protocolModule ?method ;
                            urnp:valueType ?valueType .
            OPTIONAL {
                ?concept_metadata urnp:categoricalValuesCollection ?categoricalValuesCollection .
            }
        }
        ORDER BY ?label
    """
    )
    for triple in result:
        new_data_graph.add(triple)


def expand_graph(graph: Graph, new_data_graph: Graph):
    add_observable_property_relationships(graph, new_data_graph)
    # ... other graph expansion functions
