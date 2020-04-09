"""This module contains the set of MapRoulette's exceptions"""


class MapRouletteBaseException(Exception):
    """MapRoulette Base Exception"""


class ConnectionUnavailableError(MapRouletteBaseException):
    """A connection error occurred"""


class HttpError(MapRouletteBaseException):
    """An HTTP error occurred"""


class IllegalArgumentError(MapRouletteBaseException):
    """Errors produced by passing illegal arguments"""


class InvalidJsonError(MapRouletteBaseException):
    """Errors produced from an invalid JSON object"""
