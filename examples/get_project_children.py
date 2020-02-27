import maproulette
import json

# Create a configuration object using an API key
config = maproulette.Configuration(api_key='YOUR_API_KEY')

# Create an API object using your config object
api = maproulette.Api(config)

# The ID of the project whose children I want to fetch is 4719
my_project_id = '4719'

# Print the API response
print(json.dumps(api.get_project_children(my_project_id), indent=4, sort_keys=True))
