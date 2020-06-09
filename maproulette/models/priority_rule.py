"""This module contains the definition of a priority rule object in MapRoulette."""

import json

VALID_CONDITIONS = {'OR', 'AND'}
VALID_TYPES = {'string', 'integer', 'double', 'long'}
VALID_STRING_OPERATORS = {'equal', 'not_equal', 'contains', 'not_contains', 'is_empty', 'is_not_empty'}
VALID_NUMERIC_OPERATORS = {'==', '!=', '<', '<=', '>', '>='}


class PriorityRuleModel:
    """Definition for a MapRoulette priority rule"""

    @property
    def condition(self):
        """The condition (AND/OR) to use to chain together multiple priority rules"""
        return self._condition

    @condition.setter
    def condition(self, value):
        if value not in VALID_CONDITIONS:
            raise ValueError(f"Priority condition must be one of {VALID_CONDITIONS}.")
        self._condition = value

    @property
    def rules(self):
        """The list of priority rules to be used in the priority rule model"""
        return self._rules

    @rules.setter
    def rules(self, value):
        self._rules = value

    def __init__(self, condition, rules):
        self.condition = condition
        self.rules = list()
        if isinstance(rules, list):
            for i in rules:
                if isinstance(i, PriorityRule):
                    self.rules.append(i.to_dict())
                else:
                    raise ValueError("Rules must be PriorityRule instances")
        elif isinstance(rules, PriorityRule):
            self.rules.append(rules.to_dict())
        else:
            raise ValueError("Rules must PriorityRule instances")

    def to_dict(self):
        """Converts all properties of a priority rule model object into a dictionary"""
        return {
            "condition": self._condition,
            "rules": self._rules
        }

    def to_json(self):
        """Converts all properties of a priority rule model object into a JSON object"""
        return json.dumps(self.to_dict())


class PriorityRule:
    """Definition for a single priority rule"""

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
            raise ValueError(f"Priority type must be one of {VALID_TYPES}.")
        self._priority_type = value

    @property
    def priority_operator(self):
        """The type for the priority rule"""
        return self._priority_operator

    @priority_operator.setter
    def priority_operator(self, value):
        if self.priority_type == 'string':
            if value not in VALID_STRING_OPERATORS:
                raise ValueError(f"Priority operator must be one of {VALID_STRING_OPERATORS}.")
        else:
            if value not in VALID_NUMERIC_OPERATORS:
                raise ValueError(f"Priority operator must be one of {VALID_NUMERIC_OPERATORS}.")
        self._priority_operator = value

    def __init__(self, priority_value=None, priority_type=None, priority_operator=None):
        self._priority_value = priority_value
        self._priority_type = priority_type
        self._priority_operator = priority_operator

    def to_dict(self):
        """Converts all properties of a priority rule object into a dictionary"""
        return {
            "value": self._priority_value,
            "type": self._priority_type,
            "operator": self._priority_operator
        }

    def to_json(self):
        """Converts all properties of a priority rule object into a JSON object"""
        return json.dumps(self.to_dict())
