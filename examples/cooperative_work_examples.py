import maproulette
import json
import base64

# Create a configuration object for MapRoulette using your API key:
config = maproulette.Configuration(api_key="2450|wB+DfON5nZ1p8cclrgtILUaPHtuJAG+2LJ7l5Q4wOSIBmO7Y+wiL4v9P1GAv3EPU")

# Create an API objects with the above config object:
api = maproulette.Task(config)

# Setting a challenge ID in which we'll place our cooperative task
challenge_id = "14452"

# We'll start by creating some 'child' operations to apply to the target objects add them to a list:
child_operations_list = [maproulette.ChildOperationModel(operation="setTags",
                                                        data={"test_tag_1": "True"}).to_dict(),
                        maproulette.ChildOperationModel(operation="setTags",
                                                        data={"test_tag_2": "True"}).to_dict(),
                        maproulette.ChildOperationModel(operation="setTags",
                                                        data={"test_tag_3": "True"}).to_dict()]

print(str(child_operations_list))
print(type(str(child_operations_list)))

# Now we'll pass these operations into a 'parent' operation list to specify the objects to which the changes
# will be applied:
test_parent_relation = [maproulette.ParentOperationModel(operation_type="modifyElement",
                                                        element_type="way",
                                                        osm_id="31110737",
                                                        child_operations=child_operations_list).to_dict()]

print(test_parent_relation)
print(type(test_parent_relation))


# Now we can create a basic task to apply these suggested changes to:
with open('data/Example_Geometry.geojson', 'r') as data_file:
    data = json.loads(data_file.read())

test_task = maproulette.TaskModel(name="Test_Coop_Task_Type_1_2",
                                  parent=14452,
                                  geometries=data,
                                  version=2,
                                  type=1,
                                  parent_operations=test_parent_relation).to_dict()


# Finally, we'll pass our task object to into the create_task method to call the /task
# endpoint, creating this new task with our cooperative work model applied
print(json.dumps(api.create_task(test_task), indent=4, sort_keys=True))


# We can also utilize 'type 2' cooperative work, which allow the changes to be passed
# in via an osc file rather than explicitly specifying tag operations in the request
# body:
osc_test_file = #pending

osc_test_file_encoded = base64.encodebytes(bytes(osc_test_file, 'utf-8'))

test_task = maproulette.TaskModel(name="Test_Coop_Task_Type_3",
                                  parent=14452,
                                  geometries=data,
                                  version=2,
                                  type=2,
                                  content=osc_test_file_encoded).to_dict()

print(json.dumps(api.create_task(test_task), indent=4, sort_keys=True))
