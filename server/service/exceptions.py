"""Service package exceptions."""


class ServiceUnavailable(Exception):
    """Exception for overall service availability."""


class ServiceNotFound(Exception):
    """Service unable to find anything."""
