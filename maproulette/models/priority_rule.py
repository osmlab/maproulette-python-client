"""This module contains the definition of a priority rule object in MapRoulette."""

import json
from enum import Enum, auto


class ExtendedEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    @classmethod
    def list(cls):
        return [i.value for i in cls]


class Conditions(ExtendedEnum):
    """An enumeration of valid logical conditions for a priority rule object"""
    OR = "OR"
    AND = "AND"


class Types(ExtendedEnum):
    """An enumeration of valid types for a priority rule object"""
    STRING = auto()
    INTEGER = auto()
    DOUBLE = auto()
    LONG = auto()


class StringOperators(ExtendedEnum):
    """An enumeration of valid string operators for a priority rule object"""
    EQUAL = auto()
    NOT_EQUAL = auto()
    CONTAINS = auto()
    NOT_CONTAINS = auto()
    IS_EMPTY = auto()
    IS_NOT_EMPTY = auto()


class NumericOperators(ExtendedEnum):
    """An enumeration of valid numeric operators for a priority rule object"""
    EQUAL_TO = "=="
    NOT_EQUAL_TO = "!="
    LESS_THAN = "<"
    LESS_THAN_OR_EQUAL = "<="
    GREATER_THAN = ">"
    GREATER_THAN_OR_EQUAL = ">="


class PriorityRuleModel:
    """A model for a priority rule definition in MapRoulette.

    :param condition: the logical condition to use to string together multiple rules. The valid options for conditions
        are defined by the :class:`~maproulette.models.priority_rule.Conditions` enum.
    :type condition: Conditions or str
    :param rules: one or more rules to use for the priority rule definition. Rules should be instances of the
        :class:`~maproulette.models.priority_rule.PriorityRule` class.
    :type rules: PriorityRule or list
    """

    @property
    def condition(self):
        """The condition to use to chain together multiple priority rules"""
        return self._condition

    @condition.setter
    def condition(self, value):
        if isinstance(value, Conditions):
            self._condition = value.value
        else:
            if value not in Conditions.list():
                raise ValueError(f"Priority condition must be one of {Conditions.list()}.")
            self._condition = value

    @property
    def rules(self):
        """The list of priority rules to be used in the priority rule model"""
        return self._rules

    @rules.setter
    def rules(self, value):
        self._rules = value

    def __init__(self, condition, rules):
        """The constructor for the PriorityRuleModel class"""
        self.condition = condition
        self.rules = list()
        if isinstance(rules, list):
            if len(rules) > 0:
                for i in rules:
                    if isinstance(i, PriorityRule):
                        self.rules.append(i.to_dict())
                    else:
                        raise ValueError("Rules must be PriorityRule instances")
            else:
                ValueError("Rule list cannot be empty")
        elif isinstance(rules, PriorityRule):
            self.rules.append(rules.to_dict())
        else:
            raise ValueError("Rules must be PriorityRule instances")

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
    """Definition for a single priority rule

    :param priority_type: the data type for the priority rule. The valid options are defined by the
        :class:`~maproulette.models.priority_rule.Types` enum.
    :type priority_type: Types or str
    :param priority_operator: the operator to use for the priority rule. The valid options for string-type priority
        rules are defined by the :class:`~maproulette.models.priority_rule.StringOperators` enum and the valid options
        for numeric-type priority rules are defined by the :class:`~maproulette.models.priority_rule.NumericOperators`
        enum.
    :type priority_operator: NumericOperators or StringOperators or str
    :param priority_value: the value to use for the priority rule. This should be formatted like 'highway.footway' to
        indicate that any task with a 'highway' property equal to 'footway' should be considered for this rule. Multiple
        values can be specified using commas. Example: 'highway.footway,pedestrian'.
    :type priority_value: str
    """

    @property
    def priority_type(self):
        """The type for the priority rule"""
        return self._priority_type

    @priority_type.setter
    def priority_type(self, value):
        if isinstance(value, Types):
            self._priority_type = value.value
        elif value in Types.list():
            self._priority_type = value
        else:
            raise ValueError(f"Priority types must be one of {Types.list()}.")

    @property
    def priority_operator(self):
        """The operator to use for the priority rule"""
        return self._priority_operator

    @priority_operator.setter
    def priority_operator(self, value):
        if self._priority_type == 'string':
            if isinstance(value, StringOperators):
                self._priority_operator = value.value
            elif value in StringOperators.list():
                self._priority_operator = value
            else:
                raise ValueError(f"String type priority operators must be one of {StringOperators.list()}.")
        else:
            if isinstance(value, NumericOperators):
                self._priority_operator = value.value
            elif value in NumericOperators.list():
                self._priority_operator = value
            else:
                raise ValueError(f"Numeric type priority operators must be one of {NumericOperators.list()}.")

    @property
    def priority_value(self):
        """The value for the priority rule"""
        return self._priority_value

    @priority_value.setter
    def priority_value(self, value):
        self._priority_value = value

    def __init__(self, priority_type, priority_operator, priority_value):
        """The constructor for the PriorityRule class"""
        self.priority_type = priority_type
        self.priority_operator = priority_operator
        self.priority_value = priority_value

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
