"""This module contains the basic methods that handle API calls to the MapRoulette API. It uses the requests library to
accomplish this."""

import requests
import json
from .errors import HttpError, InvalidJsonError, ConnectionUnavailableError, UnauthorizedError, NotFoundError


class MapRouletteServer:
    """Class that holds the basic requests that can be made to the MapRoulette API."""
    def __init__(self, configuration):
        self.url = configuration.url
        self.base_url = configuration.base_url
        self.headers = configuration.headers
        if self.check_health():
            self.session = requests.Session()

    def check_health(self):
        """Checks health of connection to host by pinging the URL set in the configuration"""
        response = requests.get(
            self.base_url + '/ping',
            headers=self.headers,
            verify=False
        )
        if response.ok:
            return True
        else:
            raise ConnectionUnavailableError(
                message='Specified server unavailable',
                status=response.status_code,
                payload=response
            )

    def get(self, endpoint, params=None):
        """Method that completes a GET request to the MapRoulette API

        :param endpoint: the server endpoint to use for the GET request
        :param params: the parameters that pertain to the request (optional)
        :returns: a JSON object containing the API response
        """
        response = self.session.get(
            self.url + endpoint,
            params=params,
            headers=self.headers,
            verify=False)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                raise NotFoundError(
                    message='Resource not found',
                    status=e.response.status_code,
                    payload=e.response
                ) from None
            else:
                raise HttpError(
                    message='An HTTP error occurred',
                    status=e.response.status_code,
                    payload=e.response
                ) from None
        except (requests.ConnectionError, requests.Timeout) as e:
            raise ConnectionUnavailableError(
                message="Connection Unavailable",
                status=e.response.status_code,
                payload=response
            ) from None
        try:
            return {
                "data": response.json(),
                "status": response.status_code
            }
        except json.decoder.JSONDecodeError:
            return {
                "status": response.status_code
            }

    def post(self, endpoint, body=None):
        """Method that completes a POST request to the MapRoulette API

        :param endpoint: the server endpoint to use for the POST request
        :param body: the body of the request (optional)
        :returns: a JSON object containing the API response
        """
        response = self.session.post(
            self.url + endpoint,
            json=body,
            headers=self.headers,
            verify=False)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 400:
                raise InvalidJsonError(
                    message='Invalid JSON payload',
                    status=e.response.status_code,
                    payload=e.response
                ) from None
            elif e.response.status_code == 401:
                raise UnauthorizedError(
                    message='The user is not authorized to make this request',
                    status=e.response.status_code,
                    payload=e.response
                ) from None
            else:
                raise HttpError(
                    message='An HTTP error occurred',
                    status=e.response.status_code,
                    payload=e.response
                ) from None
        except (requests.ConnectionError, requests.Timeout) as e:
            raise ConnectionUnavailableError(e) from None
        try:
            return {
                "data": response.json(),
                "status": response.status_code
            }
        except json.decoder.JSONDecodeError:
            return {
                "status": response.status_code
            }

    def put(self, endpoint, body=None):
        """Method that completes a PUT request to the MapRoulette API

        :param endpoint: the server endpoint to use for the PUT request
        :param body: the body of the request (optional)
        :returns: a JSON object containing the response code and the API response if
        """
        response = self.session.put(
            self.url + endpoint,
            json=body,
            headers=self.headers,
            verify=False)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 400:
                raise InvalidJsonError(
                    message='Invalid JSON payload',
                    status=e.response.status_code,
                    payload=e.response
                ) from None
            elif e.response.status_code == 401:
                raise UnauthorizedError(
                    message='The user is not authorized to make this request',
                    status=e.response.status_code,
                    payload=e.response
                ) from None
            else:
                raise HttpError(
                    message='An HTTP error occurred',
                    status=e.response.status_code,
                    payload=e.response
                ) from None
        except (requests.ConnectionError, requests.Timeout) as e:
            raise ConnectionUnavailableError(e) from None
        try:
            return {
                "data": response.json(),
                "status": response.status_code
            }
        except json.decoder.JSONDecodeError:
            return {
                "status": response.status_code
            }

    def delete(self, endpoint):
        """Method that completes a DELETE request to the MapRoulette API

        :param endpoint: the server endpoint to use for the DELETE request
        :returns: a JSON object containing the API response
        """
        response = self.session.delete(
            self.url + endpoint,
            headers=self.headers)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise UnauthorizedError(
                    message='The user is not authorized to make this request',
                    status=e.response.status_code,
                    payload=e.response
                ) from None
            elif e.response.status_code == 404:
                raise NotFoundError(
                    message='Resource not found',
                    status=e.response.status_code,
                    payload=e.response
                ) from None
            else:
                raise HttpError(
                    message='An HTTP error occurred',
                    status=e.response.status_code,
                    payload=e.response
                ) from None
        except (requests.ConnectionError, requests.Timeout) as e:
            raise ConnectionUnavailableError(e) from None
        try:
            return {
                "data": response.json(),
                "status": response.status_code
            }
        except json.decoder.JSONDecodeError:
            return {
                "status": response.status_code
            }

    @staticmethod
    def is_json(input_object):
        """Method to determine whether user input is valid JSON.

        :param input_object: the user's input to check
        :returns: True if valid json object
        """
        try:
            json_object = json.loads(input_object)
            del json_object
            return True
        except ValueError:
            return False
