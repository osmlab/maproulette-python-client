import json
import maproulette as mr
configuration = mr.Configuration(api_key='{YOUR_API_KEY}')

api = mr.Api(configuration)

my_project = mr.ProjectModel(name='my_new_project_name_20200120_abc')
my_project.description = 'my project description'

api.create_project(my_project)
print(json.dumps(api.create_project(my_project), indent=4, sort_keys=True))
