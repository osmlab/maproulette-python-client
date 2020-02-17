import json
import maproulette as mr

# Create a configuration object using an API key
configuration = mr.Configuration(api_key='{YOUR_API_KEY}')

# Create an API object using your config object
api = mr.Api(configuration)

# Initialize a project model using the project name
my_project = mr.ProjectModel(name='my_new_project_name_20200120_abc')

# You can set other parameters like your project description like this:
my_project.description = 'my project description'

# Print the API response
print(json.dumps(api.create_project(my_project), indent=4, sort_keys=True))
