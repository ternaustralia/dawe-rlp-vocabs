# DAWE RLP Controlled Vocabularies

Source Excel files for DAWE RLP controlled vocabularies.

The Excel files are converted to RDF using the Python tool [excel2rdf](https://pypi.org/project/excel2rdf/) via the Python script `generate.py`.

## Running

### Virtual environment
Set up Python virtual environment.

```bash
python3 -m venv venv
```

Activate Python virtual environment. The following instruction only works on macOS and Linux distros.

```bash
source venv/bin/activate
```

For Windows, run the following.

```bash
.\venv\Scripts\activate
```

### Install dependencies
Install Python dependencies.
```bash
pip install -r requirements.txt
```

### Download Excel files from Google Drive using a Google Service Account

See the [authentication section](https://docs.iterative.ai/PyDrive2/quickstart/#authentication) from PyDrive2's documentation on creating a new Google Cloud Platform project. 

Under APIs and Services, create a new Service Account. Create a new key for the Service Account. Download the key as a JSON file and save it as `client_secrets.json`. 

Ensure `client_secrets.jsonn` is in the root of this project's directory.

### Run the script
Run the Python script to convert the data in the Excel files to RDF. The output is RDF serialised as Turtle.

```bash
python generate.py
```

You should see some logging like the following:

```
INFO:generate.py:Downloading vocab-sources/protocols-collection.xlsx with id 1RLOQvSXfLaJ-eRSfWa6KPDXTn4a_MRNA
INFO:oauth2client.transport:Attempting refresh to obtain initial access_token
INFO:oauth2client.client:Refreshing access_token
INFO:generate.py:Downloading vocab-sources/observable-properties-by-module.xlsx with id 1kzR1BTPgARnWfHh_mK-xx15TEl1D2bky
INFO:generate.py:Downloading vocab-sources/protocols-plot-description.xlsx with id 1Dbrhl1gTIMn7VaijCiSbQc63ybpQmXd_
INFO:generate.py:Downloading vocab-sources/plot-description-observable-properties-collection.xlsx with id 1qPJ3I4NhfnKLDiqBQVkolAYBDbSZEPQ7
INFO:generate.py:Downloading vocab-sources/plot-description-observable-properties.xlsx with id 1wmEWPnAmo2kunMH_zLSq3HkXckY8Ml33
INFO:generate.py:Downloading vocab-sources/protocols-cover.xlsx with id 11OD9vTq8TDCOyHmOZHutWr-1dK6t7Zsv
INFO:generate.py:Downloading vocab-sources/cover-observable-properties-collection.xlsx with id 1jUcXQ1HQ9RxxJeYxWp7dosjdwFr0vVw2
INFO:generate.py:Downloading vocab-sources/cover-observable-properties.xlsx with id 1nw2KeprNMmIYYzHz_T2-bD3IoSyj2ayb
INFO:generate.py:Downloading vocab-sources/protocols-floristics.xlsx with id 1BryGRR1JYl_2eLisqrF9SZyw7ZnRj-Ix
INFO:generate.py:Downloading vocab-sources/floristics-observable-properties-collection.xlsx with id 1tWaBUfSol735NzpPeTTpYIpkNE9JaIzJ
INFO:generate.py:Downloading vocab-sources/floristics-observable-properties.xlsx with id 1gsS0NgpF1Njs-S4hW0rSTQJbpi-N7oEl
INFO:generate.py:Downloading vocab-sources/protocols-plant-tissue-vouchering.xlsx with id 19ghAUOE0GGFw5UDxmEyOtFJRgmVy6XRO
INFO:generate.py:Downloading vocab-sources/protocols-vegetation-mapping.xlsx with id 1Ofkweb9pNvMT4OT53P7NNh-v4FevjbTs
INFO:generate.py:Downloading vocab-sources/vegetation-mapping-observable-properties-collection.xlsx with id 1OnomiXiDzHhTNrM5p1xINguiP5tPrydF
INFO:generate.py:Downloading vocab-sources/vegetation-mapping-observable-properties.xlsx with id 1BiWiCK0O3OZPfsyUBIhdx0HyFTb-Xy-S
INFO:generate.py:Downloading vocab-sources/protocols-opportunistic-observations.xlsx with id 1dTfOpJ9l68qVs9msUWQVDfilWExG_NkW
INFO:generate.py:Downloading vocab-sources/opportunistic-observations-observable-properties-collection.xlsx with id 15KybrSynrOW26eDFy9ZxQzR4BdYTtz_N
INFO:generate.py:Downloading vocab-sources/opportunistic-observations-observable-properties.xlsx with id 1AMWD4_SZQBbut4MxYqJPE8IvxdJFMzkJ
INFO:generate.py:Downloading vocab-sources/protocols-photopoints.xlsx with id 1cei9yda7SRMSdDD9VRL-DAGTbHJhSXEZ
ERROR:generate.py:API endpoint https://dev.core-api.paratoo.tern.org.au/lut-soils-substrates returned no data.
INFO:generate.py:PySHACL conforms output: False
INFO:generate.py:sh:Violation exists: True
INFO:generate.py:sh:Warning exists: True
INFO:generate.py:sh:Info exists: False
```

You should now have an `output.ttl` file in the same directory.

The logs at the end summarise the types of [severities](https://www.w3.org/TR/shacl/#results-severity) found in the [validation results](https://www.w3.org/TR/shacl/#results-validation-result). 

## Contact

Edmond Chuc  
e.chuc@uq.edu.au
