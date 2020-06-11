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

    def get_task_history(self, task_id):
        """Method to retrieve task history using the corresponding task ID

        :param task_id: the ID corresponding with the task
        :return: the API response from the GET request
        """
        response = self.get(
            endpoint=f"/task/{task_id}/history")
        return response

    def create_tasks(self, data):
        """Method to create a batch of tasks

        :param data: a JSON input containing task details
        :return: the API response from the POST request
        """
        response = self.post(
            endpoint="/tasks",
            body=data)
        return response

    def update_tasks(self, data):
        """Method to update a batch of tasks

        :param data: a JSON input containing task details
        :return: the API response from the PUT request
        """
        response = self.put(
            endpoint="/tasks",
            body=data)
        return response

    def get_task_tags(self, task_id):
        """Method to retrieve the tags for a task using the corresponding task ID

        :param task_id: the ID corresponding with the task
        :return: the API response from the GET request
        """
        response = self.get(
            endpoint=f"/task/{task_id}/tags")
        return response

    def delete_task_tags(self, task_id, tags):
        """Method to delete the supplied tags from a task using the corresponding task ID

        :param task_id: the ID corresponding with the task
        :param tags: a comma-separated list of tags to be deleted
        :return: the API response from the DELETE request
        """
        query_params = {
            "tags": str(tags)
        }
        response = self.delete(
            endpoint=f"/task/{task_id}/tags",
            params=query_params
        )
        return response

    def get_tasks_by_tags(self, tags, limit=10, page=0):
        """Method to retrieve tasks that have the specified tags

        :param tags: a comma-separated list of tags to be searched for
        :param limit: the limit to the number of results returned in the response. Default is 10
        :param page: used in conjunction with the limit parameter to page through X number of responses. Default is 0.
        :return: the API response from the GET request
        """
        query_params = {
            "tags": str(tags),
            "limit": str(limit),
            "page": str(page)
        }
        response = self.get(
            endpoint="/tasks/tags",
            params=query_params
        )
        return response

    def update_task_tags(self, task_id, tags):
        """Method to update a task's tags using the supplied tags and corresponding task ID

        :param task_id: the ID corresponding with the task
        :param tags: a comma-separated list of tags to be updated. If empty all tags will be removed.
        :return: the API response from the GET request
        """
        query_params = {
            "tags": str(tags)
        }
        response = self.get(
            endpoint=f"/task/{task_id}/tags/update",
            params=query_params
        )
        return response

    

    @staticmethod
    def is_task_model(input_object):
        """Method to determine whether user input is a valid task model

        :param input_object: the user's input to check
        :returns: True if instance of model
        """
        return bool(isinstance(input_object, TaskModel))
