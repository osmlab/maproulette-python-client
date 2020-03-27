import maproulette
import json

# Create a configuration object for MapRoulette using your API key:
config = maproulette.Configuration(api_key="API_KEY")

# Create an API objects with the above config object:
api = maproulette.Api(config)

# Specify the ID of the challenge you want up add tasks to:
challenge_id = '12978'

# Provide a GeoJSON of the task data:
with open('LOCAL_GEOJSON_FILE', 'r') as data_file:
    data = json.loads(data_file.read())

print(data)

# Printing response:
print(api.add_tasks_to_challenge(data, challenge_id))