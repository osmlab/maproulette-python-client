import maproulette
import unittest
from tests.sample_data import test_geojson, test_overpassQL_query
from unittest.mock import patch


class TestChallengeAPI(unittest.TestCase):

    config = maproulette.Configuration(api_key="API_KEY")
    api = maproulette.Challenge(config)

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_by_id(self, mock_request, api_instance=api):
        test_challenge_id = '12974'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_challenge_by_id(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_statistics_by_id(self, mock_request, api_instance=api):
        test_challenge_id = '12974'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_challenge_statistics_by_id(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_tasks(self, mock_request, api_instance=api):
        test_challenge_id = '12974'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_challenge_tasks(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.post')
    def test_create_challenge(self, mock_request, api_instance=api):
        test_challenge_model = maproulette.ChallengeModel(name='Test_Challenge_Name',
                                                          instruction='Do something',
                                                          description='This is a test challenge',
                                                          overpassQL=test_overpassQL_query)
        mock_request.return_value.status_code = '200'
        response = api_instance.create_challenge(test_challenge_model)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_add_tasks_to_challenge(self, mock_request, api_instance=api):
        test_challenge_id = '12978'
        mock_request.return_value.status_code = '200'
        response = api_instance.add_tasks_to_challenge(test_geojson, test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.post')
    def test_create_virtual_challenge(self, mock_request, api_instance=api):
        # TODO: add model for virtual challenge to aid in posting
        test_challenge_model = maproulette.ChallengeModel(name='Test_Challenge_Name',
                                                          instruction='Do something',
                                                          description='This is a test challenge',
                                                          overpassQL=test_overpassQL_query)
        mock_request.return_value.status_code = '200'
        response = api_instance.create_virtual_challenge(test_challenge_model)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_by_name(self, mock_request, api_instance=api):
        test_project_id = '12345'
        test_challenge_name = 'Test_Challenge_Name'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_challenge_by_name(test_project_id, test_challenge_name)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenges_by_tags(self, mock_request, api_instance=api):
        test_challenge_tag = 'River'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_challenges_by_tags(test_challenge_tag)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_virtual_challenge_by_id(self, mock_request, api_instance=api):
        test_virtual_challenge_id = '12345'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_virtual_challenge_by_id(test_virtual_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_listing(self, mock_request, api_instance=api):
        test_project_ids = '12345,67891,23456'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_challenge_listing(test_project_ids)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_children(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_challenge_children(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_comments(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_challenge_comments(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_extract_challenge_comments(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        mock_request.return_value.status_code = '200'
        response = api_instance.extract_challenge_comments(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_extract_task_summaries(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        mock_request.return_value.status_code = '200'
        response = api_instance.extract_task_summaries(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_challenge_geojson(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_challenge_geojson(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_update_task_priorities(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        mock_request.return_value.status_code = '200'
        response = api_instance.update_task_priorities(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_reset_task_instructions(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        mock_request.return_value.status_code = '200'
        response = api_instance.reset_task_instructions(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.delete')
    def test_delete_challenge(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        mock_request.return_value.status_code = '200'
        response = api_instance.delete_challenge(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.delete')
    def test_delete_challenge_tasks(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        mock_request.return_value.status_code = '200'
        response = api_instance.delete_challenge_tasks(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_update_challenge(self, mock_request, api_instance=api):
        test_challenge_id = '12345'
        test_challenge_model = maproulette.ChallengeModel(name='Test_Challenge_Name',
                                                          instruction='Do something',
                                                          description='This is a test challenge',
                                                          overpassQL=test_overpassQL_query)
        mock_request.return_value.status_code = '200'
        response = api_instance.update_challenge(test_challenge_id, test_challenge_model)
        self.assertEqual(response['status'], '200')
