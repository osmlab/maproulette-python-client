"""
This module contains the methods that the user will use directly to interact with the MapRoulette API
"""
import json
from maproulette.api.maproulette_server import MapRouletteServer
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
        response, status_code = self.server.get(
            endpoint=f"/project/{str(project_id)}"
        )
        return response, status_code

    def get_project_by_name(self, project_name):
        """
        Method to fetch a project by unique MapRoulette project name
        :param project_name: the unique project name
        :return: the response from the API
        """
        response, status_code = self.server.get(
            endpoint=f"/projectByName/{str(project_name)}"
        )
        return response, status_code

    def find_project(self, matcher="", parent=-1, limit=10, page=0, only_enabled="true"):
        """
        Method to search for projects based on a specific search criteria
        :param matcher: the search string used to match the project names. Default is empty string
        :param parent: the parent ID. This field is ignored for this request. Default is -1.
        :param limit: the limit to the number of results returned in the response. Default is 10
        :param page: used in conjunction with the limit parameter to page through X number of responses. Default is 0.
        :param only_enabled: flag to set if only wanting enabled projects returned. Default is True.
        :return: the response from the API in a list form
        """
        query_params = {
            "q": matcher,
            "parentId": str(parent),
            "limit": str(limit),
            "page": str(page),
            "onlyEnabled": only_enabled
        }
        response, status_code = self.server.get(
            endpoint="/projects/find",
            params=query_params
        )
        return response, status_code

    def get_project_children(self, project_id, limit=10, page=0):
        """
        Method to fetch a project's children in an expanded list. Unlike the GET request /project/{id}/challenges, this
        function will wrap the JSON array list inside of the parent project object, showing the full hierarchy. It will
        not include the children tasks of the challenges
        :param project_id: the id of the parent project
        :param limit: the limit to the number of results returned in the response. Default is 10
        :param page: used in conjunction with the limit parameter to page through X number of responses. Default is 0.
        :return: the response from the API
        """
        query_params = {
            "limit": str(limit),
            "page": str(page)
        }
        response, status_code = self.server.get(
            endpoint=f"/project/{project_id}/children",
            params=query_params
        )
        return response, status_code

    def get_project_challenges(self, project_id, limit=10, page=0):
        """
        Method to fetch a list of a project's challenges.
        :param project_id: the id of the parent project
        :param limit: the limit to the number of results returned in the response. Default is 10
        :param page: used in conjunction with the limit parameter to page through X number of responses. Default is 0.
        :return: the response from the API in list form
        """
        query_params = {
            "limit": str(limit),
            "page": str(page)
        }
        response, status_code = self.server.get(
            endpoint=f"/project/{project_id}/challenges",
            params=query_params
        )
        return response, status_code

    def create_project(self, data):
        """
        Method to create a new project
        :param data: the data to use to create the new project
        :return:
        """
        if self.is_model(data):
            data = ProjectModel.to_dict(data)
        response, status_code = self.server.post(
            endpoint="/project",
            body=data)
        return response, status_code

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
            return True
        except ValueError:
            return False

    @staticmethod
    def is_model(input_object):
        """
        Method to determine whether user input is a valid project/challenge/task model
        :param input_object: the user's input to check
        :return: True if instance of model
        """
        return bool(isinstance(input_object, (ProjectModel, ChallengeModel, TaskModel)))
