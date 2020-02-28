"""
This module contains the definition of a Challenge object in MapRoulette.
"""

import json
import os


class ChallengeModel:
    """
    Definition for a MapRoulette Challenge
    """

    @property
    def path(self):
        return os.path.join("challenge", self._id)

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
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def instruction(self):
        return self._instruction

    @instruction.setter
    def instruction(self, value):
        self._instruction = value

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        self._difficulty = value

    @property
    def blurb(self):
        return self._blurb

    @blurb.setter
    def blurb(self, value):
        self._blurb = value

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value

    @property
    def challenge_type(self):
        return self._challenge_type

    @challenge_type.setter
    def challenge_type(self, value):
        self._challenge_type = value

    @property
    def featured(self):
        return self._featured

    @featured.setter
    def featured(self, value):
        self._featured = value

    @property
    def default_priority(self):
        return self._default_priority

    @default_priority.setter
    def default_priority(self, value):
        self._default_priority = value

    @property
    def default_zoom(self):
        return self._default_zoom

    @default_zoom.setter
    def default_zoom(self, value):
        self._default_zoom = value

    @property
    def min_zoom(self):
        return self._min_zoom

    @min_zoom.setter
    def min_zoom(self, value):
        self._min_zoom = value

    @property
    def max_zoom(self):
        return self._max_zoom

    @max_zoom.setter
    def max_zoom(self, value):
        self._max_zoom = value

    def __init__(self, name, id=None, description=None, parent=None, instruction=None, difficulty=None, blurb=None,
                 enabled=None, challenge_type=None, featured=None, default_priority=None, default_zoom=None,
                 min_zoom=None, max_zoom=None):
        self._id = id
        self._name = name
        self._description = description
        self._parent = parent
        self._instruction = instruction
        self._difficulty = difficulty
        self._blurb = blurb
        self._enabled = enabled
        self._challenge_type = challenge_type
        self._featured = featured
        self._default_priority = default_priority
        self._default_zoom = default_zoom
        self._min_zoom = min_zoom
        self._max_zoom = max_zoom

    def to_dict(self):
        properties = {
            "id": self._id,
            "name": self._name,
            "description": self._description,
            "parent": self._parent,
            "instruction": self._instruction,
            "difficulty": self._difficulty,
            "blurb": self._blurb,
            "enabled": self._enabled,
            "challengeType": self._challenge_type,
            "featured": self._featured,
            "defaultPriority": self._default_priority,
            "defaultZoom": self._default_zoom,
            "minZoom": self._min_zoom,
            "maxZoom": self._max_zoom
        }
        return {k: v for (k, v) in properties.items() if v is not None}

    def to_json(self):
        return json.dumps(self.to_dict())
