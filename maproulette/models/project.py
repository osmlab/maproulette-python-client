"""
This module contains the definition of a Project object in MapRoulette.
"""

import json
import os


class ProjectModel:
    """
    Definition for a MapRoulette Project
    """

    READONLY = ["id"]

    @property
    def path(self):
        return os.path.join("project", str(self._id))

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def groups(self):
        return self._groups

    @groups.setter
    def groups(self, value):
        self._description = value

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value

    @property
    def is_virtual(self):
        return self._is_virtual

    @is_virtual.setter
    def is_virtual(self, value):
        self._is_virtual = value

    def __init__(self, name, id=None, description=None, groups=None, enabled=None, display_name=None, is_virtual=None):
        self._id = id
        self._name = name
        self._description = description
        self._groups = groups
        self._enabled = enabled
        self._display_name = display_name
        self._is_virtual = is_virtual

    def to_dict(self):
        properties = {
            "id": self._id,
            "name": self._name,
            "description": self._description,
            "groups": self._groups,
            "enabled": self._enabled,
            "display_name": self._display_name,
            "is_virtual": self._is_virtual
        }
        return {k: v for (k, v) in properties.items() if v is not None}

    def to_json(self):
        return json.dumps(self.to_dict())
