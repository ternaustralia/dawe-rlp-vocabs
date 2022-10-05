"""diff.py

Perform a diff of the RDF source files in this repository with the RDF data
in the remote GraphDB repository.

Outputs two files:
    - only_in_local.ttl - a set of triples that only exist in the source files in this repository
    - only_in_remote.ttl - a set of triples that only exist in the remote GraphDB repository
"""

from pathlib import Path

import requests
from rdflib import Graph

path = Path("vocab_files")

files = [f for f in path.glob("**/*.ttl")]

local_graph = Graph()

for file in files:
    local_graph.parse(file, format="turtle")

response = requests.get(
    "https://graphdb.tern.org.au/repositories/dawe_vocabs_core/statements?context=<https://linked.data.gov.au/def/nrm/>",
    headers={"accept": "text/turtle"},
)
try:
    response.raise_for_status()
except Exception as err:
    raise Exception(response.text) from err

remote_graph = Graph()
remote_graph.parse(data=response.text, format="turtle")

local_graph_diff = local_graph - remote_graph
remote_graph_diff = remote_graph - local_graph

print("in local graph but not in remote graph")
print(len(local_graph_diff))
local_graph_diff.serialize("only_in_local.ttl", format="turtle")

print("in remote graph but not in local graph")
print(len(remote_graph_diff))
remote_graph_diff.serialize("only_in_remote.ttl", format="turtle")
