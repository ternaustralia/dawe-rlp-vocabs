import pandas as pd
import requests
import json
from rdflib import Graph, Namespace, URIRef
from datetime import datetime
import glob
import os
import logging
import ssl

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
downloads_folder = "Downloads/LUTs"
log_filename = os.path.join(downloads_folder, f"debug_{timestamp}.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_filename), logging.StreamHandler()],
)

SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")


def load_turtle_files(folder_path):
    g = Graph()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".ttl"):
                turtle_file = os.path.join(root, file)
                try:
                    g.parse(turtle_file, format="turtle")
                except Exception as e:
                    logging.error(f"Error loading {turtle_file}: {str(e)}")
    return g


def get_endpoint_labels(endpoint_url):
    try:
        response = requests.get(endpoint_url)
        data = response.json()
        return [item["attributes"]["label"].lower() for item in data["data"]]
    except Exception as e:
        logging.error(f"Error fetching endpoint {endpoint_url}: {str(e)}")
        return []


def get_collection_labels(g, collection_iri):
    collection_uri = URIRef(collection_iri)
    labels = set()

    if (
        collection_iri
        == "https://linked.data.gov.au/def/alum/5"
    ):
        for concept in g.subjects(SKOS.broader, collection_uri):
            for label in g.objects(concept, SKOS.prefLabel):
                labels.add(str(label).lower())
    elif collection_iri in [
        "https://linked.data.gov.au/def/alum",
        "http://linked.data.gov.au/dataset/bioregion/IBRA7",
    ]:
        for concept in g.subjects(SKOS.inScheme, collection_uri):
            for label in g.objects(concept, SKOS.prefLabel):
                labels.add(str(label).lower())
    else:
        for member in g.objects(collection_uri, SKOS.member):
            for label in g.objects(member, SKOS.prefLabel):
                labels.add(str(label).lower())

    return labels


def main():
    ssl._create_default_https_context = ssl._create_unverified_context

    logging.info("Loading Turtle files...")
    luts_graph = load_turtle_files("vocab_files")
    logging.info(f"Loaded graph with {len(luts_graph)} triples")

    sheet1_url = "https://docs.google.com/spreadsheets/d/1pwZMpUOevx3xcrM0DYBHTdlssXFl6hOPLIOBWueQUS4/edit#gid=1418476783"
    sheet2_url = "https://docs.google.com/spreadsheets/d/1pwZMpUOevx3xcrM0DYBHTdlssXFl6hOPLIOBWueQUS4/edit#gid=1843516922"

    sheet1_url = sheet1_url.replace("/edit#gid=", "/export?format=csv&gid=")
    sheet2_url = sheet2_url.replace("/edit#gid=", "/export?format=csv&gid=")

    try:
        df1 = pd.read_csv(sheet1_url)
        df2 = pd.read_csv(sheet2_url)
        logging.info(f"Successfully read sheets. Sheet1: {len(df1)} rows, Sheet2: {len(df2)} rows")
    except Exception as e:
        logging.error(f"Error reading sheets: {str(e)}")
        return

    missing_labels_file = os.path.join(downloads_folder, f"missing_luts_{timestamp}.log")
    excel_data = []

    with open(missing_labels_file, "w") as log_file:
        for _, row in df1.iterrows():
            if (
                pd.notna(row["Modules"])
                and pd.notna(row["Paratoo endpoints"])
                and "To be confirmed" not in row["Paratoo endpoints"]
            ):

                logging.info(
                    f"Processing endpoint: {row['Paratoo endpoints']}, collection: {row['NRM Categorical Collection']}"
                )
                endpoint_labels = get_endpoint_labels(row["Paratoo endpoints"])
                collection_labels = get_collection_labels(
                    luts_graph, row["NRM Categorical Collection"]
                )

                for label in endpoint_labels:
                    if label not in collection_labels:
                        found = False
                        matching_rows = df2[
                            (df2["paratoo-source"] == row["Paratoo endpoints"])
                            & (df2["NRM Collection URI"] == row["NRM Categorical Collection"])
                        ]

                        for _, sheet2_row in matching_rows.iterrows():
                            missing_values = (
                                sheet2_row["missing values"].lower().split(",")
                                if pd.notna(sheet2_row["missing values"])
                                else []
                            )
                            if label in [mv.strip() for mv in missing_values]:
                                if pd.notna(sheet2_row["NRM Concept URI"]):
                                    concept_uri = URIRef(sheet2_row["NRM Concept URI"])
                                    collection_uri = URIRef(row["NRM Categorical Collection"])
                                    has_member = (
                                        collection_uri,
                                        SKOS.member,
                                        concept_uri,
                                    ) in luts_graph
                                    has_inScheme = (
                                        concept_uri,
                                        SKOS.inScheme,
                                        collection_uri,
                                    ) in luts_graph
                                    has_broader = (
                                        concept_uri,
                                        SKOS.broader,
                                        collection_uri,
                                    ) in luts_graph

                                    if has_member or has_inScheme or has_broader:
                                        found = True
                                        break

                        if not found:
                            message = f"The value '{label}' in Paratoo endpoint '{row['Paratoo endpoints']}' is missing in categorical collection '{row['NRM Categorical Collection']}'\n"
                            log_file.write(message)
                            excel_data.append(
                                {
                                    "paratoo-source": row["Paratoo endpoints"],
                                    "NRM Collection URI": row["NRM Categorical Collection"],
                                    "missing values": label,
                                }
                            )

    # Write to Excel file
    if excel_data:
        excel_df = pd.DataFrame(excel_data)
        excel_file = os.path.join(downloads_folder, f"missing_values_{timestamp}.xlsx")
        excel_df.to_excel(excel_file, index=False)
        logging.info(f"Excel file created: {excel_file}")


if __name__ == "__main__":
    main()
