[![Deploy on release to GraphDB](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/deploy_to_graphdb.yml/badge.svg)](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/deploy_to_graphdb.yml)

# DAWE RLP Controlled Vocabularies

> Will be rebranded to DAWE NRM Controlled Vocabularies soon.

Proposed base URI of DAWE NRM Controlled Vocabularies:

```
https://linked.data.gov.au/def/nrm/
```

Proposal submitted to [AGLDWG PID Catalogue](https://catalogue.linked.data.gov.au/index.php/resource/239).

## Running

Open the repository in Visual Studio Code in a devcontainer. This can be done by running `command + shift + p` and selecting `Remote-Containers: Rebuild Container`. Note that Docker Desktop needs to be installed.

## Tests

[![Tests](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/test.yml/badge.svg)](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/test.yml)

Run tests and generate a HTML coverage report.

```
make test
```

View HTML coverage report in a browser. This runs a Python web server on `htmlcov/`.

```
make htmlcov
```

### Generate categorical values

Some of the controlled vocabularies in this repository are synced with an upstream data source provided by TERN's Ecosystem Surveillance. These _categorical values_, also known as look-up tables (LUTs) are pulled and transformed into SKOS controlled vocabularies.

Pull from the Strapi API endpoints defined in `src/dawe_nrm/api/categorical_values/endpoints.py` and write Turtle files to `vocab_files/categorical_collections/luts`.

```
make luts
```

Check if upstream LUTs data have changed by running:

```
python luts.py -p remote_data_dir -v
```

This checks to ensure the upstream data is the same as the local copy in this repository. If the data is not isomorphic, the program will return a standard exit code `1`.

#### Scheduled check

A scheduled check for changes in the upstream LUTs data runs every 30 minutes in GitHub Actions. The result is notified in TERN's Data Service and Analytics' Microsoft Teams and Slack channels.

[![Check upstream LUTs for changes](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/luts.yml/badge.svg)](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/luts.yml)

The above badge indicates whether there are changes in the upstream LUTs.

- `passing` - no changes
- `failing` - new changes detected

See `.github/workflows/luts.yml` for more information.

### Code quality

Run black to auto-format Python code.

```
black .
```

Run isort to auto-format Python code imports.

```
isort .
```

Run RDF Turtle formatter.

```
make format-turtle
```

Note: _Not implemented yet_.

## Contact

Edmond Chuc  
e.chuc@uq.edu.au

Junrong Yu  
junrong.yu@uq.edu.au
