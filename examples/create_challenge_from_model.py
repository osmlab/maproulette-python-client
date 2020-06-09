import maproulette
import json

# Create a configuration object for MapRoulette using your API key:
config = maproulette.Configuration()

# Create an API objects with the above config object:
api = maproulette.Challenge(config)

# Creating a test challenge model with name and child task
challenge_data = maproulette.ChallengeModel(name='Test_Challenge_Name')

# Adding example description
challenge_data.description = "This is a test challenge"

# Adding required instruction
challenge_data.instruction = "Do something"

# Let's create a basic rule to classify features with tags 'highway' = 'footway' to be high priority
rule_1 = maproulette.PriorityRule(priority_value='highway.footway', priority_type='string', priority_operator='equal')

# Create a formal priority rule for the challenge
challenge_data.high_priority_rule = maproulette.PriorityRuleModel(condition='OR', rules=[rule_1]).to_json()

# Adding example overpass QL input for challenge
challenge_data.overpassQL = open('data/Example_OverpassQL_Query', 'r').read()

print(challenge_data.overpassQL)

# Create challenge
print(json.dumps(api.create_challenge(challenge_data)))
