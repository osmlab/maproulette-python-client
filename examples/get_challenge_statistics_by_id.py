import maproulette
import json

# Create a configuration object for MapRoulette using your API key:
config = maproulette.Configuration(api_key="API_KEY")

# Create an API objects with the above config object:
api = maproulette.Challenge(config)

# Specify the ID of the challenge you want up add tasks to:
challenge_id = 'TEST_ID'

# Printing response
print(json.dumps(api.get_challenge_statistics_by_id(challenge_id)))
