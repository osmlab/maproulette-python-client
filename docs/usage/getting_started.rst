Getting Started
=====================================================

Install the package (or add it to your requirements.txt file):

.. code-block:: bash

    $ pip install maproulette

Import the package:

.. code-block:: python

    import maproulette


From there, create a configuration object. When creating the configuration you can specify a number of of parameters
depending on your needs including the hostname, protocol, and client-side certificates. Depending on your use case, you
may need to obtain and pass your API key as well. For example:

.. code-block:: python

    config = maproulette.Configuration(api_key='{YOUR_API_KEY}')


Once you have your configuration object we can create an API object using one of several modules depending on the
functionality that the user is looking for. For example, creating a Project object allows the user to interact with all
of the project-related functionality in the MapRoulette package.

.. code-block:: python

    api = maproulette.Project(config)


Now we have access to the MapRoulette Project API methods. In the example below, I want to find a project by name using
a search string:

.. code-block:: python

    # We want to fetch a project with name 'Health Facilities in India'
    my_project_name = 'Health Facilities in India'

    # Pretty-print the API response
    print(json.dumps(api.find_project(my_project_name), indent=4, sort_keys=True))

This returns a nicely printed JSON object representing the project named 'Health Facilities in India':

.. code-block:: json

    {
        "data": [
            {
                "created": "2019-08-26T06:34:28.655Z",
                "deleted": false,
                "description": "Adding the Hospitals ",
                "displayName": "Health Facilities in India",
                "enabled": true,
                "featured": false,
                "groups": [
                    {
                        "created": "2020-03-25T16:23:04.360Z",
                        "groupType": 1,
                        "id": 9273,
                        "modified": "2020-03-25T16:23:04.360Z",
                        "name": "4719_Admin",
                        "projectId": 4719
                    },
                    {
                        "created": "2020-03-25T16:23:04.360Z",
                        "groupType": 2,
                        "id": 9274,
                        "modified": "2020-03-25T16:23:04.360Z",
                        "name": "4719_Write",
                        "projectId": 4719
                    },
                    {
                        "created": "2020-03-25T16:23:04.360Z",
                        "groupType": 3,
                        "id": 9275,
                        "modified": "2020-03-25T16:23:04.360Z",
                        "name": "4719_Read",
                        "projectId": 4719
                    }
                ],
                "id": 4719,
                "isVirtual": false,
                "modified": "2020-01-30T11:05:44.466Z",
                "name": "health_facilities_in_india",
                "owner": 4785024
            }
        ],
        "status": 200
    }
