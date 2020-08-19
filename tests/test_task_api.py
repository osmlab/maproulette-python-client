import json
import maproulette
import unittest
from tests.sample_data import test_geojson
from unittest.mock import patch


class TestTaskAPI(unittest.TestCase):

    config = maproulette.Configuration(api_key="API_KEY")
    api = maproulette.Task(config)

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_task_by_id(self, mock_request, api_instance=api):
        test_task_id = '42914448'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_task_by_id(test_task_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_task_history(self, mock_request, api_instance=api):
        test_task_id = '42914448'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_task_history(test_task_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.post')
    def test_create_tasks(self, mock_request, api_instance=api):
        test_tasks = []
        geometries = test_geojson['features'][0]['geometry']
        test_task_model = maproulette.TaskModel(name='test_task',
                                                parent='12345',
                                                geometries=geometries)
        test_tasks.append(test_task_model.to_dict())
        mock_request.return_value.status_code = '200'
        responses = api_instance.create_tasks(test_tasks)
        for response in responses:
            self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_update_tasks(self, mock_request, api_instance=api):
        geometries = test_geojson['features'][0]['geometry']
        test_task_model = maproulette.TaskModel(name='test_task',
                                                parent='12345',
                                                geometries=geometries)
        mock_request.return_value.status_code = '200'
        response = api_instance.update_tasks(test_task_model)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_task_tags(self, mock_request, api_instance=api):
        task_id = '42914448'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_task_tags(task_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.delete')
    def test_delete_task_tags(self, mock_request, api_instance=api):
        task_id = '42914448'
        tags = 'test'
        mock_request.return_value.status_code = '200'
        response = api_instance.delete_task_tags(task_id, tags)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_tasks_by_tags(self, mock_request, api_instance=api):
        tags = 'test'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_tasks_by_tags(tags)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_update_task_tags(self, mock_request, api_instance=api):
        task_id = '42914448'
        tags = 'test'
        mock_request.return_value.status_code = '200'
        response = api_instance.update_task_tags(task_id, tags)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_update_task_status(self, mock_request, api_instance=api):
        task_id = '42914448'
        status = 3
        mock_request.return_value.status_code = '200'
        response = api_instance.update_task_status(task_id, status)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_task_comments(self, mock_request, api_instance=api):
        task_id = '42914448'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_task_comments(task_id)
        self.assertEqual(response['status'], '200')

    def test_batch_generator(self, api_instance=api):

        batch_size = 10
        test_length = 1234
        test_list = [i for i in range(test_length)]
        running_total = 0
        for chunk in api_instance.batch_generator(test_list, batch_size):
            running_total += len(chunk)
            self.assertIsInstance(chunk, list)
            self.assertLessEqual(len(chunk), batch_size)
        self.assertEqual(test_length, running_total)
