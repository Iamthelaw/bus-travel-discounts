"""Custom exceptions."""


class ParserError(Exception):
    """Base class for any parser related errors."""


class RequestError(ParserError):
    """Something wrong with request."""
