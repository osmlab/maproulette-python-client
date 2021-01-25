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


class OSMObjects(ExtendedEnum):
    """An enumeration of valid OSM object types"""
    WAY = "way"
    NODE = "node"
    RELATION = "relation"


class OperationTypes(ExtendedEnum):
    """An enumeration of valid operation types"""
    CREATE_ELEMENT = "createElement"
    DELETE_ELEMENT = "deleteElement"
    MODIFY_ELEMENT = "modifyElement"


class Operations(ExtendedEnum):
    """An enumeration of valid operations"""
    SET_TAGS = "setTags"
    UNSET_TAGS = "unsetTags"


class CooperativeWorkTypes(ExtendedEnum):
    """An enumeration of valid cooperative work types"""
    TYPE_ONE = 1
    TYPE_TWO = 2
