# MapRoulette - A Python Client for the MapRoulette API


https://maproulette-python-client.readthedocs.io

[![PyPI version](https://badge.fury.io/py/maproulette.svg)](https://badge.fury.io/py/maproulette)
[![Build Status](https://travis-ci.com/osmlab/maproulette-python-client.svg?branch=master)](https://travis-ci.com/osmlab/maproulette-python-client)

This client makes it easy for users to communicate with the MapRoulette API from within
their Python environment. In the example below, we are able to access a MapRoulette project in just four lines of code:

```
   >>> import maproulette
   >>> config = maproulette.Configuration()
   >>> api = maproulette.Project(config)
   >>> api.get_project_by_id(4719)
   {'data': {'id': 4719, 'owner': 4785024, 'name': 'health_facilities_in_india',...}
```

The full documentation for this package can be found [here](https://maproulette-python-client.readthedocs.io/). 


## Getting Started

Install the package (or add it to your requirements.txt file):

```bash
pip install maproulette
```

Import the package:

```
import maproulette
```

From there, create a configuration object. Depending on your use case, you may need to pass your API key. Specify
that when you create your configuration. For example:

```
config = maproulette.Configuration(api_key='{YOUR_API_KEY}')
```

Once you have your configuration object we can create an API object using one of several modules depending on the
functionality that the user is looking for. For example, creating a Project object allows the user to interact with all
of the project-related functionality in the MapRoulette package.

```
api = maproulette.Project(config)
```

Now we have access to the MapRoulette Project API methods. In the example below, I want to find a project by name using
a search string:

```
# We want to fetch a project with name 'Health Facilities in India'
my_project_name = 'Health Facilities in India'

# Pretty-print the API response
print(json.dumps(api.find_project(my_project_name), indent=4, sort_keys=True))
```

This returns a nicely printed JSON object representing the project named 'Health Facilities in India':

```
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
```
## Development

### Contributing

Open an issue! Thanks for contributing!

### Testing

This package uses [Tox](https://tox.readthedocs.io/en/latest/) to perform testing. In order to run Tox, execute the
`tox` command from the root directory. 


### Building the Documentation

The documentation for this package is built with [Sphinx](https://www.sphinx-doc.org/en/master/index.html). In order to
build the documentation for this package: 

```
$ cd docs
``` 
and then: 
```
$ make html
```
That command will generate the HTML documentation files for the project. We've hosted these docs at
[Read the Docs](https://readthedocs.org/). 
