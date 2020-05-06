import maproulette
import json

# Create a configuration object for MapRoulette using your API key:
config = maproulette.Configuration(api_key="API_KEY")

# Create an API objects with the above config object:
api = maproulette.Challenge(config)

# Creating a test challenge model with name and child task
challenge_data = maproulette.ChallengeModel(name='Test_Challenge_Name')

# Adding example description
challenge_data.description = "This is a test challenge"

# Adding required instruction
challenge_data.instruction = "Do something"

# Adding example overpass QL input for challenge
challenge_data.overpassQL = open('data/Example_OverpassQL_Query', 'r').read()

print(challenge_data.overpassQL)

# Create challenge
print(json.dumps(api.create_challenge(challenge_data)))
