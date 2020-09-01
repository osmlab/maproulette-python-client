import maproulette
import unittest
from tests.sample_data import test_geojson, test_overpassQL_query
from unittest.mock import patch


class TestChallengeAPI(unittest.TestCase):

    config = maproulette.Configuration(api_key="API_KEY")
    api = maproulette.Challenge(config)
    url = config.api_url

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_by_id(self, mock_request, api_instance=api):
        test_challenge_id = '12974'
        api_instance.get_challenge_by_id(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}/challenge/12974',
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_statistics_by_id(self, mock_request, api_instance=api):
        test_challenge_id = '12974'
        api_instance.get_challenge_statistics_by_id(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}/data/challenge/{test_challenge_id}',
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_tasks(self, mock_request, api_instance=api):
        test_challenge_id = '12974'
        api_instance.get_challenge_tasks(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}/challenge/{test_challenge_id}/tasks',
            params={'limit': '10',
                    'page': '0'})

    @patch('maproulette.api.maproulette_server.requests.Session.post')
    def test_create_challenge(self, mock_request, api_instance=api):
        test_challenge_model = maproulette.ChallengeModel(name='Test_Challenge_Name',
                                                          instruction='Do something',
                                                          description='This is a test challenge',
                                                          overpassQL=test_overpassQL_query)
        api_instance.create_challenge(test_challenge_model)
        mock_request.assert_called_once_with(
            f'{self.url}/challenge',
            json={'name': 'Test_Challenge_Name', 'description': 'This is a test challenge',
                  'instruction': 'Do something',
                  'overpassQL': 'way["name"="Københavns Lufthavn"];\nout body geom qt;'},
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_add_tasks_to_challenge(self, mock_request, api_instance=api):
        test_challenge_id = '12978'
        api_instance.add_tasks_to_challenge(test_geojson, test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}'
        )

    @patch('maproulette.api.maproulette_server.requests.Session.post')
    def test_create_virtual_challenge(self, mock_request, api_instance=api):
        # TODO: add model for virtual challenge to aid in posting
        test_challenge_model = maproulette.ChallengeModel(name='Test_Challenge_Name',
                                                          instruction='Do something',
                                                          description='This is a test challenge',
                                                          overpassQL=test_overpassQL_query)
        api_instance.create_virtual_challenge(test_challenge_model)
        mock_request.assert_called_once_with(
            f'{self.url}'
        )

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_by_name(self, mock_request, api_instance=api):
        test_project_id = '12345'
        test_challenge_name = 'Test_Challenge_Name'
        api_instance.get_challenge_by_name(test_project_id, test_challenge_name)
        mock_request.assert_called_once_with(
            f'{self.url}'
        )

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_virtual_challenge_by_id(self, mock_request, api_instance=api):
        test_virtual_challenge_id = '12345'
        api_instance.get_virtual_challenge_by_id(test_virtual_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}'
        )

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_listing(self, mock_request, api_instance=api):
        test_project_ids = '12345,67891,23456'
        api_instance.get_challenge_listing(test_project_ids)
        mock_request.assert_called_once_with(
            f'{self.url}'
        )

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_children(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.get_challenge_children(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}'
        )

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_comments(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.get_challenge_comments(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}'
        )

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_extract_challenge_comments(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.extract_challenge_comments(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}'
        )

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_extract_task_summaries(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.extract_task_summaries(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}'
        )

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_geojson(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.get_challenge_geojson(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}'
        )

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_update_task_priorities(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.update_task_priorities(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}'
        )

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_reset_task_instructions(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.reset_task_instructions(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}'
        )

    @patch('maproulette.api.maproulette_server.requests.Session.delete')
    def test_delete_challenge(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.delete_challenge(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}'
        )

    @patch('maproulette.api.maproulette_server.requests.Session.delete')
    def test_delete_challenge_tasks(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.delete_challenge_tasks(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}'
        )

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_update_challenge(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        test_challenge_model = maproulette.ChallengeModel(name='Test_Challenge_Name',
                                                          instruction='Do something',
                                                          description='This is a test challenge',
                                                          overpassQL=test_overpassQL_query)
        api_instance.update_challenge(test_challenge_id, test_challenge_model)
        mock_request.assert_called_once_with(
            f'{self.url}'
        )
