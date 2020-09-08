import maproulette
import unittest
from unittest.mock import patch


class TestUserAPI(unittest.TestCase):

    config = maproulette.Configuration(api_key="API_KEY")
    api = maproulette.User(config)
    url = config.api_url

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_find_user_by_username(self, mock_request, api_instance=api):
        test_username = 'my_username_123'
        api_instance.find_user_by_username(test_username)
        mock_request.assert_called_once_with(
            f'{self.url}/users/find/{test_username}',
            params={'limit': '10',
                    'page': '0'
                    }
        )

    @patch('maproulette.api.maproulette_server.requests.Session.post')
    def test_add_user_to_project(self, mock_request, api_instance=api):
        test_user_id = '12345'
        test_project_id = '6789'
        test_group = '2'
        api_instance.add_user_to_project(user_id=test_user_id,
                                                    project_id=test_project_id,
                                                    group_type=test_group,
                                                    is_osm_user_id='true')
        mock_request.assert_called_once_with(
            f'{self.url}/user/{test_user_id}/project/{test_project_id}/{test_group}',
            json=None,
            params={'isOSMUserId': 'true'}
        )

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_add_user_list_to_project(self, mock_request, api_instance=api):
        test_user_ids = [123, 456, 789]
        test_project_id = '6789'
        test_group = '2'
        api_instance.add_user_list_to_project(user_ids=test_user_ids,
                                                         project_id=test_project_id,
                                                         group_type=test_group,
                                                         is_osm_user_id='true')
        mock_request.assert_called_once_with(
            f'{self.url}/user/project/{test_project_id}/{test_group}',
            params={'isOSMUserId': 'true'},
            json=test_user_ids
        )
