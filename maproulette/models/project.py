"""This module contains the definition of a Project object in MapRoulette."""

import json
import os


class ProjectModel:
    """Definition for a MapRoulette Project"""

    READONLY = ["id"]

    @property
    def path(self):
        """The path to the project"""
        return os.path.join("project", str(self._id))

    @property
    def id(self):
        """The ID of the project"""
        return self._id

    @property
    def name(self):
        """The internal name of the project"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        """The description for the project"""
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def groups(self):
        """The groups that are associated with the project"""
        return self._groups

    @groups.setter
    def groups(self, value):
        self._description = value

    @property
    def enabled(self):
        """Whether this project is enabled for use or not"""
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value

    @property
    def display_name(self):
        """The friendly name that can be displayed to users"""
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value

    @property
    def is_virtual(self):
        """Whether or not a project is virtual"""
        return self._is_virtual

    @is_virtual.setter
    def is_virtual(self, value):
        self._is_virtual = value

    @property
    def featured(self):
        """Whether or not the project is featured"""
        return self._featured

    @featured.setter
    def featured(self, value):
        self._featured = value

    def __init__(self, name, id=None, description=None, groups=None, enabled=None,
                 is_virtual=None, display_name=None, featured=None):
        self._id = id
        self._name = name
        self._description = description
        self._groups = groups
        self._enabled = enabled
        self._display_name = display_name
        self._featured = featured
        self._is_virtual = is_virtual

    def to_dict(self):
        """Converts all non-null properties of a project object into a dictionary"""
        properties = {
            "id": self._id,
            "name": self._name,
            "description": self._description,
            "groups": self._groups,
            "enabled": self._enabled,
            "display_name": self._display_name,
            "featured": self._featured,
            "isVirtual": self._is_virtual
        }
        return {k: v for (k, v) in properties.items() if v is not None}

    def to_json(self):
        """Converts all non-null properties of a project object into a JSON object"""
        return json.dumps(self.to_dict())
