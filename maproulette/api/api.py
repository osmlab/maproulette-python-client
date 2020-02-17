"""
This module contains the methods that the user will use directly to interact with the MapRoulette API
"""
import json
from maproulette.api.maproulette_server import MapRouletteServer
from maproulette.api import query_constants
from maproulette.models.project import ProjectModel
from maproulette.models.challenge import ChallengeModel
from maproulette.models.task import TaskModel


class Api:
    """Class to handle the API requests"""

    def __init__(self, config):
        self.server = MapRouletteServer(config)

    def get_project_by_id(self, project_id):
        """
        Method to fetch a project by unique MapRoulette project ID
        :param project_id: the unique project ID
        :return: the response from the API
        """
        response = self.server.get(
            endpoint=query_constants.URI_PROJECT_BASE % project_id
        )
        return response

    def get_project_by_name(self, project_name):
        """
        Method to fetch a project by unique MapRoulette project name
        :param project_name: the unique project name
        :return: the response from the API
        """
        response = self.server.get(
            endpoint=query_constants.URI_PROJECT_GET_BY_NAME % project_name
        )
        return response

    def find_project(self, matcher="", parent="-1", limit="10", page="0", only_enabled="true"):
        """
        Method to search for projects based on a specific search criteria
        :param matcher: the search string used to match the project names. Default is empty string
        :param parent: the parent ID. This field is ignored for this request. Default is -1.
        :param limit: the limit to the number of results returned in the response. Default is 10
        :param page: used in conjunction with the limit parameter to page through X number of responses. Default is 0.
        :param only_enabled: flag to set if only wanting enabled projects returned. Default is True.
        :return: the response from the API in a list form
        """
        response = self.server.get(
            endpoint=query_constants.URI_PROJECT_FIND +
            query_constants.QUERY_PARAMETER_Q + matcher + "&" +
            query_constants.QUERY_PARAMETER_PARENT_IDENTIFIER + str(parent) + "&" +
            query_constants.QUERY_PARAMETER_LIMIT + str(limit) + "&" +
            query_constants.QUERY_PARAMETER_PAGE + str(page) + "&" +
            query_constants.QUERY_PARAMETER_ONLY_ENABLED + only_enabled
        )
        return response

    def get_project_children(self, project_id, limit="10", page="0"):
        """
        Method to fetch a project's children in an expanded list. Unlike the GET request /project/{id}/challenges, this
        function will wrap the JSON array list inside of the parent project object, showing the full hierarchy. It will
        not include the children tasks of the challenges
        :param project_id: the id of the parent project
        :param limit: the limit to the number of results returned in the response. Default is 10
        :param page: used in conjunction with the limit parameter to page through X number of responses. Default is 0.
        :return: the response from the API
        """
        response = self.server.get(
            endpoint=query_constants.URI_PROJECT_CHILDREN % project_id + "?" +
            query_constants.QUERY_PARAMETER_LIMIT + str(limit) + "&" +
            query_constants.QUERY_PARAMETER_PAGE + str(page)
        )
        return response

    def get_project_challenges(self, project_id, limit="10", page="0"):
        """
        Method to fetch a list of a project's challenges.
        :param project_id: the id of the parent project
        :param limit: the limit to the number of results returned in the response. Default is 10
        :param page: used in conjunction with the limit parameter to page through X number of responses. Default is 0.
        :return: the response from the API in list form
        """
        response = self.server.get(
            endpoint=query_constants.URI_CHALLENGES % project_id + "?" +
            query_constants.QUERY_PARAMETER_LIMIT + str(limit) + "&" +
            query_constants.QUERY_PARAMETER_PAGE + str(page)
        )
        return response

    def create_project(self, data):
        """
        Method to create a new project
        :param data: the data to use to create the new project
        :return:
        """
        if self.is_model(data):
            data = ProjectModel.to_json(data)
        elif self.is_json(data):
            pass
        response = self.server.post(
            endpoint=query_constants.URI_PROJECT_POST,
            body=data)
        return response

    @staticmethod
    def is_json(input_object):
        """
        Method to determine whether user input is valid JSON.
        :param input_object: the user's input to check
        :return: True if valid json object
        """
        try:
            json_object = json.loads(input_object)
            del json_object
        except ValueError:
            pass
        return True

    @staticmethod
    def is_model(input_object):
        """
        Method to determine whether user input is a valid project/challenge/task model
        :param input_object: the user's input to check
        :return: True if instance of model
        """
        return bool(isinstance(input_object, (ProjectModel, ChallengeModel, TaskModel)))
