import maproulette as mr
import json

# Create a configuration object using a url and API key
config = mr.Configuration(api_key='YOUR_API_KEY')
# Create an API object using your config object
api = mr.Api(config)

# I know my project ID is 83
my_project_id = '4719'

# Print the API response
print(json.dumps(api.get_project_challenges(my_project_id), indent=4, sort_keys=True))