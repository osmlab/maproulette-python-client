import json


class ChildOperationModel:

    @property
    def operation(self):
        """"""
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value

    @property
    def data(self):
        """"""
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def __init__(self, operation=None, data=None):
        self._operation = operation
        self._data = data


    def to_dict(self):
        properties = {
            "operation": self._operation,
            "data": self._data
        }
        return {k: v for (k, v) in properties.items() if v is not None}

    def to_json(self):
        """Converts all non-null properties of a task object into a JSON object"""
        return json.dumps(self.to_dict())
