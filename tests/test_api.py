import maproulette
import requests
import unittest
from tests.sample_data import test_geojson, test_overpassQL_query
from maproulette.api import errors
from unittest import mock
from unittest.mock import patch


class TestAPI(unittest.TestCase):

    config = maproulette.Configuration(api_key="API_KEY")
    api = maproulette.Api(config)
    server = maproulette.MapRouletteServer(configuration=config)

    @patch('maproulette.api.maproulette_server.requests.get')
    def test_get_project_by_id(self, mock_request, api_instance=api):
        test_project_id = '32922'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_project_by_id(test_project_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.get')
    def test_get_project_by_name(self, mock_request, api_instance=api):
        test_project_name = 'Maptime!'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_project_by_name(test_project_name)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.get')
    def test_find_project(self, mock_request, api_instance=api):
        test_search = 'Health Facilities in India'
        mock_request.return_value.status_code = '200'
        response = api_instance.find_project(test_search)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.get')
    def test_get_project_challenges(self, mock_request, api_instance=api):
        test_project_id = '12974'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_project_challenges(test_project_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.post')
    def test_create_project(self, mock_request, api_instance=api):
        test_project_model = maproulette.ProjectModel(name='Test_Project_Name',
                                                      description='This is a test project')
        mock_request.return_value.status_code = '200'
        response = api_instance.create_project(test_project_model)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.get')
    def test_get_task_by_id(self, mock_request, api_instance=api):
        test_task_id = '42914448'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_task_by_id(test_task_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.get')
    def test_get_challenge_by_id(self, mock_request, api_instance=api):
        test_challenge_id = '12974'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_challenge_by_id(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.get')
    def test_get_challenge_statistics_by_id(self, mock_request, api_instance=api):
        test_challenge_id = '12974'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_challenge_statistics_by_id(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.get')
    def test_get_challenge_tasks(self, mock_request, api_instance=api):
        test_challenge_id = '12974'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_challenge_tasks(test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.post')
    def test_create_challenge(self, mock_request, api_instance=api):
        test_challenge_model = maproulette.ChallengeModel(name='Test_Challenge_Name',
                                                          instruction='Do something',
                                                          description='This is a test challenge',
                                                          overpassQL=test_overpassQL_query)
        mock_request.return_value.status_code = '200'
        response = api_instance.create_challenge(test_challenge_model)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.put')
    def test_add_tasks_to_challenge(self, mock_request, api_instance=api):
        test_challenge_id = '12978'
        mock_request.return_value.status_code = '200'
        response = api_instance.add_tasks_to_challenge(test_geojson, test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.get')
    def test_get_http_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.HTTPError()
        with self.assertRaises(requests.exceptions.HTTPError):
            self.server.get(endpoint='')

    @patch('maproulette.api.maproulette_server.requests.get')
    def test_get_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError()
        with self.assertRaises(requests.exceptions.ConnectionError):
            self.server.get(endpoint='')

    @patch('maproulette.api.maproulette_server.requests.post')
    def test_post_http_error(self, mock_post):
        mock_post.side_effect = requests.exceptions.HTTPError()
        with self.assertRaises(requests.exceptions.HTTPError):
            self.server.post(endpoint='')

    @patch('maproulette.api.maproulette_server.requests.post')
    def test_post_connection_error(self, mock_post):
        mock_post.side_effect = requests.exceptions.ConnectionError()
        with self.assertRaises(requests.exceptions.ConnectionError):
            self.server.post(endpoint='')

    @patch('maproulette.api.maproulette_server.requests.put')
    def test_put_http_error(self, mock_put):
        mock_put.side_effect = requests.exceptions.HTTPError()
        with self.assertRaises(requests.exceptions.HTTPError):
            self.server.put(endpoint='')

    @patch('maproulette.api.maproulette_server.requests.put')
    def test_put_connection_error(self, mock_put):
        mock_put.side_effect = requests.exceptions.ConnectionError()
        with self.assertRaises(requests.exceptions.ConnectionError):
            self.server.put(endpoint='')

    @patch('maproulette.api.maproulette_server.requests.delete')
    def test_delete_http_error(self, mock_delete):
        mock_delete.side_effect = requests.exceptions.HTTPError()
        with self.assertRaises(requests.exceptions.HTTPError):
            self.server.delete(endpoint='')

    @patch('maproulette.api.maproulette_server.requests.delete')
    def test_delete_connection_error(self, mock_delete):
        mock_delete.side_effect = requests.exceptions.ConnectionError()
        with self.assertRaises(requests.exceptions.ConnectionError):
            self.server.delete(endpoint='')
