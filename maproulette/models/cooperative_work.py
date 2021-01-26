import json
from .enums import CooperativeWorkTypes

"""This module contains the definition of a Cooperative Work object in MapRoulette."""


class CooperativeWorkModel:
    """Definition for a Cooperative Work object"""

    @property
    def version(self):
        """The version of maproulette cooperative work format to be processed
        (currently, only version 2 is supported)"""
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def type(self):
        """The type of cooperative work operation (either 1 for tag fix or 2 for change file)
        to be contained in the model"""
        return self._type

    @type.setter
    def type(self, value):
        if value in CooperativeWorkTypes.list():
            self._type = value
        else:
            raise ValueError(f"Cooperative work type must be one of {CooperativeWorkTypes.list()}.")

    @property
    def parent_operations(self):
        """A dict containing parent operation details which follows the parent_operation model"""
        return self.parent_operations

    @parent_operations.setter
    def parent_operations(self, value):
        self._parent_operations = value

    @property
    def content(self):
        """A base64-encoded osc changefile to be used in type 2 cooperative work operations"""
        return self.content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def file_type(self):
        """The type of changefile to be used in type 2 cooperative work
        (currently, only xml files are supported"""
        return self.file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value

    @property
    def file_format(self):
        """The format of changefile to be used in type 2 cooperative work
        (currently, only osc files are supported"""
        return self.file_format

    @file_format.setter
    def file_format(self, value):
        self._file_format = value

    @property
    def encoding(self):
        """The type of encoding used in the changefile for type 2 cooperative work
        (currently, only base64 encoding is supported)"""
        return self.encoding

    @encoding.setter
    def encoding(self, value):
        self._encoding = value

    # file_type, file_format, and encoding defaults are set because they are the only values currently
    # supported for cooperative work model type 2. The version default is included as the currently
    # used format version.

    def __init__(self, version=2, type=None, parent_operations=None, file_type="xml", file_format="osc",
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
