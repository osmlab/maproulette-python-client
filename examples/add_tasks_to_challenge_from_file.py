import maproulette
import json

# Create a configuration object for MapRoulette using your API key:
config = maproulette.Configuration(api_key="2450|wB+DfON5nZ1p8cclrgtILUaPHtuJAG+2LJ7l5Q4wOSIBmO7Y+wiL4v9P1GAv3EPU")

# Create an API objects with the above config object:
api = maproulette.Api(config)

# Specify the ID of the challenge you want up add tasks to:
challenge_id = '12974'

# Provide a GeoJSON of the task data:
with open('/Users/adamshaw/Downloads/Fields.geojson', 'r') as data_file:
    data = json.loads(data_file.read())

print(data)

# Printing response:
print(api.add_tasks_to_challenge(data, challenge_id, False, 'Test_Date'))