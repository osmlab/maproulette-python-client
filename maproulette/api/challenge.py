"""This module contains the methods that the user will use directly to interact with MapRoulette challenges"""

import json
from maproulette.api.maproulette_server import MapRouletteServer
from maproulette.models.challenge import ChallengeModel


class Challenge(MapRouletteServer):
    """Class to handle the challenge-related API requests"""

    def __init__(self, config):
        super().__init__(configuration=config)

    def create_challenge(self, data):
        """Method to create a new challenge

        :param data: a JSON input containing challenge details
        :returns: the API response to the POST request
        """
        if self.is_challenge_model(data):
            data = ChallengeModel.to_dict(data)
        response = self.post(
            endpoint="/challenge",
            body=data)
        return response

    def get_challenge_by_id(self, challenge_id):
        """Method to retrieve challenge information via the corresponding challenge ID

        :param challenge_id: the ID corresponding to the challenge
        :returns: the API response from the GET request
        """
        response = self.get(endpoint=f"/challenge/{challenge_id}")
        return response

    def get_challenge_statistics_by_id(self, challenge_id):
        """Method to retrieve statistics for a challenge using its corresponding ID

        :param challenge_id: the ID corresponding to the challenge
        :returns: the API response to the GET request
        """
        response = self.get(endpoint=f"/data/challenge/{challenge_id}")
        return response

    def get_challenge_tasks(self, challenge_id, limit=10, page=0):
        """Method to retrieve all tasks from a given challenge by ID

        :param challenge_id: the ID corresponding to the challenge
        :param limit: the limit to the number of results returned in the response. Default is 10
        :param page: used in conjunction with the limit parameter to page through X number of responses. Default is 0.
        :returns: the API response from the GET request
        """
        query_params = {
            "limit": str(limit),
            "page": str(page)
        }
        response = self.get(
            endpoint=f"/challenge/{challenge_id}/tasks",
            params=query_params
        )
        return response

    def add_tasks_to_challenge(self, data, challenge_id):
        """Method to add tasks to an existing challenge

        :param data: a geojson containing geometry of tasks to be added to a challenge
        :param challenge_id: the ID corresponding to the challenge that tasks will be added to
        :returns: the API response from the PUT request
        """
        response = self.put(
            endpoint=f"/challenge/{challenge_id}/addTasks",
            body=data)
        return response

    @staticmethod
    def is_challenge_model(input_object):
        """Method to determine whether user input is a valid challenge model

        :param input_object: the user's input to check
        :returns: True if instance of model
        """
        return bool(isinstance(input_object, ChallengeModel))
