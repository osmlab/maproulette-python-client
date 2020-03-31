import maproulette
import json
import unittest
import os
import examples.data
import pytest
from unittest.mock import patch


def test_example():
    assert 1 == 1


class TestAPI(unittest.TestCase):

    config = maproulette.Configuration(api_key="API_KEY")
    api = maproulette.Api(config)
    test_data_dir = os.path.join(os.path.dirname(__file__), '../examples/data')
    test_geom = json.loads(open(os.path.join(test_data_dir, 'Example_Geometry.geojson'), 'r').read())
    test_query = open(os.path.join(test_data_dir, 'Example_OverpassQL_Query'), 'r').read()

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
    def test_create_challenge_from_model(self, mock_request, api_instance=api):
        test_challenge_model = maproulette.ChallengeModel(name='Test_Challenge_Name',
                                                          instruction='Do something',
                                                          description='This is a test challenge',
                                                          overpassQL=self.test_query)
        mock_request.return_value.status_code = '200'
        response = api_instance.create_challenge_from_model(test_challenge_model)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.put')
    def test_add_tasks_to_challenge(self, mock_request, api_instance=api):
        test_challenge_id = '12978'
        mock_request.return_value.status_code = '200'
        response = api_instance.add_tasks_to_challenge(self.test_geom, test_challenge_id)
        self.assertEqual(response['status'], '200')
