import json
from .enums import OSMObjects, OperationTypes


class ParentOperationModel:

    @property
    def operation_type(self):
        """The operation type to be applied to the OSM object ('createElement', 'modifyElement', 'deleteElement')"""
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        if value in OperationTypes.list():
            self._operation_type = value
        else:
            raise ValueError(f"Operation type must be one of {OperationTypes.list()}.")

    @property
    def element_type(self):
        """The element type of the object to which the operation is applied ('way', 'node', 'relation')"""
        return self._element_type

    @element_type.setter
    def element_type(self, value):
        if value in OSMObjects.list():
            self._element_type = value
        else:
            raise ValueError(f"Element type must be one of {OSMObjects.list()}.")

    @property
    def osm_id(self):
        """The OSM ID of the object to which the operation is applied"""
        return self._osm_id

    @osm_id.setter
    def osm_id(self, value):
        if value.isnumeric():
            self._osm_id = value
        else:
            raise ValueError("OSM ID value must be a numeric OSM ID")

    @property
    def child_operations(self):
        """The set of operations that will be applied according to the operation type and
        object specified in the parent relation"""
        return self.child_operations

    @child_operations.setter
    def child_operations(self, value):
        self._child_operations = value

    def __init__(self, operation_type=None, element_type=None, osm_id=None, child_operations=None):
        self.operation_type = operation_type
        self.element_type = element_type
        self.osm_id = osm_id
        self.child_operations = child_operations

    def to_dict(self):
        properties = {
            "operationType": self._operation_type,
            "data": {
                "id": f"{self._element_type}/{self._osm_id}",
                "operations": self._child_operations
            }

        }
        return {k: v for (k, v) in properties.items() if v is not None}

    def to_json(self):
        """Converts all non-null properties of a task object into a JSON object"""
        return json.dumps(self.to_dict())
