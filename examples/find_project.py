import maproulette
import json

# Create a configuration object using a url and API key
config = maproulette.Configuration(api_key="API_KEY")

# Create an API object using your config object
api = maproulette.Api(config)

# We want to fetch a project with name 'Health Facilities in India'
my_project_name = 'Health Facilities in India'

# Print the API response
print(json.dumps(api.find_project(my_project_name), indent=4, sort_keys=True))
