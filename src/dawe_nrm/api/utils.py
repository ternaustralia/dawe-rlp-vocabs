import uuid


def get_local_uuid_name(id):
    """Use an id to seed the generation of a uuid5."""
    return str(uuid.uuid5(uuid.NAMESPACE_URL, id))
