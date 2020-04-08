"""
A Python wrapper for the MapRoulette API
"""

from .api.maproulette_server import MapRouletteServer
from .api.configuration import Configuration
from .api.api import Api
from .models.project import ProjectModel
from .models.challenge import ChallengeModel
from .models.task import TaskModel

__version__ = '1.0.0'
