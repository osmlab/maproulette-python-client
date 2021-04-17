import maproulette
import unittest
from tests.sample_data import test_geojson, test_overpassQL_query, create_challenge_output
from unittest.mock import patch
import json


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
            json=json.loads(create_challenge_output),
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_add_tasks_to_challenge(self, mock_request, api_instance=api):
        test_challenge_id = '12978'
        api_instance.add_tasks_to_challenge(test_geojson, test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}/challenge/12978/addTasks',
            json=test_geojson,
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.post')
    def test_create_virtual_challenge(self, mock_request, api_instance=api):
        # TODO: add model for virtual challenge to aid in posting
        test_challenge_model = maproulette.ChallengeModel(name='Test_Challenge_Name',
                                                          instruction='Do something',
                                                          description='This is a test challenge',
                                                          overpassQL=test_overpassQL_query)
        api_instance.create_virtual_challenge(test_challenge_model)
        mock_request.assert_called_once_with(
            f'{self.url}/virtualchallenge',
            json=test_challenge_model,
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_by_name(self, mock_request, api_instance=api):
        test_project_id = '12345'
        test_challenge_name = 'Test_Challenge_Name'
        api_instance.get_challenge_by_name(test_project_id, test_challenge_name)
        mock_request.assert_called_once_with(
            f'{self.url}/project/{test_project_id}/challenge/{test_challenge_name}',
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenges_by_tags(self, mock_request, api_instance=api):
        test_challenge_tag = 'River'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_challenges_by_tags(test_challenge_tag)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_virtual_challenge_by_id(self, mock_request, api_instance=api):
        test_virtual_challenge_id = '12345'
        api_instance.get_virtual_challenge_by_id(test_virtual_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}/virtualchallenge/{test_virtual_challenge_id}',
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_listing(self, mock_request, api_instance=api):
        test_project_ids = '12345,67891,23456'
        api_instance.get_challenge_listing(test_project_ids)
        mock_request.assert_called_once_with(
            f'{self.url}/challenges/listing',
            params={'projectIds': test_project_ids,
                    'limit': '10',
                    'page': '0',
                    'onlyEnabled': 'true'})

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_children(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.get_challenge_children(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}/challenge/{test_challenge_id}/children',
            params={'limit': '10',
                    'page': '0'})

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_comments(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.get_challenge_comments(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}/challenge/{test_challenge_id}/comments',
            params={'limit': '10',
                    'page': '0'})

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_extract_challenge_comments(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.extract_challenge_comments(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}/challenge/{test_challenge_id}/comments/extract',
            params={'limit': '10',
                    'page': '0'})

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_extract_task_summaries(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.extract_task_summaries(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}/challenge/{test_challenge_id}/tasks/extract',
            params={'limit': '10',
                    'page': '0',
                    'status': '',
                    'reviewStatus': '',
                    'priority': '',
                    'exportProperties': '',
                    'taskPropertySearch': ''})

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_geojson(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.get_challenge_geojson(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}/challenge/view/{test_challenge_id}',
            params={'status': '',
                    'reviewStatus': '',
                    'priority': '',
                    'taskPropertySearch': ''})

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_update_task_priorities(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.update_task_priorities(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}/challenge/{test_challenge_id}/updateTaskPriorities',
            json=None,
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_reset_task_instructions(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.reset_task_instructions(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}/challenge/{test_challenge_id}/resetTaskInstructions',
            json=None,
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.delete')
    def test_delete_challenge(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.delete_challenge(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}/challenge/{test_challenge_id}',
            params={'immediate': 'false'})

    @patch('maproulette.api.maproulette_server.requests.Session.delete')
    def test_delete_challenge_tasks(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.delete_challenge_tasks(test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}/challenge/{test_challenge_id}/tasks',
            params={'statusFilters': ''})

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_update_challenge(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        test_challenge_model = maproulette.ChallengeModel(name='Test_Challenge_Name',
                                                          instruction='Do something',
                                                          description='This is a test challenge',
                                                          overpassQL=test_overpassQL_query)
        api_instance.update_challenge(test_challenge_id, test_challenge_model)
        mock_request.assert_called_once_with(
            f'{self.url}/challenge/{test_challenge_id}',
            json=json.loads(create_challenge_output),
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_rebuild_challenge(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        api_instance.rebuild_challenge(test_challenge_id, True, True)
        mock_request.assert_called_once_with(
            f'{self.url}/challenge/{test_challenge_id}/rebuild',
            params={'removeUnmatched': 'true', 'skipSnapshot': 'true'},
            json=None)
