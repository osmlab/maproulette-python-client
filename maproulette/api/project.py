"""This module contains the methods that the user will use directly to interact with MapRoulette projects"""

import json
from maproulette.api.maproulette_server import MapRouletteServer
from maproulette.models.project import ProjectModel


class Project(MapRouletteServer):
    """Class to handle the project-related API requests"""

    def __init__(self, config):
        super().__init__(configuration=config)

    def get_project_by_id(self, project_id):
        """Method to fetch a project by unique MapRoulette project ID

        :param project_id: the unique project ID
        :returns: the API response from the GET request
        """
        response = self.get(
            endpoint=f"/project/{str(project_id)}"
        )
        return response

    def get_project_by_name(self, project_name):
        """Method to fetch a project by unique MapRoulette project name

        :param project_name: the unique project name
        :returns: the API response from the GET request
        """
        response = self.get(
            endpoint=f"/projectByName/{str(project_name)}"
        )
        return response

    def find_project(self, matcher="", limit=10, page=0, only_enabled="true"):
        """Method to search for projects based on a specific search criteria

        :param matcher: the search string used to match the project names. Default is empty string
        :param limit: the limit to the number of results returned in the response. Default is 10
        :param page: used in conjunction with the limit parameter to page through X number of responses. Default is 0.
        :param only_enabled: flag to set if only wanting enabled projects returned. Default is True.
        :returns: the API response from the GET request
        """
        query_params = {
            "search": matcher,
            "limit": str(limit),
            "page": str(page),
            "onlyEnabled": only_enabled
        }
        response = self.get(
            endpoint="/projects",
            params=query_params
        )
        return response

    def get_project_challenges(self, project_id, limit=10, page=0):
        """Method to fetch a list of a project's challenges.

        :param project_id: the id of the parent project
        :param limit: the limit to the number of results returned in the response. Default is 10
        :param page: used in conjunction with the limit parameter to page through X number of responses. Default is 0.
        :returns: the API response from the GET request
        """
        query_params = {
            "limit": str(limit),
            "page": str(page)
        }
        response = self.get(
            endpoint=f"/project/{project_id}/challenges",
            params=query_params
        )
        return response

    def create_project(self, data):
        """Method to create a new project

        :param data: the data to use to create the new project
        :returns: the API response to the POST request
        """
        if self.is_project_model(data):
            data = ProjectModel.to_dict(data)
        response = self.post(
            endpoint="/project",
            body=data)
        return response

    @staticmethod
    def is_project_model(input_object):
        """Method to determine whether user input is a valid project model

        :param input_object: the user's input to check
        :returns: True if instance of model
        """
        return bool(isinstance(input_object, ProjectModel))
