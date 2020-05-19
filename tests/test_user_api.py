import maproulette
import unittest
from unittest.mock import patch


class TestUserAPI(unittest.TestCase):

    config = maproulette.Configuration(api_key="API_KEY")
    api = maproulette.User(config)

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_find_user_by_username(self, mock_request, api_instance=api):
        test_username = 'my_username_123'
        mock_request.return_value.status_code = '200'
        response = api_instance.find_user_by_username(test_username)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.post')
    def test_add_user_to_project_group(self, mock_request, api_instance=api):
        test_user_id = '12345'
        test_project_id = '6789'
        test_group = '2'
        mock_request.return_value.status_code = '200'
        response = api_instance.add_user_to_project_group(user_id=test_user_id,
                                                          project_id=test_project_id,
                                                          group_type=test_group,
                                                          is_osm_user_id='true')
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_add_list_of_users_to_project_group(self, mock_request, api_instance=api):
        test_user_ids = [123, 456, 789]
        test_project_id = '6789'
        test_group = '2'
        mock_request.return_value.status_code = '200'
        response = api_instance.add_list_of_users_to_project_group(user_ids=test_user_ids,
                                                                   project_id=test_project_id,
                                                                   group_type=test_group,
                                                                   is_osm_user_id='true')
        self.assertEqual(response['status'], '200')
