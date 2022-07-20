[![Publish to prod environment of Research Vocabularies Australia](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/publish_to_rva_prod_env.yml/badge.svg)](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/publish_to_rva_prod_env.yml)
[![Publish to demo environment of Research Vocabularies Australia](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/publish_to_rva_demo_env.yml/badge.svg)](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/publish_to_rva_demo_env.yml)
[![Publish on release to GraphDB](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/publish_to_graphdb.yml/badge.svg)](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/publish_to_graphdb.yml)

# NRM Controlled Vocabularies

This repository contains the source data for the controlled vocabularies used by the Natural Resource Management (NRM) field survey collection protocols.

The controlled vocabularies are published to ARDC's Research Vocabularies Australia as [Natural Resource Management Survey Vocabularies](https://vocabs.ardc.edu.au/viewById/639). The NRM controlled vocabularies can also be viewed on TERN's Linked Data website at https://linkeddata.tern.org.au/viewers/dawe-vocabs.

The NRM controlled vocabularies use persistent identifiers issued by the Australian Government Linked Data Working Group (AGLDWG). The base URI issued for this project is:

```
https://linked.data.gov.au/def/nrm/
```

Submission: [AGLDWG PID Catalogue](https://catalogue.linked.data.gov.au/index.php/resource/239).

The NRM controlled vocabularies are located in the `vocab_files/` directory.

---

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

### Code formatting standards

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
ontotools dir normalize .
```

## Contact

Edmond Chuc  
e.chuc@uq.edu.au

Junrong Yu  
junrong.yu@uq.edu.au
