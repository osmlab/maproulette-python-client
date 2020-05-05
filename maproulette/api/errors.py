"""This module contains the set of MapRoulette's exceptions"""


class MapRouletteBaseException(Exception):
    """MapRoulette Base Exception"""
    def __init__(self, message, status=None, payload=None):
        self.message = message
        self.status = status
        self.payload = payload

    def __str__(self):
        return repr({
                "status": self.status,
                "message": self.message,
                "payload": self.payload
                })


class NotFoundError(MapRouletteBaseException):
    """Resource cannot be found"""


class ConnectionUnavailableError(MapRouletteBaseException):
    """A connection error occurred"""


class UnauthorizedError(MapRouletteBaseException):
    """The user is not authorized to make this request"""


class HttpError(MapRouletteBaseException):
    """An HTTP error occurred"""


class InvalidJsonError(MapRouletteBaseException):
    """Errors produced from an invalid JSON object"""
