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
        response = self.server.get(
            endpoint=f"/project/{str(project_id)}"
        )
        return response

    def get_project_by_name(self, project_name):
        """
        Method to fetch a project by unique MapRoulette project name
        :param project_name: the unique project name
        :return: the response from the API
        """
        response = self.server.get(
            endpoint=f"/projectByName/{str(project_name)}"
        )
        return response

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
        response = self.server.get(
            endpoint="/projects/find",
            params=query_params
        )
        return response

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
        response = self.server.get(
            endpoint=f"/project/{project_id}/children",
            params=query_params
        )
        return response

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
        response = self.server.get(
            endpoint=f"/project/{project_id}/challenges",
            params=query_params
        )
        return response

    def create_project(self, data):
        """
        Method to create a new project
        :param data: the data to use to create the new project
        :return:
        """
        if self.is_model(data):
            data = ProjectModel.to_dict(data)
        response = self.server.post(
            endpoint="/project",
            body=data)
        return response

    def get_challenge_by_id(self, challenge_id):
        """
        Method to retrieve challenge information via the corresponding challenge ID
        :param challenge_id: the ID corresponding to the challenge
        :return: the API response from the GET request
        """
        response = self.server.get(endpoint=f"/challenge/{challenge_id}")
        return response


    def get_challenge_tasks(self, challenge_id, limit=10, page=0):
        """
        Method to retrieve all tasks from a given challenge by ID
        :param challenge_id: the ID corresponding to the challenge
        :return: the API response from the GET request
        """
        query_params = {
            "limit": str(limit),
            "page": str(page)
        }
        response = self.server.get(
            endpoint=f"/challenge/{challenge_id}/tasks",
            params=query_params
        )
        return response

    def add_tasks_to_challenge(self, data, challenge_id):
        """
        Method to add tasks to an existing challenge
        :param data: a geojson containing geometry of tasks to be added to a challenge
        :param challenge_id: the ID corresponding to the challenge that tasks will be added to
        :return: the API response from the PUT request
        """
        if self.is_model(data):
            data = TaskModel.to_dict(data)
        response = self.server.put(
            endpoint=f"/challenge/{challenge_id}/addTasks",
            body=data)
        return response

    def get_task_by_id(self, task_id):
        """"
        Method to retrieve task information using the corresponding task ID
        :param task_id: the  ID  corresponding with the task
        :return: the  API response from the GET request
        """
        response = self.server.get(
            endpoint=f"/task/{task_id}")
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
