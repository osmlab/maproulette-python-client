import maproulette
import unittest
from tests.sample_data import test_geojson, test_overpassQL_query
from unittest.mock import patch


class TestProjectAPI(unittest.TestCase):

    config = maproulette.Configuration(api_key="API_KEY")
    api = maproulette.Project(config)

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_project_by_id(self, mock_request, api_instance=api):
        test_project_id = '32922'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_project_by_id(test_project_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_project_by_name(self, mock_request, api_instance=api):
        test_project_name = 'Maptime!'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_project_by_name(test_project_name)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_find_project(self, mock_request, api_instance=api):
        test_search = 'Health Facilities in India'
        mock_request.return_value.status_code = '200'
        response = api_instance.find_project(test_search)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_project_challenges(self, mock_request, api_instance=api):
        test_project_id = '12974'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_project_challenges(test_project_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.post')
    def test_create_project(self, mock_request, api_instance=api):
        test_project_model = maproulette.ProjectModel(name='Test_Project_Name',
                                                      description='This is a test project')
        mock_request.return_value.status_code = '200'
        response = api_instance.create_project(test_project_model)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.post')
    def test_add_challenge_to_project(self, mock_request, api_instance=api):
        test_virtual_project_model = maproulette.ProjectModel(name='Test Virtual Project Name',
                                                              id=1234,
                                                              is_virtual=True)
        test_challenge_model = maproulette.ChallengeModel(name='Test Challenge Name',
                                                          id=246)
        test_virtual_project_id = test_virtual_project_model.id
        test_challenge_id = test_challenge_model.id
        mock_request.return_value.status_code = '200'
        response = api_instance.add_challenge_to_project(test_virtual_project_id, test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.post')
    def test_remove_challenge_from_project(self, mock_request, api_instance=api):
        test_virtual_project_model = maproulette.ProjectModel(name='Test Virtual Project Name',
                                                              id=1234,
                                                              is_virtual=True)
        test_challenge_model = maproulette.ChallengeModel(name='Test Challenge Name', id=246)
        test_virtual_project_id = test_virtual_project_model.id
        test_challenge_id = test_challenge_model.id
        mock_request.return_value.status_code = '200'
        response = api_instance.remove_challenge_from_project(test_virtual_project_id, test_challenge_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.delete')
    def test_delete_project(self, mock_request, api_instance=api):
        test_project_model = maproulette.ProjectModel(name='Test Project Name', id=1234)
        test_project_id = test_project_model.id
        mock_request.return_value.status_code = '200'
        response = api_instance.delete_project(test_project_id)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_update_project(self, mock_request, api_instance=api):
        test_project_model = maproulette.ProjectModel(name='Test Project Name', id=1234)
        test_updated_project_model = maproulette.ProjectModel(name='Test Updated Project Name')
        test_project_model_id = test_project_model.id
        mock_request.return_value.status_code = '200'
        response = api_instance.update_project(test_project_model_id, test_updated_project_model)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_project_by_ids(self, mock_request, api_instance=api):
        test_project_ids = '1234,2468,1356'
        mock_request.return_value.status_code = '200'
        response = api_instance.get_projects_by_ids(test_project_ids)
        self.assertEqual(response['status'], '200')

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_random_tasks(self, mock_request, api_instance=api):
        test_project_model = maproulette.ProjectModel(name='Test Project Name',
                                                      id=1234)
        test_project_id = test_project_model.id
        mock_request.return_value.status_code = '200'
        response = api_instance.get_random_tasks(test_project_id)
        self.assertEqual(response['status'], '200')
