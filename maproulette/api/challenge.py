"""This module contains the methods that the user will use directly to interact with MapRoulette challenges"""

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

    def create_virtual_challenge(self, data):
        """Method to create a new virtual challenge

        :param data: a JSON input containing virtual challenge details
        :returns: the API response to the POST request
        """
        # TODO: add model for virtual challenge to aid in posting
        response = self.post(
            endpoint="/virtualchallenge",
            body=data)
        return response

    def get_challenge_by_id(self, challenge_id):
        """Method to retrieve challenge information via the corresponding challenge ID

        :param challenge_id: the ID corresponding to the challenge
        :returns: the API response from the GET request
        """
        response = self.get(endpoint=f"/challenge/{challenge_id}")
        return response

    def get_challenge_by_name(self, project_id, challenge_name):
        """Method to retrieve challenge information via the corresponding challenge name and parent (project) ID

        :param project_id: the ID of the parent project
        :param challenge_name: the name corresponding to the challenge
        :returns: the API response from the GET request
        """
        response = self.get(endpoint=f"/project/{project_id}/challenge/{challenge_name}")
        return response

    def get_virtual_challenge_by_id(self, challenge_id):
        """Method to retrieve an existing virtual challenge

        :param challenge_id: the ID corresponding to the virtual challenge
        :returns: the API response from the GET request
        """
        response = self.get(endpoint=f"/virtualchallenge/{challenge_id}")
        return response

    def get_challenge_statistics_by_id(self, challenge_id):
        """Method to retrieve statistics for a challenge using its corresponding ID

        :param challenge_id: the ID corresponding to the challenge
        :returns: the API response to the GET request
        """
        response = self.get(endpoint=f"/data/challenge/{challenge_id}")
        return response

    def get_challenge_listing(self, project_ids="", limit=10, page=0, only_enabled='true'):
        """Method to retrieve a lightweight list of challenges that belong to the specified project(s)

        :param project_ids: a comma-separated list of project IDs for which child challenges are desired. Default is an
            empty string (i.e. all projects)
        :param limit: the limit to the number of results returned in the response. Default is 10
        :param page: used in conjunction with the limit parameter to page through X number of responses. Default is 0.
        :param only_enabled: whether or not results should be limited to only enabled challenges. Default is true.
        :returns: the API response from the GET request
        """
        query_params = {
            "projectIds": str(project_ids),
            "limit": str(limit),
            "page": str(page),
            "onlyEnabled": str(only_enabled)
        }
        response = self.get(
            endpoint="/challenges/listing",
            params=query_params
        )
        return response

    def get_challenge_children(self, challenge_id, limit=10, page=0):
        """Method to retrieve all children from a given challenge in an expanded list. Unlike the
        :meth:`~maproulette.api.challenge.Challenge.get_challenge_tasks` method, this function will wrap the JSON
        array list inside of the parent challenge object allowing you to see the full hierarchy.

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
            endpoint=f"/challenge/{challenge_id}/children",
            params=query_params
        )
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

    def get_challenge_comments(self, challenge_id, limit=10, page=0):
        """Method to retrieve all comments for the tasks in a given challenge

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
            endpoint=f"/challenge/{challenge_id}/comments",
            params=query_params
        )
        return response

    def extract_challenge_comments(self, challenge_id, limit=10, page=0):
        """Method to retrieve all comments for the tasks in a given challenge and respond with a CSV

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
            endpoint=f"/challenge/{challenge_id}/comments/extract",
            params=query_params
        )
        return response

    def extract_task_summaries(self, challenge_id, limit=10, page=0, status="", review_status="", priority="",
                               export_properties="", task_property_search=""):
        """Method to retrieve summaries of all the tasks in a given challenge and respond with a CSV

        :param challenge_id: the ID corresponding to the challenge
        :param limit: the limit to the number of results returned in the response. Default is 10
        :param page: used in conjunction with the limit parameter to page through X number of responses. Default is 0.
        :param status: a comma-separated filter for the tasks returned using tasks status values:
            0 = Created, 1 = Fixed, 2 = False Positive, 3 = Skipped, 4 = Deleted, 5 = Already Fixed, 6 = Too Hard
        :param review_status: a comma-separated filter for the tasks returned using review status values:
            0 - Requested, 1 - Approved, 2 - Rejected, 3 - Assisted, 4 - Disputed
        :param priority: a comma-separated filter for the tasks returned by priority value:
            0 - High, 1 - Medium, 2 - Low
        :param export_properties: a comma-separated filter for the properties that should be exported
        :param task_property_search: a filter for the tasks returned using task properties
        :returns: the API response from the GET request
        """
        query_params = {
            "limit": str(limit),
            "page": str(page),
            "status": str(status),
            "reviewStatus": str(review_status),
            "priority": str(priority),
            "exportProperties": str(export_properties),
            "taskPropertySearch": str(task_property_search)
        }
        response = self.get(
            endpoint=f"/challenge/{challenge_id}/tasks/extract",
            params=query_params
        )
        return response

    def get_challenge_geojson(self, challenge_id, status="", review_status="", priority="", task_property_search=""):
        """Method to retrieve the GeoJSON for a challenge that represents all the task children of the challenge

        :param challenge_id: the ID corresponding to the challenge
        :param status: a comma-separated filter for the tasks returned using tasks status values:
            0 = Created, 1 = Fixed, 2 = False Positive, 3 = Skipped, 4 = Deleted, 5 = Already Fixed, 6 = Too Hard
        :param review_status: a comma-separated filter for the tasks returned using review status values:
            0 - Requested, 1 - Approved, 2 - Rejected, 3 - Assisted, 4 - Disputed
        :param priority: a comma-separated filter for the tasks returned by priority value:
            0 - High, 1 - Medium, 2 - Low
        :param task_property_search: a filter for the tasks returned using task properties
        :returns: the API response from the GET request
        """
        query_params = {
            "status": str(status),
            "reviewStatus": str(review_status),
            "priority": str(priority),
            "taskPropertySearch": str(task_property_search)
        }
        response = self.get(
            endpoint=f"/challenge/view/{challenge_id}",
            params=query_params
        )
        return response

    def update_task_priorities(self, challenge_id):
        """Method to update all the task priorities for a given challenge based on the priority rules in the challenge

        :param challenge_id: the ID corresponding to the challenge
        :returns: the API response from the PUT request
        """
        response = self.put(
            endpoint=f"/challenge/{challenge_id}/updateTaskPriorities"
        )
        return response

    def reset_task_instructions(self, challenge_id):
        """Method to reset all the task instructions so that they revert to the challenge instructions

        :param challenge_id: the ID corresponding to the challenge
        :returns: the API response from the PUT request
        """
        response = self.put(
            endpoint=f"/challenge/{challenge_id}/resetTaskInstructions"
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

    def delete_challenge(self, challenge_id, immediate="false"):
        """Method to delete a challenge by using the corresponding challenge ID

        :param challenge_id: the ID corresponding to the challenge
        :param immediate: whether or not the challenge should be deleted immediately
        :returns: the API response from the DELETE request
        """
        query_params = {
            "immediate": str(immediate)
        }
        response = self.delete(
            endpoint=f"/challenge/{challenge_id}",
            params=query_params
        )
        return response

    def delete_challenge_tasks(self, challenge_id, status_filters=""):
        """Method to delete all existing tasks within a challenge, optionally filtering on current task status

        :param challenge_id: the ID corresponding to the challenge
        :param status_filters: a comma separate list of status ID's:
            0 = Created, 1 = Fixed, 2 = False Positive, 3 = Skipped, 4 = Deleted, 5 = Already Fixed, 6 = Too Hard
        :returns: the API response from the DELETE request
        """
        query_params = {
            "statusFilters": str(status_filters)
        }
        response = self.delete(
            endpoint=f"/challenge/{challenge_id}/tasks",
            params=query_params
        )
        return response

    def update_challenge(self, challenge_id, data):
        """Method to update a challenge by using the corresponding challenge ID

        :param challenge_id: the ID corresponding to the challenge
        :param data: a JSON input containing challenge details
        :returns: the API response from the PUT request
        """
        if self.is_challenge_model(data):
            data = ChallengeModel.to_dict(data)
        response = self.put(
            endpoint=f"/challenge{challenge_id}",
            body=data)
        return response

    @staticmethod
    def is_challenge_model(input_object):
        """Method to determine whether user input is a valid challenge model

        :param input_object: the user's input to check
        :returns: True if instance of model
        """
        return bool(isinstance(input_object, ChallengeModel))
