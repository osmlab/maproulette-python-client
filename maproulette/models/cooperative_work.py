import json

"""This module contains the definition of a Cooperative Work object in MapRoulette."""


class CooperativeWorkModel:
    """Definition for a Cooperative Work object"""

    @property
    def version(self):
        """"""
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def type(self):
        """"""
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def parent_operations(self):
        """"""
        return self.parent_operations

    @parent_operations.setter
    def parent_operations(self, value):
        self._parent_operations = value

    @property
    def content(self):
        """"""
        return self.content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def file_type(self):
        """"""
        return self.file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value

    @property
    def file_format(self):
        """"""
        return self.file_format

    @file_format.setter
    def file_format(self, value):
        self._file_format = value

    @property
    def encoding(self):
        """"""
        return self.encoding

    @encoding.setter
    def encoding(self, value):
        self._encoding = value

    # file_type, file_format, and encoding defaults are set because they are the only values currently
    # supported for cooperative work model type 2

    def __init__(self, version=None, type=None, parent_operations=None, file_type="xml", file_format="osc",
                 encoding="base64", content=None):
        self.version = version
        self.type = type
        self.parent_operations = parent_operations
        self.file_type = file_type
        self.file_format = file_format
        self.encoding = encoding
        self.content = content


    def to_dict(self):
        properties = {"meta": {
                    "version": self._version,
                    "type": self._type},
                    "file": {
                        "type": self._file_type,
                        "format": self._file_format,
                        "encoding": self._encoding,
                        "content": self._content},
                    "operations": self._parent_operations}

        return {k: v for (k, v) in properties.items() if v is not None}


    def to_json(self):
        """Converts all non-null properties of a task object into a JSON object"""
        return json.dumps(self.to_dict())
