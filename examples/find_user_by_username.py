import maproulette
import json

# Create a configuration object using a url and API key
config = maproulette.Configuration(api_key='{YOUR_API_KEY}')

# Create an API object using your config object
api = maproulette.User(config)

# We want to fetch a user with a particular name
username = '{YOUR_USERNAME}'

# Print the API response
print(json.dumps(api.find_user_by_username(username), indent=4, sort_keys=True))
