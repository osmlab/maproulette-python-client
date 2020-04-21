import maproulette
import requests
import unittest
from maproulette.api import errors
from unittest.mock import patch
from unittest import mock


class TestAPI(unittest.TestCase):

    config = maproulette.Configuration(api_key="API_KEY")
    server = maproulette.MapRouletteServer(configuration=config)

    @patch('maproulette.api.maproulette_server.MapRouletteServer.get')
    @patch('requests.get')
    def test_get_not_found_error(self, mock_get, mock_server_get, server_instance=server):
        mock_response = mock.Mock()
        requests_http_error = requests.exceptions.HTTPError()
        not_found_error = errors.NotFoundError(message='Resource not found',
                                               status=404,
                                               payload='error payload')
        mock_response.raise_for_status.side_effect = requests_http_error
        mock_get.return_value = mock_response
        mock_server_get.side_effect = not_found_error
        with self.assertRaises(errors.NotFoundError) as context:
            server_instance.get(endpoint='')
        assert context.exception.message == 'Resource not found'
        assert context.exception.status == 404
        assert context.exception.payload == 'error payload'

    @patch('maproulette.api.maproulette_server.MapRouletteServer.get')
    @patch('requests.get')
    def test_get_generic_http_error(self, mock_get, mock_server_get, server_instance=server):
        mock_response = mock.Mock()
        requests_http_error = requests.exceptions.HTTPError()
        generic_http_error = errors.HttpError(message='An HTTP error occurred',
                                              status=403,
                                              payload='error payload')
        mock_response.raise_for_status.side_effect = requests_http_error
        mock_get.return_value = mock_response
        mock_server_get.side_effect = generic_http_error
        with self.assertRaises(errors.HttpError) as context:
            server_instance.get(endpoint='')
        assert context.exception.message == 'An HTTP error occurred'
        assert context.exception.status == 403
        assert context.exception.payload == 'error payload'

    @patch('maproulette.api.maproulette_server.MapRouletteServer.get')
    @patch('requests.get')
    def test_get_connection_error(self, mock_get, mock_server_get, server_instance=server):
        mock_response = mock.Mock()
        requests_connection_error = requests.exceptions.ConnectionError()
        connection_error = errors.ConnectionUnavailableError(message='Connection Unavailable',
                                                             status=500,
                                                             payload='error payload')
        mock_response.raise_for_status.side_effect = requests_connection_error
        mock_get.return_value = mock_response
        mock_server_get.side_effect = connection_error
        with self.assertRaises(errors.ConnectionUnavailableError) as context:
            server_instance.get(endpoint='')
        assert context.exception.message == 'Connection Unavailable'
        assert context.exception.status == 500
        assert context.exception.payload == 'error payload'

    @patch('maproulette.api.maproulette_server.MapRouletteServer.post')
    @patch('requests.post')
    def test_post_invalid_json_error(self, mock_post, mock_server_post, server_instance=server):
        mock_response = mock.Mock()
        requests_http_error = requests.exceptions.HTTPError()
        invalid_json_error = errors.InvalidJsonError(message='Invalid JSON payload',
                                                     status=400,
                                                     payload='error payload')
        mock_response.raise_for_status.side_effect = requests_http_error
        mock_post.return_value = mock_response
        mock_server_post.side_effect = invalid_json_error
        with self.assertRaises(errors.InvalidJsonError) as context:
            server_instance.post(endpoint='')
        assert context.exception.message == 'Invalid JSON payload'
        assert context.exception.status == 400
        assert context.exception.payload == 'error payload'

    @patch('maproulette.api.maproulette_server.MapRouletteServer.post')
    @patch('requests.post')
    def test_post_generic_http_error(self, mock_post, mock_server_post, server_instance=server):
        mock_response = mock.Mock()
        requests_http_error = requests.exceptions.HTTPError()
        generic_http_error = errors.HttpError(message='An HTTP error occurred',
                                              status=403,
                                              payload='error payload')
        mock_response.raise_for_status.side_effect = requests_http_error
        mock_post.return_value = mock_response
        mock_server_post.side_effect = generic_http_error
        with self.assertRaises(errors.HttpError) as context:
            server_instance.post(endpoint='')
        assert context.exception.message == 'An HTTP error occurred'
        assert context.exception.status == 403
        assert context.exception.payload == 'error payload'

    @patch('maproulette.api.maproulette_server.MapRouletteServer.post')
    @patch('requests.post')
    def test_post_unauthorized_error(self, mock_post, mock_server_post, server_instance=server):
        mock_response = mock.Mock()
        requests_http_error = requests.exceptions.HTTPError()
        unauthorized_error = errors.UnauthorizedError(message='The user is not authorized to make this request',
                                                      status=401,
                                                      payload='error payload')
        mock_response.raise_for_status.side_effect = requests_http_error
        mock_post.return_value = mock_response
        mock_server_post.side_effect = unauthorized_error
        with self.assertRaises(errors.UnauthorizedError) as context:
            server_instance.post(endpoint='')
        assert context.exception.message == 'The user is not authorized to make this request'
        assert context.exception.status == 401
        assert context.exception.payload == 'error payload'

    @patch('maproulette.api.maproulette_server.MapRouletteServer.post')
    @patch('requests.post')
    def test_post_connection_error(self, mock_post, mock_server_post, server_instance=server):
        mock_response = mock.Mock()
        requests_connection_error = requests.exceptions.ConnectionError()
        connection_error = errors.ConnectionUnavailableError(message='Connection Unavailable',
                                                             status=500,
                                                             payload='error payload')
        mock_response.raise_for_status.side_effect = requests_connection_error
        mock_post.return_value = mock_response
        mock_server_post.side_effect = connection_error
        with self.assertRaises(errors.ConnectionUnavailableError) as context:
            server_instance.post(endpoint='')
        assert context.exception.message == 'Connection Unavailable'
        assert context.exception.status == 500
        assert context.exception.payload == 'error payload'

    @patch('maproulette.api.maproulette_server.MapRouletteServer.put')
    @patch('requests.put')
    def test_put_invalid_json_error(self, mock_put, mock_server_put, server_instance=server):
        mock_response = mock.Mock()
        requests_http_error = requests.exceptions.HTTPError()
        invalid_json_error = errors.InvalidJsonError(message='Invalid JSON payload',
                                                     status=400,
                                                     payload='error payload')
        mock_response.raise_for_status.side_effect = requests_http_error
        mock_put.return_value = mock_response
        mock_server_put.side_effect = invalid_json_error
        with self.assertRaises(errors.InvalidJsonError) as context:
            server_instance.put(endpoint='')
        assert context.exception.message == 'Invalid JSON payload'
        assert context.exception.status == 400
        assert context.exception.payload == 'error payload'

    @patch('maproulette.api.maproulette_server.MapRouletteServer.put')
    @patch('requests.put')
    def test_put_generic_http_error(self, mock_put, mock_server_put, server_instance=server):
        mock_response = mock.Mock()
        requests_http_error = requests.exceptions.HTTPError()
        generic_http_error = errors.HttpError(message='An HTTP error occurred',
                                              status=403,
                                              payload='error payload')
        mock_response.raise_for_status.side_effect = requests_http_error
        mock_put.return_value = mock_response
        mock_server_put.side_effect = generic_http_error
        with self.assertRaises(errors.HttpError) as context:
            server_instance.put(endpoint='')
        assert context.exception.message == 'An HTTP error occurred'
        assert context.exception.status == 403
        assert context.exception.payload == 'error payload'

    @patch('maproulette.api.maproulette_server.MapRouletteServer.put')
    @patch('requests.put')
    def test_put_unauthorized_error(self, mock_put, mock_server_put, server_instance=server):
        mock_response = mock.Mock()
        requests_http_error = requests.exceptions.HTTPError()
        unauthorized_error = errors.UnauthorizedError(message='The user is not authorized to make this request',
                                                      status=401,
                                                      payload='error payload')
        mock_response.raise_for_status.side_effect = requests_http_error
        mock_put.return_value = mock_response
        mock_server_put.side_effect = unauthorized_error
        with self.assertRaises(errors.UnauthorizedError) as context:
            server_instance.put(endpoint='')
        assert context.exception.message == 'The user is not authorized to make this request'
        assert context.exception.status == 401
        assert context.exception.payload == 'error payload'

    @patch('maproulette.api.maproulette_server.MapRouletteServer.put')
    @patch('requests.put')
    def test_put_connection_error(self, mock_put, mock_server_put, server_instance=server):
        mock_response = mock.Mock()
        requests_connection_error = requests.exceptions.ConnectionError()
        connection_error = errors.ConnectionUnavailableError(message='Connection Unavailable',
                                                             status=500,
                                                             payload='error payload')
        mock_response.raise_for_status.side_effect = requests_connection_error
        mock_put.return_value = mock_response
        mock_server_put.side_effect = connection_error
        with self.assertRaises(errors.ConnectionUnavailableError) as context:
            server_instance.put(endpoint='')
        assert context.exception.message == 'Connection Unavailable'
        assert context.exception.status == 500
        assert context.exception.payload == 'error payload'

    @patch('maproulette.api.maproulette_server.MapRouletteServer.delete')
    @patch('requests.delete')
    def test_delete_unauthorized_error(self, mock_delete, mock_server_delete, server_instance=server):
        mock_response = mock.Mock()
        requests_http_error = requests.exceptions.HTTPError()
        unauthorized_error = errors.UnauthorizedError(message='The user is not authorized to make this request',
                                                      status=401,
                                                      payload='error payload')
        mock_response.raise_for_status.side_effect = requests_http_error
        mock_delete.return_value = mock_response
        mock_server_delete.side_effect = unauthorized_error
        with self.assertRaises(errors.UnauthorizedError) as context:
            server_instance.delete(endpoint='')
        assert context.exception.message == 'The user is not authorized to make this request'
        assert context.exception.status == 401
        assert context.exception.payload == 'error payload'

    @patch('maproulette.api.maproulette_server.MapRouletteServer.delete')
    @patch('requests.delete')
    def test_delete_not_found_error(self, mock_delete, mock_server_delete, server_instance=server):
        mock_response = mock.Mock()
        requests_http_error = requests.exceptions.HTTPError()
        not_found_error = errors.NotFoundError(message='Resource not found',
                                               status=404,
                                               payload='error payload')
        mock_response.raise_for_status.side_effect = requests_http_error
        mock_delete.return_value = mock_response
        mock_server_delete.side_effect = not_found_error
        with self.assertRaises(errors.NotFoundError) as context:
            server_instance.delete(endpoint='')
        assert context.exception.message == 'Resource not found'
        assert context.exception.status == 404
        assert context.exception.payload == 'error payload'

    @patch('maproulette.api.maproulette_server.MapRouletteServer.delete')
    @patch('requests.delete')
    def test_delete_generic_http_error(self, mock_delete, mock_server_delete, server_instance=server):
        mock_response = mock.Mock()
        requests_http_error = requests.exceptions.HTTPError()
        generic_http_error = errors.HttpError(message='An HTTP error occurred',
                                              status=403,
                                              payload='error payload')
        mock_response.raise_for_status.side_effect = requests_http_error
        mock_delete.return_value = mock_response
        mock_server_delete.side_effect = generic_http_error
        with self.assertRaises(errors.HttpError) as context:
            server_instance.delete(endpoint='')
        assert context.exception.message == 'An HTTP error occurred'
        assert context.exception.status == 403
        assert context.exception.payload == 'error payload'

    @patch('maproulette.api.maproulette_server.MapRouletteServer.delete')
    @patch('requests.delete')
    def test_delete_connection_error(self, mock_delete, mock_server_delete, server_instance=server):
        mock_response = mock.Mock()
        requests_connection_error = requests.exceptions.ConnectionError()
        connection_error = errors.ConnectionUnavailableError(message='Connection Unavailable',
                                                             status=500,
                                                             payload='error payload')
        mock_response.raise_for_status.side_effect = requests_connection_error
        mock_delete.return_value = mock_response
        mock_server_delete.side_effect = connection_error
        with self.assertRaises(errors.ConnectionUnavailableError) as context:
            server_instance.delete(endpoint='')
        assert context.exception.message == 'Connection Unavailable'
        assert context.exception.status == 500
        assert context.exception.payload == 'error payload'
