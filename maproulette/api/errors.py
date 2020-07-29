"""This module contains the set of MapRoulette's exceptions"""


class MapRouletteBaseException(Exception):
    """MapRoulette Base Exception"""
    def __init__(self, message, status, payload):
        self.message = message
        self.status = status
        self.payload = payload

    def __str__(self):
        error = {
                "status": self.status,
                "message": self.message,
                "payload": self.payload
            }
        return repr({k: v for (k, v) in error.items() if v is not None})


class NotFoundError(MapRouletteBaseException):
    """Resource cannot be found"""
    def __init__(self, message=None, status=None, payload=None):
        if message:
            self.message = message
        else:
            self.message = "Resource cannot be found."
        super().__init__(message=self.message, status=status, payload=payload)


class ConnectionUnavailableError(MapRouletteBaseException):
    """A connection error occurred"""
    def __init__(self, message=None, status=None, payload=None):
        if message:
            self.message = message
        else:
            self.message = "A connection error occurred."
        super().__init__(message=self.message, status=status, payload=payload)


class UnauthorizedError(MapRouletteBaseException):
    """The user is not authorized to make this request"""
    def __init__(self, message=None, status=None, payload=None):
        if message:
            self.message = message
        else:
            self.message = "The user is not authorized to make this request."
        super().__init__(message=self.message, status=status, payload=payload)


class HttpError(MapRouletteBaseException):
    """An HTTP error occurred"""
    def __init__(self, message=None, status=None, payload=None):
        if message:
            self.message = message
        else:
            self.message = "An HTTP error occurred."
        super().__init__(message=self.message, status=status, payload=payload)


class InvalidJsonError(MapRouletteBaseException):
    """Errors produced from an invalid JSON object"""
    def __init__(self, message=None, status=None, payload=None):
        if message:
            self.message = message
        else:
            self.message = "Invalid JSON payload."
        super().__init__(message=self.message, status=status, payload=payload)
