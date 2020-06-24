import maproulette
import json

# Create a configuration object using a url and API key
config = maproulette.Configuration(api_key='{YOUR_API_KEY}')

# Create an API object using your config object
api = maproulette.Project(config)

# We can fetch a project using the name 'Health Facilities in India':
my_project_name = 'Health Facilities in India'

# Print the API response
print(json.dumps(api.find_project(my_project_name), indent=4, sort_keys=True))

# We can also fetch a project using the project ID:
my_project_id = '4719'

# Print the API response
print(json.dumps(api.get_project_by_id(my_project_id), indent=4, sort_keys=True))

# We can access the project's challenges as well:
print(json.dumps(api.get_project_challenges(my_project_id), indent=4, sort_keys=True))

# If we want to create a new project, we can use the Project Model:
my_project = maproulette.ProjectModel(name='my_new_project_name_20200120_abc')

# You can set other parameters like your project description like this:
my_project.description = 'my project description'

# Print the API response
print(json.dumps(api.create_project(my_project), indent=4, sort_keys=True))
