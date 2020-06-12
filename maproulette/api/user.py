"""This module contains the methods that the user will use directly to interact with MapRoulette users"""

from maproulette.api.maproulette_server import MapRouletteServer


class User(MapRouletteServer):
    """Class to handle the user-related API requests"""

    def __init__(self, config):
        super().__init__(configuration=config)

    def find_user_by_username(self, username, limit=10, page=0):
        """Method to search for a user based on a specific username

        :param username: the username to search for.
        :param limit: the limit to the number of results returned in the response. Default is 10
        :param page: used in conjunction with the limit parameter to page through X number of responses. Default is 0.
        :returns: the API response from the GET request
        """
        query_params = {
            "limit": str(limit),
            "page": str(page)
        }
        response = self.get(
            endpoint=f"/users/find/{username}",
            params=query_params
        )
        return response

    def add_user_to_project(self, user_id, project_id, group_type, is_osm_user_id='true'):
        """Method to add a user to a project group

        :param user_id: the user ID to add to the specified project group
        :param project_id: the ID of the project
        :param group_type: the group type to add the user to (1 - Admin, 2 - Write, 3 - Read)
        :param is_osm_user_id: whether or not the specified user ID is an OSM user ID. Default is 'false'.
        :returns: the API response from the POST request
        """
        query_params = {
            "isOSMUserId": str(is_osm_user_id)
        }
        response = self.post(
            endpoint=f"/user/{user_id}/project/{project_id}/{group_type}",
            params=query_params
        )
        return response

    def add_user_list_to_project(self, user_ids, project_id, group_type, is_osm_user_id='true'):
        """Method to add a user to a project group

        :param user_ids: a list of user IDs to add to the specified project group. IDs should be integers.
        :param project_id: the ID of the project
        :param group_type: the group type to add the user to (1 - Admin, 2 - Write, 3 - Read)
        :param is_osm_user_id: whether or not the specified user ID is an OSM user ID. Default is 'false'.
        :returns: the API response from the PUT request
        """
        query_params = {
            "isOSMUserId": str(is_osm_user_id)
        }
        response = self.put(
            endpoint=f"/user/project/{project_id}/{group_type}",
            params=query_params,
            body=user_ids
        )
        return response
