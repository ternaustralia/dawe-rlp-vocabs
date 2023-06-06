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
                        tern:valueType ?valueType .
        }
        WHERE {
            ?_concept_metadata a urnc:ObservablePropertyMeta ;
                            urnp:observableProperty ?observable_property ;
                            urnp:featureType ?featureType ;
                            urnp:protocolModule ?method ;
                            urnp:valueType ?valueType .
        }
        ORDER BY ?label
    """
    )
    for triple in result:
        new_data_graph.add(triple)


def add_observable_property_categorical_values_collections(
    graph: Graph, new_data_graph: Graph
):
    result = graph.query(
        """
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX urnc: <urn:class:>
        PREFIX urnp: <urn:property:>
        PREFIX tern: <https://w3id.org/tern/ontologies/tern/>

        CONSTRUCT {
            ?observable_property tern:hasCategoricalValuesCollection ?categoricalValuesCollection .
        }
        WHERE {
            ?_concept_metadata a urnc:ObservablePropertyMeta ;
                            urnp:observableProperty ?observable_property ;
                            urnp:categoricalValuesCollection ?categoricalValuesCollection .
        }
        ORDER BY ?label
    """
    )
    for triple in result:
        new_data_graph.add(triple)


def add_categorical_concepts_definition_source(graph: Graph, new_data_graph: Graph):
    result = graph.query(
        """
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX urnc: <urn:class:>
        PREFIX urnp: <urn:property:>
        PREFIX tern: <https://w3id.org/tern/ontologies/tern/>
        PREFIX dcterms: <http://purl.org/dc/terms/>

        CONSTRUCT {
            ?categorical_concept skos:definition ?definition ;
                                dcterms:source ?source .
        }
        WHERE {
            ?_categorical_concept_metadata a urnc:CategoricalConceptMeta ;
                            urnp:categoricalConcept ?categorical_concept ;
                            urnp:conceptDefinition ?definition ;
                            urnp:conceptSource ?source .
        }
    """
    )
    for triple in result:
        new_data_graph.add(triple)


def add_skos_concept_collection_relationship(graph: Graph, new_data_graph: Graph):
    result = graph.query(
        """
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX urnc: <urn:class:>
        PREFIX urnp: <urn:property:>
        PREFIX tern: <https://w3id.org/tern/ontologies/tern/>
        PREFIX dcterms: <http://purl.org/dc/terms/>

        CONSTRUCT {
            ?concept tern:isMemberOf ?collection .
        }
        WHERE {
            ?concept a skos:Concept .
            ?collection a skos:Collection ;
                        skos:member ?concept .
        }
    """
    )
    for triple in result:
        new_data_graph.add(triple)


def add_modules_submodules_relationship(graph: Graph, new_data_graph: Graph):
    result = graph.query(
        """
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX urnc: <urn:class:>
        PREFIX urnp: <urn:property:>
        PREFIX tern: <https://w3id.org/tern/ontologies/tern/>
        PREFIX dcterms: <http://purl.org/dc/terms/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

        CONSTRUCT {
            ?subProtocol tern:isMemberOf ?protocol .
        }
        WHERE {
            ?protocol skos:memberList/rdf:rest*/rdf:first ?subProtocol .
        }
    """
    )
    for triple in result:
        new_data_graph.add(triple)


def expand_graph(graph: Graph, new_data_graph: Graph):
    add_observable_property_relationships(graph, new_data_graph)
    add_observable_property_categorical_values_collections(graph, new_data_graph)
    add_categorical_concepts_definition_source(graph, new_data_graph)
    add_skos_concept_collection_relationship(graph, new_data_graph)
    add_modules_submodules_relationship(graph, new_data_graph)
    # ... other graph expansion functions
