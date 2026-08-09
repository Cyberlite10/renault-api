"""Exceptions raised by the Mitsubishi API client."""


class MitsubishiApiError(Exception):
    """Base error returned by the Mitsubishi connected-car API."""


class MitsubishiAuthenticationError(MitsubishiApiError):
    """The access token was rejected or has expired."""
