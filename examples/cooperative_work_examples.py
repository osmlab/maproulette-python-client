import maproulette
import json
import base64

# Create a configuration object for MapRoulette using your API key:
config = maproulette.Configuration(api_key="API_KEY")

# Create an API objects with the above config object:
api = maproulette.Task(config)

# Setting a challenge ID in which we'll place our cooperative task
challenge_id = 14452

# We'll start by creating some 'child' operations to apply to the target objects add them to a list:
child_operations_list = [maproulette.ChildOperationModel(operation="setTags",
                                                         data={"test_tag_1": "True",
                                                               "test_tag_2": "True",
                                                               "test_tag_3": "True"}).to_dict(),
                         maproulette.ChildOperationModel(operation="setTags",
                                                         data={"test_tag_4": "True"}).to_dict(),
                         maproulette.ChildOperationModel(operation="setTags",
                                                         data={"test_tag_5": "True"}).to_dict()]

# Now we'll pass these operations into a 'parent' operation list to specify the objects to which the changes
# will be applied:
test_parent_relation = [maproulette.ParentOperationModel(operation_type="modifyElement",
                                                         element_type="way",
                                                         osm_id="175208404",
                                                         child_operations=child_operations_list).to_dict()]

# The below flags error when handling is in the constructor, but not when in the setter:
test_2 = maproulette.ParentOperationModel(operation_type="modifyElement",
                                element_type="way",
                                osm_id="175208404",
                                child_operations=child_operations_list)


# Now that we have a Parent Operation containing the Child Operations we'd like to implement, we
# can pass this into our Cooperative Work model:

test_cooperative_work = maproulette.CooperativeWorkModel(version=2,
                                                         type=1,
                                                         parent_operations=test_parent_relation).to_dict()

# Now we can create a basic task to apply these suggested changes to:
with open('data/Example_Geometry.geojson', 'r') as data_file:
    data = json.loads(data_file.read())

test_task = maproulette.TaskModel(name="Test_Coop_Task_Kastellet",
                                  parent=challenge_id,
                                  geometries=data,
                                  cooperative_work=test_cooperative_work).to_dict()


# Finally, we'll pass our task object to into the create_task method to call the /task
# endpoint, creating this new task with our cooperative work model applied
print(json.dumps(api.create_task(test_task), indent=4, sort_keys=True))


# Alternatively, cooperative work can be populated as in-progress edits via an OSM changefile (osc file)
# as 'type 2' cooperative work:
with open('data/ExampleChangefile.osc', 'rb') as data_file:
    osc_file = base64.b64encode(data_file.read()).decode('ascii')

test_osc_cooperative_work = maproulette.CooperativeWorkModel(type=2,
                                                             content=osc_file).to_dict()

test_osc_task = maproulette.TaskModel(name="Test_Coop_Task_Kastellet_OSC_2",
                                  parent=challenge_id,
                                  geometries=data,
                                  cooperative_work=test_osc_cooperative_work).to_dict()

print(json.dumps(api.create_task(test_osc_task), indent=4, sort_keys=True))

