import maproulette
import json

# Create a configuration object for MapRoulette using your API key:
config = maproulette.Configuration(api_key="API_KEY")

# Create an API objects with the above config object:
api = maproulette.Task(config)

# To fetch a task, specify the task ID
task_id = '42914448'

# Printing response
print(json.dumps(api.get_task_by_id(task_id), indent=4, sort_keys=True))

# You can access a task's history:
print(json.dumps(api.get_task_history(task_id), indent=4, sort_keys=True))

# Or get a task's tags:
print(json.dumps(api.get_task_tags(task_id), indent=4, sort_keys=True))

# You can also fetch tasks by specifying a list of tags:
tags = 'tag1,tag2'
print(json.dumps(api.get_tasks_by_tags(tags), indent=4, sort_keys=True))
