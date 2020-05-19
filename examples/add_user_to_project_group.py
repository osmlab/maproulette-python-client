import maproulette
import json

# Create a configuration object using a url and API key
config = maproulette.Configuration(api_key='{YOUR_API_KEY}')

# Create an API object using your config object
api = maproulette.User(config)

# Specify the user ID to grant privileges to
user_id = '{SOME_USER_ID}'

# Specify the project ID to update the privileges for
project_id = '{YOUR_PROJECT_ID}'

# Specify what level of access you want to grant this user (1 - Admin, 2 - Write, 3 - Read)
group = '2'

# Print the API response
print(json.dumps(api.add_user_to_project_group(user_id=user_id,
                                               project_id=project_id,
                                               group_type=group), indent=4, sort_keys=True))
