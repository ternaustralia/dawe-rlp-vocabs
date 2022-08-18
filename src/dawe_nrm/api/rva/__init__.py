from pathlib import Path
from typing import Tuple

import httpx

PROD_URL = "https://vocabs.ardc.edu.au/registry/api/"
DEV_URL = "https://demo.vocabs.ardc.edu.au/registry/api/"


class RVAError(Exception):
    """RVA Error - raised when a request fails"""

    pass


def get_vocabulary(id_: str | int, dev: bool = False) -> dict:
    """Get the public vocabulary metadata by ID

    By default, only the top-level metadata of the vocabulary is returned.

    See: https://documentation.ardc.edu.au/display/DOC/Vocabulary+Registry+API+methods#VocabularyRegistryAPImethods-getVocabularyById
    """
    url = (DEV_URL if dev else PROD_URL) + f"resource/vocabularies/{id_}"
    headers = {"accept": "application/json"}
    response = httpx.get(url, headers=headers, timeout=60)

    if response.status_code != 200:
        raise RVAError(f"{response.status_code} - {response.text}")

    return response.json()


def get_vocabulary_edit(
    id_: str | int, auth: Tuple[str, str], dev: bool = False
) -> dict:
    """Get the entire vocabulary metadata by ID

    This is provided to assist API users who are updating their own vocabularies.

    See: https://documentation.ardc.edu.au/display/DOC/Vocabulary+Registry+API+methods#VocabularyRegistryAPImethods-getVocabularyByIdEdit
    """
    url = (DEV_URL if dev else PROD_URL) + f"resource/vocabularies/{id_}/edit"
    headers = {"accept": "application/json"}
    response = httpx.get(url, headers=headers, auth=auth, timeout=60)

    if response.status_code != 200:
        raise RVAError(f"{response.status_code} - {response.text}")

    return response.json()


def create_upload(
    file_bytes_str: Path | bytes | str,
    file_name: str,
    owner: str,
    auth: Tuple[str, str],
    file_format: str = "TTL",
    dev: bool = False,
) -> Tuple[str, str]:
    """Upload a file

    Returns a tuple containing the upload ID and the filename of the
    uploaded artifact, after passing through a sanitization process.

    See: https://documentation.ardc.edu.au/display/DOC/Vocabulary+Registry+API+methods#VocabularyRegistryAPImethods-createUpload
    """
    url = (DEV_URL if dev else PROD_URL) + "resource/uploads"
    headers = {"accept": "application/json"}
    params = {"format": file_format, "owner": owner}

    if isinstance(file_bytes_str, Path):
        file = open(file_bytes_str, "rb")
    elif isinstance(file_bytes_str, bytes):
        file = file_bytes_str
    elif isinstance(file_bytes_str, str):
        file = file_bytes_str.encode("utf-8")
    else:
        raise TypeError(
            f"Expected file_bytes_str to be a Path, bytes or str. Instead, got {type(file_bytes_str)}"
        )

    files = {"file": (file_name, file)}

    try:
        response = httpx.post(
            url, headers=headers, params=params, files=files, auth=auth, timeout=60
        )
        if response.status_code != 201:
            raise RVAError(f"{response.status_code} - {response.text}")
    finally:
        if isinstance(file_bytes_str, Path):
            file.close()

    data = response.json()

    # integerValue: the upload ID of the upload
    # stringValue: the filename of the upload, after passing through a "sanitization" process
    return (data["integerValue"], data["stringValue"])


def publish_new_vocabulary_version(
    vocabulary_id: str | int,
    upload_id: str | int,
    title: str,
    release_date: str,
    auth: Tuple[str, str],
    dev: bool = False,
):
    """Publish a new vocabulary version"""
    metadata = get_vocabulary_edit(vocabulary_id, auth, dev=dev)
    versions: list | None = metadata.get("version")

    if versions:
        for version in versions:
            # Change current version's status to superseded
            status = version.get("status")
            if status == "current":
                version["status"] = "superseded"

    # Insert a new version with the status as current.
    new_version = {
        "browse-flag": [],
        "access-point": [
            {
                "ap-file": {"upload-id": int(upload_id)},
                "source": "user",
                "discriminator": "file",
            }
        ],
        "status": "current",
        "title": title,
        "release-date": release_date,
        "do-import": True,
        "do-publish": True,
    }

    versions.append(new_version)

    url = (DEV_URL if dev else PROD_URL) + f"resource/vocabularies/{vocabulary_id}"
    headers = {"accept": "application/json", "content-type": "application/json"}
    response = httpx.put(url, headers=headers, json=metadata, auth=auth, timeout=60)

    # Indeterminate status code - docs says 200 but received 201.
    if response.status_code != 201 and response.status_code != 200:
        raise RVAError(f"{response.status_code} - {response.text}")

    return response.json()
