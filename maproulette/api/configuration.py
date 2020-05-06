"""This module contains the basic configuration object that is used to communicate with the MapRoulette API."""

DEFAULT_URL = 'maproulette.org'
DEFAULT_PROTOCOL = 'https'
DEFAULT_API_VERSION = '/api/v2'


class Configuration:
    """Class for storing the configuration of the MapRoulette server"""
    def __init__(self, url=DEFAULT_URL, protocol=DEFAULT_PROTOCOL, api_version=DEFAULT_API_VERSION, api_key=None):
        self.url = f"{protocol}://{url}{api_version}"
        self.base_url = f"{protocol}://{url}"
        self.headers = dict()
        self.headers['apikey'] = api_key
        self.protocol = protocol
