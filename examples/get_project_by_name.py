import maproulette as mr
import json

# Create a configuration object using an API key
config = mr.Configuration(api_key='YOUR_API_KEY')
# Create an API object using your config object
api = mr.Api(config)

# We want to fetch a project with name 'test_intersection_analysis_1'
my_project_name = 'Health Facilities in India'

# Print the API response
print(json.dumps(api.get_project_by_name(my_project_name), indent=4, sort_keys=True))
