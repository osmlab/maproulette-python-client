import maproulette
import unittest
from tests.sample_data import test_project
from unittest.mock import patch


class TestProjectAPI(unittest.TestCase):

    config = maproulette.Configuration(api_key="API_KEY")
    api = maproulette.Project(config)
    url = config.api_url

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_project_by_id(self, mock_request, api_instance=api):
        test_project_id = '32922'
        api_instance.get_project_by_id(test_project_id)
        mock_request.assert_called_once_with(
            f'{self.url}/project/{test_project_id}',
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_project_by_name(self, mock_request, api_instance=api):
        test_project_name = 'Maptime!'
        api_instance.get_project_by_name(test_project_name)
        mock_request.assert_called_once_with(
            f'{self.url}/projectByName/{test_project_name}',
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_find_project(self, mock_request, api_instance=api):
        test_search = 'Health Facilities in India'
        api_instance.find_project(test_search)
        mock_request.assert_called_once_with(
            f'{self.url}/projects',
            params={'search': test_search,
                    'limit': '10',
                    'page': '0',
                    'onlyEnabled': 'true'})

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_project_challenges(self, mock_request, api_instance=api):
        test_project_id = '12974'
        api_instance.get_project_challenges(test_project_id)
        mock_request.assert_called_once_with(
            f'{self.url}/project/{test_project_id}/challenges',
            params={'limit': '10',
                    'page': '0'})

    @patch('maproulette.api.maproulette_server.requests.Session.post')
    def test_create_project(self, mock_request, api_instance=api):
        test_project_model = maproulette.ProjectModel(name='Test_Project_Name',
                                                      description='This is a test project')
        api_instance.create_project(test_project_model)
        mock_request.assert_called_once_with(
            f'{self.url}/project',
            json=test_project,
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.post')
    def test_add_challenge_to_project(self, mock_request, api_instance=api):
        test_virtual_project_model = maproulette.ProjectModel(name='Test Virtual Project Name',
                                                              id=1234)
        test_challenge_model = maproulette.ChallengeModel(name='Test Challenge Name',
                                                          id=246)
        test_virtual_project_id = test_virtual_project_model.id
        test_challenge_id = test_challenge_model.id
        api_instance.add_challenge_to_project(test_virtual_project_id, test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}/project/{test_virtual_project_id}/challenge/{test_challenge_id}/add',
            json=None,
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.post')
    def test_remove_challenge_from_project(self, mock_request, api_instance=api):
        test_virtual_project_model = maproulette.ProjectModel(name='Test Virtual Project Name',
                                                              id=1234)
        test_challenge_model = maproulette.ChallengeModel(name='Test Challenge Name', id=246)
        test_virtual_project_id = test_virtual_project_model.id
        test_challenge_id = test_challenge_model.id
        api_instance.remove_challenge_from_project(test_virtual_project_id, test_challenge_id)
        mock_request.assert_called_once_with(
            f'{self.url}/project/{test_virtual_project_id}/challenge/{test_challenge_id}/remove',
            json=None,
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.delete')
    def test_delete_project(self, mock_request, api_instance=api):
        test_project_model = maproulette.ProjectModel(name='Test Project Name', id=1234)
        test_project_id = test_project_model.id
        api_instance.delete_project(test_project_id)
        mock_request.assert_called_once_with(
            f'{self.url}/project/{test_project_id}',
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.put')
    def test_update_project(self, mock_request, api_instance=api):
        test_project_model = maproulette.ProjectModel(name='Test Project Name', id=1234)
        test_updated_project_name = 'Test Updated Project Name'
        test_updated_project_model = maproulette.ProjectModel(name=test_updated_project_name)
        test_project_model_id = test_project_model.id
        api_instance.update_project(test_project_model_id, test_updated_project_model)
        mock_request.assert_called_once_with(
            f'{self.url}/project/{test_project_model_id}',
            json={'name': test_updated_project_name},
            params=None)

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_project_by_ids(self, mock_request, api_instance=api):
        test_project_ids = '1234,2468,1356'
        api_instance.get_projects_by_ids(test_project_ids)
        mock_request.assert_called_once_with(
            f'{self.url}/projectsById',
            params={'projectIds': test_project_ids})

    @patch('maproulette.api.maproulette_server.requests.Session.get')
    def test_get_random_tasks(self, mock_request, api_instance=api):
        test_project_model = maproulette.ProjectModel(name='Test Project Name',
                                                      id=1234)
        test_project_id = test_project_model.id
        api_instance.get_random_tasks(test_project_id)
        mock_request.assert_called_once_with(
            f'{self.url}/project/{test_project_id}/tasks',
            params={'limit': '1',
                    'proximity': '-1',
                    'search': ''})
