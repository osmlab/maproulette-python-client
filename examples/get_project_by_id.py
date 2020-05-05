import maproulette
import json

# Create a configuration object using an API key
config = maproulette.Configuration(api_key='{YOUR_API_KEY}')

# Create an API object using your config object
api = maproulette.Project(config)

# We want to fetch a project with ID '4719'
my_project_id = '4719'

# Print the API response
print(json.dumps(api.get_project_by_id(my_project_id), indent=4, sort_keys=True))
