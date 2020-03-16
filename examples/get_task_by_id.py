import maproulette
import json

# Create a configuration object for MapRoulette using your API key:
config = maproulette.Configuration(api_key="API_KEY")

# Create an API objects with the above config object:
api = maproulette.Api(config)

# Specify the ID of the challenge you want up add tasks to:
task_id = 'TEST_ID'

# Printing response
print(json.dumps(api.get_task_by_id(task_id)))