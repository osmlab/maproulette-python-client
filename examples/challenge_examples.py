import maproulette
import json

# Create a configuration object for MapRoulette using your API key:
config = maproulette.Configuration(api_key="API_KEY")

# Create an API objects with the above config object:
api = maproulette.Challenge(config)

# Fetching a challenge based on challenge ID is easy. Specify the ID of the challenge you want:
challenge_id = '12974'

# Printing response
print(json.dumps(api.get_challenge_by_id(challenge_id), indent=4, sort_keys=True))

# We can also access a challenge by specifying the parent project ID and the challenge name:
challenge_name = 'Test_Challenge'
project_id = '2491'
print(json.dumps(api.get_challenge_by_name(project_id=project_id,
                                           challenge_name=challenge_name), indent=4, sort_keys=True))

# We can access challenge statistics as well:
print(json.dumps(api.get_challenge_statistics_by_id(challenge_id)))

# Accessing a challenge's tasks is easy too. Specify the ID of the challenge you want:
print(json.dumps(api.get_challenge_tasks(challenge_id), indent=4, sort_keys=True))

# In order to create a new challenge, we can make our lives easier by using the Challenge Model
challenge_data = maproulette.ChallengeModel(name='Test_Challenge_Name')

# Adding example description
challenge_data.description = "This is a test challenge"

# Adding required instruction
challenge_data.instruction = "Do something"

# Let's create a basic rule to classify features with tags 'highway' = 'footway' to be high priority
rule_1 = maproulette.PriorityRule(priority_value='highway.footway',
                                  priority_type=maproulette.priority_rule.Types.STRING,
                                  priority_operator=maproulette.priority_rule.StringOperators.EQUAL)

# Create a formal priority rule for the challenge
challenge_data.high_priority_rule = maproulette.PriorityRuleModel(condition=maproulette.priority_rule.Conditions.OR,
                                                                  rules=rule_1
                                                                  ).to_json()

# Adding example overpass QL input for challenge
challenge_data.overpassQL = open('data/Example_OverpassQL_Query', 'r').read()

# Create challenge
print(json.dumps(api.create_challenge(challenge_data)))

# If we want to add tasks to an existing challenge we can specify the challenge ID:
challenge_id = 'TEST_ID'

# Provide a GeoJSON of the task data:
with open('data/Example_Geometry.geojson', 'r') as data_file:
    data = json.loads(data_file.read())

# Printing response:
print(json.dumps(api.add_tasks_to_challenge(data, challenge_id)))
