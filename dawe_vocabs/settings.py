from os import environ

try:
    from dotenv import load_dotenv

    load_dotenv()
except:
    pass

from dawe_vocabs.schemas import LUTSchema, ExcelVocab


from typing import List

from rdflib import Namespace

# Settings

# Google API key.
# This is required to download the Excel files from Google Drive.
api_key = environ["GOOGLE_API_KEY"]

# Show table result in logging output.
show_table_result = False

# Base URI used for all generated vocabularies.
base_uri = Namespace("https://linked.data.gov.au/def/test/dawe-cv/")

# SHACL shapes file.
shapes_file = "shapes.shapes.ttl"

# Look up tables to be generated.
lut_configs: List[LUTSchema] = [
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-landform-patterns",
        "Landform pattern values",
        "A collection of landform pattern values and its codes.",
        "19d91a7a-2733-4b84-9d2b-4bda4808c003",
        "landform pattern values",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-landform-elements",
        "Landform element values",
        "A collection of landform element values and its codes.",
        "c1a58967-cb12-4c2c-a7ca-9cee2589919c",
        "landform element values",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-site-slopes",
        "Site slope values",
        "A collection of site slope values and its codes.",
        "d893e669-c530-4bc3-a057-a5799ffcb5db",
        "site slope values",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-soils-surface-strew-sizes",
        "Soil surface strew size values",
        "A collection of soil surface strew size values and its codes.",
        "3b25ce0f-9eb7-4d2d-97ce-143858cfd4d4",
        "soil surface strew size values",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-soils-lithologies",
        "Soil lithology values",
        "A collection of soil lithology values and its codes.",
        "1d50eb79-685f-45ea-84b4-627154eddede",
        "soil lithology values",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-veg-structural-formations",
        "Vegetation structural formation values",
        "A collection of vegetation structural formation values and its codes.",
        "6e9baf51-566e-4a5d-93c4-a6e097dc364d",
        "vegetation structural formation values",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-climatic-conditions",
        "Climatic condition values",
        "A collection of climatic condition values and its codes.",
        "2ebfee89-92db-44b3-bb89-06dd92798ae6",
        "climatic condition values",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-veg-growth-stages",
        "Vegetation growth stage",
        "A collection of vegetation growth stage values and its codes.",
        "89c02383-fb5e-4acd-b248-902a2d579170",
        "vegetation growth stage values",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-fire-histories",
        "Fire history values",
        "A collection of fire history values and its codes.",
        "6e9d2f51-ce64-4c67-8391-d14a8bf96b6b",
        "fire history values",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-disturbances",
        "Disturbance type values",
        "A collection of disturbance type values and its codes.",
        "f5a470e8-d29f-4ff6-b50d-529b0444dbe4",
        "disturbance type values",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-veg-growth-forms",
        "Vegetation growth form values",
        "A collection of vegetation growth form values and its codes.",
        "d0fc07a7-3ec9-45ed-8850-885a32828d3c",
        "vegetation growth form values",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-veg-height-classes",
        "Vegetation height class values",
        "A collection of vegetation height class values and its codes.",
        "b1b05cd1-3b85-4639-a6af-799a34d88d43",
        "vegetation height class values",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-soils-substrates",
        "Soil substrate values",
        "A collection of soil substrate values and its codes.",
        "b061d7db-a608-4062-96d4-b367d6d9a792",
        "soil substrate values",
    ),
]

