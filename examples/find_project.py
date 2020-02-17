import maproulette as mr
import json

# Create a configuration object using a url and API key
config = mr.Configuration(api_key='{YOUR_API_KEY}')
# Create an API object using your config object
api = mr.Api(config)

# We want to fetch a project with name 'test_intersection_analysis_1'
my_project_name = 'Health Facilities in India'

print(json.dumps(api.find_project(my_project_name), indent=4, sort_keys=True))
