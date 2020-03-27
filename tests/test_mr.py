import maproulette
import json
import unittest
import pytest
from unittest.mock import patch


def test_example():
    assert 1 == 1


class TestRequests(unittest.TestCase):

    config = maproulette.Configuration(api_key="API_KEY")
    api = maproulette.Api(config)

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
                                                          overpassQL="""way["name"="Københavns Lufthavn"];
                                                                        out body geom qt;""")
        mock_request.return_value.status_code = '200'
        response = api_instance.create_challenge_from_model(test_challenge_model)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.put')
    def test_add_tasks_to_challenge(self, mock_request, api_instance=api):
        test_challenge_id = '12978'
        test_challenge_geometry = json.loads("""{
                                        "type": "FeatureCollection",
                                        "generator": "JOSM",
                                        "features": [
                                            {
                                                "type": "Feature",
                                                "properties": null,
                                                "geometry": {
                                                    "type": "LineString",
                                                    "coordinates": [
                                                        [
                                                            -0.13698190844,
                                                            50.81561190201
                                                        ],
                                                        [
                                                            -0.13702256313,
                                                            50.81534476302
                                                        ]
                                                    ]
                                                }
                                            }
                                        ]
                                    }""")
        mock_request.return_value.status_code = '200'
        response = api_instance.add_tasks_to_challenge(test_challenge_geometry, test_challenge_id)
        self.assertEqual(response['status'], '200')
