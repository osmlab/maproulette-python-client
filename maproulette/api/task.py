"""This module contains the methods that the user will use directly to interact with MapRoulette tasks"""

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
        :returns: the API response from the GET request
        """
        response = self.get(
            endpoint=f"/task/{task_id}/history")
        return response

    def create_tasks(self, data, batch_size=5000):
        """Method to create a batch of tasks using the specified batch_size.

        :param data: a JSON input containing task details
        :param batch_size: the number of tasks to post per API call. The default is 5000.
        :type batch_size: int
        :returns: the API response from the POST request
        """
        response = []
        for batch in self.batch_generator(input_list=data, chunk_size=batch_size):
            response.append(self.post(
                endpoint="/tasks",
                body=batch)
            )
        return response

    def update_tasks(self, data):
        """Method to update a batch of tasks

        :param data: a JSON input containing task details
        :returns: the API response from the PUT request
        """
        response = self.put(
            endpoint="/tasks",
            body=data)
        return response

    def get_task_tags(self, task_id):
        """Method to retrieve the tags for a task using the corresponding task ID

        :param task_id: the ID corresponding with the task
        :returns: the API response from the GET request
        """
        response = self.get(
            endpoint=f"/task/{task_id}/tags")
        return response

    def delete_task_tags(self, task_id, tags):
        """Method to delete the supplied tags from a task using the corresponding task ID

        :param task_id: the ID corresponding with the task
        :param tags: a comma-separated list of tags to be deleted
        :returns: the API response from the DELETE request
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
        :returns: the API response from the GET request
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
        :returns: the API response from the GET request
        """
        query_params = {
            "tags": str(tags)
        }
        response = self.get(
            endpoint=f"/task/{task_id}/tags/update",
            params=query_params
        )
        return response

    def update_task_status(self, task_id, status, comment=None, tags=None, request_review=None,
                           completion_responses=None):
        """Method to update a task's status to one of the following:
        0 - Created, 1 - Fixed, 2 - False Positive, 3 - Skipped, 4 - Deleted, 5 - Already Fixed, 6 - Too Hard.

        :param task_id: the ID corresponding with the task
        :param status: the status to update the task to
        :param comment: optional comment that is provided by the user when setting the status
        :param tags: optional tags to associate with this task
        :param request_review: optional boolean indicating if a review is requested on this task
        :param completion_responses: optional key/value JSON to be stored within this task
        :returns: the API response from the PUT request
        """
        query_params = {
            "comment": str(comment),
            "tags": str(tags),
            "requestReview": str(request_review)
        }
        response = self.put(
            endpoint=f"/task/{task_id}/{status}",
            params=query_params,
            body=completion_responses
        )
        return response

    def get_task_comments(self, task_id):
        """Method to retrieve the comments for a task using the corresponding task ID

        :param task_id: the ID corresponding with the task
        :returns: the API response from the GET request
        """
        response = self.get(
            endpoint=f"/task/{task_id}/comments"
        )
        return response

    @staticmethod
    def is_task_model(input_object):
        """Method to determine whether user input is a valid task model

        :param input_object: the user's input to check
        :returns: True if instance of model
        """
        return bool(isinstance(input_object, TaskModel))

    @staticmethod
    def batch_generator(input_list, chunk_size):
        """Method to yield successive n-sized chunks from input_list

        :param input_list: the list to break into chunks
        :param chunk_size: the number of list items to include per chunk
        :type chunk_size: int
        :returns: an iterator for the n-sized chunks of the input_list
        """
        for i in range(0, len(input_list), chunk_size):
            yield input_list[i:i + chunk_size]
