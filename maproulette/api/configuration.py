"""
This module contains the basic configuration object that is used to communicate with the MapRoulette API
"""

DEFAULT_URL = 'https://maproulette.org'
DEFAULT_PROTOCOL = 'https'


class Configuration:
    """
    Class for storing the configuration of the MapRoulette server
    """
    def __init__(self, url=DEFAULT_URL, protocol=DEFAULT_PROTOCOL, api_key=None):
        self.url = url
        self.headers = dict()
        self.headers['apikey'] = api_key
        self.protocol = protocol
