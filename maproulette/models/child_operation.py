import json
from .enums import Operations


class ChildOperationModel:

    @property
    def operation(self):
        """The operation to be applied to the OSM object ('setTags', 'deleteTags')"""
        return self._operation

    @operation.setter
    def operation(self, value):
        if value in Operations.list():
            self._operation = value
        else:
            raise ValueError(f"Operation must be one of {Operations.list()}.")

    @property
    def data(self):
        """Either a dict (key/value pair) of a tag/tags to be set in a 'setTags' operation, or an
        array of tag keys (as strings) to be deleted in a deleteTags operation"""
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def __init__(self, operation=None, data=None):
        self.operation = operation
        self.data = data

    def to_dict(self):
        properties = {
            "operation": self._operation,
            "data": self._data
        }
        return {k: v for (k, v) in properties.items() if v is not None}

    def to_json(self):
        """Converts all non-null properties of a child operation object into a JSON object"""
        return json.dumps(self.to_dict())
