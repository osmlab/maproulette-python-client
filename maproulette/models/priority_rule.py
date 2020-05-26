"""This module contains the definition of a priority rule object in MapRoulette."""

import json
import os

VALID_TYPES = {'string', 'integer', 'double', 'long', 'nested rule'}


class PriorityRuleModel:
    """Definition for a MapRoulette priority rule"""

    @property
    def priority_value(self):
        """The value for the priority rule"""
        return self._priority_value

    @priority_value.setter
    def priority_value(self, value):
        self._priority_value = value

    @property
    def priority_type(self):
        """The type for the priority rule"""
        return self._priority_type

    @priority_type.setter
    def priority_type(self, value):
        if value not in VALID_TYPES:
            raise ValueError("Priority type must be one of %s.", VALID_TYPES)
        self._priority_type = value

    @property
    def priority_operator(self):
        """The type for the priority rule"""
        return self._priority_operator

    @priority_operator.setter
    def priority_operator(self, value):
        self._priority_operator = value

    def __init__(self, priority_value, priority_type, priority_operator):
        self._priority_value = priority_value
        self._priority_type = priority_type
        self._priority_operator = priority_operator

    def to_dict(self):
        """Converts all non-null properties of a project object into a dictionary"""
        return {
            "value": self._priority_value,
            "type": self._priority_type,
            "operator": self._priority_operator
        }

    def to_json(self):
        """Converts all non-null properties of a project object into a JSON object"""
        return json.dumps(self.to_dict())
