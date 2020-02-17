import maproulette as mr
import json

# Create a configuration object using an API key
config = mr.Configuration(api_key='YOUR_API_KEY')
# Create an API object using your config object
api = mr.Api(config)

# My project ID is 83
my_project_id = '4719'

# Print the API response
print(json.dumps(api.get_project_children(my_project_id), indent=4, sort_keys=True))