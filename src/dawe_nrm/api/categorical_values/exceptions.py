class NoDataInAPIException(Exception):
    """This is raised when no data is received from the API."""


class UnexpectedDataShapeException(Exception):
    """This is raised when the shape of the data (JSON) is not the expected shape."""
