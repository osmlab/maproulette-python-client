"""This module contains the basic configuration object that is used to communicate with the MapRoulette API."""

DEFAULT_HOSTNAME = 'maproulette.org'
DEFAULT_PROTOCOL = 'https'
DEFAULT_API_VERSION = '/api/v2'


class Configuration:
    """Class for storing the configuration of the MapRoulette server"""
    def __init__(self, hostname=DEFAULT_HOSTNAME, protocol=DEFAULT_PROTOCOL, api_version=DEFAULT_API_VERSION,
                 api_key=None, certs=None, verify=True):
        """Create a new configuration object to connect to the MapRoulette server.

        :param hostname: Optional parameter to specify the hostname of the MapRoulette instance being addressed. Do not
        include the protocol (https, http). Default value is 'maproulette.org'.
        :type hostname: str
        :param protocol: Optional parameter to specify the protocol to use for the connection to the MapRoulette
        instance being addressed such as https or http. Default value is 'https'.
        :type protocol: str
        :param api_version: Optional parameter to specify the API version to use. The default is '/api/v2'.
        :type api_version: str
        :param api_key: Optional parameter to pass the user-specific API key. This key is necessary for some actions.
        :type api_key: str
        :param certs: Optional parameter to pass the client-side certificate and key if necessary to make connection
        with the MapRoulette instance being addressed.
        :type certs: tuple
        :param verify: Optional parameter to specify whether to verify SSL certificates for HTTPS requests. Default is
        True.
        :type verify: bool
        """
        self.api_url = f"{protocol}://{hostname}{api_version}"
        self.base_url = f"{protocol}://{hostname}"
        self.protocol = protocol
        self.headers = dict()
        self.headers['apikey'] = api_key
        self.certs = certs
        self.verify = verify
