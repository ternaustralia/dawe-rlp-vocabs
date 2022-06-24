import requests
from jinja2 import Template

graphdb_configuration_template = Template(
    """
#
# RDF4J configuration template for a GraphDB Free repository
#
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix rep: <http://www.openrdf.org/config/repository#>.
@prefix sr: <http://www.openrdf.org/config/repository/sail#>.
@prefix sail: <http://www.openrdf.org/config/sail#>.
@prefix owlim: <http://www.ontotext.com/trree/owlim#>.
[] a rep:Repository ;
    rep:repositoryID "{{ repository_id }}" ;
    rdfs:label "{{ repository_title }}" ;
    rep:repositoryImpl [
        rep:repositoryType "graphdb:FreeSailRepository" ;
        sr:sailImpl [
            sail:sailType "graphdb:FreeSail" ;
            
            owlim:base-URL "http://example.org/owlim#" ;
            owlim:defaultNS "" ;
            owlim:entity-index-size "10000000" ;
            owlim:entity-id-size  "32" ;
            owlim:imports "" ;
        	owlim:repository-type "file-repository" ;
            owlim:ruleset "empty" ;
            owlim:storage-folder "storage" ;
 
            owlim:enable-context-index "true" ;
            owlim:enablePredicateList "true" ;
            owlim:in-memory-literal-properties "true" ;
            owlim:enable-literal-index "true" ;
            owlim:check-for-inconsistencies "false" ;
            owlim:disable-sameAs  "true" ;
            owlim:query-timeout  "0" ;
            owlim:query-limit-results  "0" ;
            owlim:throw-QueryEvaluationException-on-timeout "false" ;
            owlim:read-only "false" ;
        ]
    ].
"""
)


def create(graphdb_url: str, repository_id: str, repository_title: str) -> bool:
    """Create a GraphDB repository.
    Returns True on success. Raises a HTTPError if repository already exists.
    """
    data = Template.render(
        graphdb_configuration_template,
        repository_id=repository_id,
        repository_title=repository_title,
    )
    headers = {"content-type": "text/turtle"}
    r = requests.put(
        f"{graphdb_url}/repositories/{repository_id}", data=data, headers=headers
    )
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise requests.exceptions.HTTPError(r.text) from err
    return True


def insert(
    graphdb_url: str,
    repository_id: str,
    data: str,
    content_type: str,
    context: str = "null",
):
    """Load and overwrite data in a GraphDB repository's named graph.

    :data: The actual RDF data, not file path.
    """
    headers = {"content-type": f"{content_type}"}
    r = requests.put(
        f"{graphdb_url}/repositories/{repository_id}/statements",
        params={"context": context},
        data=data,
        headers=headers,
    )
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise requests.exceptions.HTTPError(r.text) from err
    return True
