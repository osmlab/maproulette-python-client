"""
A Python wrapper for the MapRoulette API
"""

from .api.maproulette_server import MapRouletteServer
from .api.configuration import Configuration
from .models.project import ProjectModel
from .models.challenge import ChallengeModel
from .models.task import TaskModel
from .models.priority_rule import PriorityRule, PriorityRuleModel
from .models import priority_rule
from .api.project import Project
from .api.challenge import Challenge
from .api.task import Task
from .api.user import User

__version__ = '1.2.1'
