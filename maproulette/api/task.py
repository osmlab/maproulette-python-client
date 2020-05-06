"""This module contains the methods that the user will use directly to interact with MapRoulette tasks"""

import json
from maproulette.api.maproulette_server import MapRouletteServer
from maproulette.models.task import TaskModel


class Task(MapRouletteServer):
    """Class to handle the task-related API requests"""

    def __init__(self, config):
        super().__init__(configuration=config)

    def get_task_by_id(self, task_id):
        """"Method to retrieve task information using the corresponding task ID

        :param task_id: the  ID  corresponding with the task
        :returns: the  API response from the GET request
        """
        response = self.get(
            endpoint=f"/task/{task_id}")
        return response

    @staticmethod
    def is_task_model(input_object):
        """Method to determine whether user input is a valid task model

        :param input_object: the user's input to check
        :returns: True if instance of model
        """
        return bool(isinstance(input_object, TaskModel))
