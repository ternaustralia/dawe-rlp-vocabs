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

### Set credentials to access Google Drive programmatically
Set the environment variable for your Google API key to download the Excel files from Google Drive.

See https://cloud.google.com/docs/authentication/api-keys for more information.

If you're running locally, you can create a `.env` file in the project directory with the following content and the application will read the key from there.

```
GOOGLE_API_KEY=<your-google-api-key>
```

### Run the script
Run the Python script to convert the data in the Excel files to RDF. The output is RDF serialised as Turtle.

```bash
python generate.py
```

You should now have an `output.ttl` file in the same directory.

Some logging is performed when running the script. 
```
INFO:generate.py:PySHACL conforms output: False
INFO:generate.py:sh:Violation exists: False
INFO:generate.py:sh:Warning exists: True
INFO:generate.py:sh:Info exists: False
```

The logs summarise the types of [severities](https://www.w3.org/TR/shacl/#results-severity) found in the [validation results](https://www.w3.org/TR/shacl/#results-validation-result). 

## Contact

Edmond Chuc  
e.chuc@uq.edu.au