# Excel files to be generated using excel2rdf.
excel_files_dir = "vocab-sources"
excel_files = (
    ExcelVocab(
        "vocab-sources/protocols-collection.xlsx",
        "https://drive.google.com/uc?export=download&id=1RLOQvSXfLaJ-eRSfWa6KPDXTn4a_MRNA",
    ),
    ExcelVocab(
        "vocab-sources/observable-properties-by-module.xlsx",
        "https://drive.google.com/uc?export=download&id=1kzR1BTPgARnWfHh_mK-xx15TEl1D2bky",
    ),
    ExcelVocab(
        "vocab-sources/protocols-plot-description.xlsx",
        "https://drive.google.com/uc?export=download&id=1Dbrhl1gTIMn7VaijCiSbQc63ybpQmXd_",
    ),
    ExcelVocab(
        "vocab-sources/plot-description-observable-properties-collection.xlsx",
        "https://drive.google.com/uc?export=download&id=1qPJ3I4NhfnKLDiqBQVkolAYBDbSZEPQ7",
    ),
    ExcelVocab(
        "vocab-sources/plot-description-observable-properties.xlsx",
        "https://drive.google.com/uc?export=download&id=1wmEWPnAmo2kunMH_zLSq3HkXckY8Ml33",
    ),
    ExcelVocab(
        "vocab-sources/protocols-cover.xlsx",
        "https://drive.google.com/uc?export=download&id=11OD9vTq8TDCOyHmOZHutWr-1dK6t7Zsv",
    ),
    ExcelVocab(
        "vocab-sources/cover-observable-properties-collection.xlsx",
        "https://drive.google.com/uc?export=download&id=1jUcXQ1HQ9RxxJeYxWp7dosjdwFr0vVw2",
    ),
    ExcelVocab(
        "vocab-sources/cover-observable-properties.xlsx",
        "https://drive.google.com/uc?export=download&id=1nw2KeprNMmIYYzHz_T2-bD3IoSyj2ayb",
    ),
    ExcelVocab(
        "vocab-sources/protocols-floristics.xlsx",
        "https://drive.google.com/uc?export=download&id=1BryGRR1JYl_2eLisqrF9SZyw7ZnRj-Ix",
    ),
    ExcelVocab(
        "vocab-sources/floristics-observable-properties-collection.xlsx",
        "https://drive.google.com/uc?export=download&id=1tWaBUfSol735NzpPeTTpYIpkNE9JaIzJ",
    ),
    ExcelVocab(
        "vocab-sources/floristics-observable-properties.xlsx",
        "https://drive.google.com/uc?export=download&id=1gsS0NgpF1Njs-S4hW0rSTQJbpi-N7oEl",
    ),
    ExcelVocab(
        "vocab-sources/protocols-plant-tissue-vouchering.xlsx",
        "https://drive.google.com/uc?export=download&id=19ghAUOE0GGFw5UDxmEyOtFJRgmVy6XRO",
    ),
    ExcelVocab(
        "vocab-sources/protocols-vegetation-mapping.xlsx",
        "https://drive.google.com/uc?export=download&id=1Ofkweb9pNvMT4OT53P7NNh-v4FevjbTs",
    ),
    ExcelVocab(
        "vocab-sources/vegetation-mapping-observable-properties-collection.xlsx",
        "https://drive.google.com/uc?export=download&id=1OnomiXiDzHhTNrM5p1xINguiP5tPrydF",
    ),
    ExcelVocab(
        "vocab-sources/vegetation-mapping-observable-properties.xlsx",
        "https://drive.google.com/uc?export=download&id=1BiWiCK0O3OZPfsyUBIhdx0HyFTb-Xy-S",
    ),
    ExcelVocab(
        "vocab-sources/protocols-opportunistic-observations.xlsx",
        "https://drive.google.com/uc?export=download&id=1dTfOpJ9l68qVs9msUWQVDfilWExG_NkW",
    ),
    ExcelVocab(
        "vocab-sources/opportunistic-observations-observable-properties-collection.xlsx",
        "https://drive.google.com/uc?export=download&id=15KybrSynrOW26eDFy9ZxQzR4BdYTtz_N",
    ),
    ExcelVocab(
        "vocab-sources/opportunistic-observations-observable-properties.xlsx",
        "https://drive.google.com/uc?export=download&id=1AMWD4_SZQBbut4MxYqJPE8IvxdJFMzkJ",
    ),
    ExcelVocab(
        "vocab-sources/protocols-photopoints.xlsx",
        "https://drive.google.com/uc?export=download&id=1cei9yda7SRMSdDD9VRL-DAGTbHJhSXEZ",
    ),
)

# Output file name.
output_filename = "output.ttl"
