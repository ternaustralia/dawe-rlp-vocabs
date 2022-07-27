[![Publish to prod environment of Research Vocabularies Australia](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/publish_to_rva_prod_env.yml/badge.svg)](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/publish_to_rva_prod_env.yml)
[![Publish to demo environment of Research Vocabularies Australia](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/publish_to_rva_demo_env.yml/badge.svg)](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/publish_to_rva_demo_env.yml)
[![Publish on release to GraphDB](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/publish_to_graphdb.yml/badge.svg)](https://github.com/ternaustralia/dawe-rlp-vocabs/actions/workflows/publish_to_graphdb.yml)

# NRM Controlled Vocabularies

This repository contains the source data for the controlled vocabularies used by the Natural Resource Management (NRM) field survey collection protocols.

The controlled vocabularies are published to ARDC's Research Vocabularies Australia as [Natural Resource Management Survey Vocabularies](https://vocabs.ardc.edu.au/viewById/639). The NRM controlled vocabularies can also be viewed on TERN's Linked Data website at https://linkeddata.tern.org.au/viewers/dawe-vocabs.

The NRM controlled vocabularies use persistent identifiers issued by the [Australian Government Linked Data Working Group](https://www.linked.data.gov.au/) (AGLDWG). The base URI issued for this project is:

```
https://linked.data.gov.au/def/nrm/
```

Submission: [AGLDWG PID Catalogue](https://catalogue.linked.data.gov.au/index.php/resource/239).

The NRM controlled vocabularies are located in the [vocab_files/](vocab_files/) directory.

---

## Pull requests

A new pull request (PR) automatically runs all the tests and validations on the controlled vocabularies. If possible, fix any failing checks and wait for feedback and/or approval from maintainers. A PR always requires at least 1 maintainer who has approved it before it is merged into the `main` branch.

See the next two sections on how to make changes and submitting changes as PRs for review.

## Editing in the browser

The source files of the controlled vocabularies are located in [vocab_files/](vocab_files/) and the editing process can be performed entirely in the browser. If you are looking to edit the files on your local host system, please see [Editing locally](#editing-locally).

### Editing on GitHub

Browse and edit the files directly in the browser at https://github.com/ternaustralia/dawe-rlp-vocabs/tree/main/vocab_files. Alternatively, you can browse the controlled vocabularies at https://linkeddata.tern.org.au/viewers/dawe-vocabs and click the `schema:url` value to open the corresponding source file on GitHub.

Once you have opened a file, e.g., [basal-area-count.ttl](https://github.com/ternaustralia/dawe-rlp-vocabs/blob/main/vocab_files/observable_property_concepts/basal-area-count.ttl), you can click the pencil icon to edit. The drop-down will provide two editing options:

1. `Edit this file` - edit directly on GitHub [[try me](https://github.com/ternaustralia/dawe-rlp-vocabs/edit/main/vocab_files/observable_property_concepts/basal-area-count.ttl)]
2. `Open in github.dev` - edit in an instance of Visual Studio Code in the browser with full git support [[try me](https://github.dev/ternaustralia/dawe-rlp-vocabs/blob/main/vocab_files/observable_property_concepts/basal-area-count.ttl)]

Note that you can also open the entire project directly in Visual Studio Code in the browser by going to https://github.com/ternaustralia/dawe-rlp-vocabs and pressing `.` on your keyboard. This provides the benefit of editing the files with the full text-editing powers of Visual Studio Code.

### Making changes

The `main` branch in the GitHub repository is protected. All changes must be submitted as a PR and reviewed and approved by the maintainers. If you have write access to the GitHub repository, you will need to create a new branch to make your changes and then submit it as a PR. If you do not have write access, you will need to fork the GitHub repository, make your changes in your fork and then submit a PR. GitHub makes it relatively pain-free to make changes, commit them and then create a PR regardless of which editing option you choose.

---

## Editing locally

This section is only relevant to those who are looking to make changes to the Python codebase, update tests or making other non-vocab related changes. If you are simply looking to make edits to the controlled vocabularies, the easiest method is to follow the instructions in [Editing the controlled vocabularies in the browser](#editing-the-controlled-vocabularies-in-the-browser).

Open the repository in Visual Studio Code in a devcontainer. This can be done by running `command + shift + p` and selecting `Remote-Containers: Rebuild Container`. Note that Docker Desktop needs to be installed.

### Tests

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

Pull from the Strapi API endpoints defined in [src/dawe_nrm/api/categorical_values/endpoints.py](src/dawe_nrm/api/categorical_values/endpoints.py) and write Turtle files to [vocab_files/categorical_collections/luts](vocab_files/categorical_collections//luts/).

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

---

## Publishing

The NRM controlled vocabularies are published to the ARDC Research Vocabularies Australia (RVA) registry. Each publication is taking a snapshot of the current repository's state in the `main` branch and publishing it to the respective environments. This repository publishes to two different RVA environments, production and demo.

### Test (demo) environment

The demo publication is located at https://demo.vocabs.ardc.edu.au/viewById/927 and is published automatically using GitHub Actions on each GitHub _prerelease_. Prerelease versions follow [Semantic Versioning](https://semver.org/) and are in the format of `MAJOR.MINOR.PATCH-dev.gitshorthash`. E.g. `0.1.3-dev.5440029`.

### Production environment

The production publication is located at https://vocabs.ardc.edu.au/viewById/639 and is published automatically using GitHub Actions on each GitHub _release_. Release versions follow [Semantic Versioning](https://semver.org/) and are in the format of `MAJOR.MINOR.PATCH` and must not have additional labels. E.g. `0.1.3`.

In addition to publishing to RVA, the production release also publishes to TERN's GraphDB database. This database is deployed on a powerful server and drives TERN's Linked Data website and the NRM controlled vocabularies viewer at https://linkeddata.tern.org.au/viewers/dawe-vocabs.

### Creating releases and prereleases

1. Create a new release or prerelease at https://github.com/ternaustralia/dawe-rlp-vocabs/releases/new
2. Create a new tag conforming to Semantic Versioning
   - Don't forget the release and prerelease versioning formats as described previously
   - If it is a prerelease, grab the latest commit's short hash (the first 7 characters of the git hash)
3. Click _Generate release notes_ to automatically generate the _Release title_ and _Description_ of the release.
4. Tick _This is a pre-release_ checkbox if it is a prerelease
5. Click _Publish release_
6. Go to https://github.com/ternaustralia/dawe-rlp-vocabs/actions and a workflow should run to publish the new release or prerelease to RVA (and also GraphDB if it's a release)

### Reverting a release or prerelease

In case a release or prerelease was published by accident, follow the steps to get the state back to before it was published.

1. Go to https://github.com/ternaustralia/dawe-rlp-vocabs/releases and delete the release
2. Go to https://github.com/ternaustralia/dawe-rlp-vocabs/tags and you should see the tag with the new release
   - To delete the tag:
     - With repository access, on the terminal type `git push --delete origin tagname`.
     - This will delete the tag in the origin (i.e., GitHub).
     - Don't forget to replace `tagname` with the actual tag, which is usually the Semantic Version value as described previously
     - The tag at https://github.com/ternaustralia/dawe-rlp-vocabs/tags should now be deleted

## Contact

Edmond Chuc  
e.chuc@uq.edu.au

Junrong Yu  
junrong.yu@uq.edu.au
