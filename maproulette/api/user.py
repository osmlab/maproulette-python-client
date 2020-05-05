"""This module contains the methods that the user will use directly to interact with MapRoulette users"""

import json
from maproulette.api.maproulette_server import MapRouletteServer


class User(MapRouletteServer):
    """Class to handle the user-related API requests"""

    def __init__(self, config):
        super().__init__(configuration=config)
