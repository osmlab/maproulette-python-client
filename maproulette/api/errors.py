"""This module contains the set of MapRoulette's exceptions"""


class MapRouletteBaseException(Exception):
    """MapRoulette Base Exception"""
    def __init__(self, message, status, payload):
        self.message = message
        self.status = status
        self.payload = payload

    def __str__(self):
        e = {
                "status": self.status,
                "message": self.message,
                "payload": self.payload
            }
        return repr({k: v for (k, v) in e.items() if v is not None})


class NotFoundError(MapRouletteBaseException):
    """Resource cannot be found"""
    def __init__(self, message='Resource not found.', status=None, payload=None):
        super().__init__(message=message, status=status, payload=payload)


class ConnectionUnavailableError(MapRouletteBaseException):
    """A connection error occurred"""
    def __init__(self, message='A connection error occurred.', status=None, payload=None):
        super().__init__(message=message, status=status, payload=payload)


class UnauthorizedError(MapRouletteBaseException):
    """The user is not authorized to make this request"""
    def __init__(self, message='The user is not authorized to make this request.', status=None, payload=None):
        super().__init__(message=message, status=status, payload=payload)


class HttpError(MapRouletteBaseException):
    """An HTTP error occurred"""
    def __init__(self, message='An HTTP error occurred.', status=None, payload=None):
        super().__init__(message=message, status=status, payload=payload)


class InvalidJsonError(MapRouletteBaseException):
    """Errors produced from an invalid JSON object"""
    def __init__(self, message='Invalid JSON payload.', status=None, payload=None):
        super().__init__(message=message, status=status, payload=payload)
