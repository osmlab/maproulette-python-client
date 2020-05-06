"""This module contains the definition of a Challenge object in MapRoulette."""

import json
import os


class ChallengeModel:
    """Definition for a MapRoulette Challenge"""

    @property
    def path(self):
        """The path to the challenge"""
        return os.path.join("challenge", self._id)

    @property
    def id(self):
        """The ID of the challenge"""
        return self._id

    @property
    def name(self):
        """The internal name of the challenge"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        """The description for the challenge"""
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def parent(self):
        """The parent ID for the challenge"""
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def instruction(self):
        """The instruction for the challenge"""
        return self._instruction

    @instruction.setter
    def instruction(self, value):
        self._instruction = value

    @property
    def difficulty(self):
        """The difficulty setting for the challenge"""
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        self._difficulty = value

    @property
    def blurb(self):
        """The blurb for the challenge"""
        return self._blurb

    @blurb.setter
    def blurb(self, value):
        self._blurb = value

    @property
    def enabled(self):
        """Whether this challenge is enabled for use or not"""
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value

    @property
    def challenge_type(self):
        """The type for this challenge"""
        return self._challenge_type

    @challenge_type.setter
    def challenge_type(self, value):
        self._challenge_type = value

    @property
    def featured(self):
        """Whether or not this challenge is featured"""
        return self._featured

    @featured.setter
    def featured(self, value):
        self._featured = value

    @property
    def overpassQL(self):
        """The Overpass query for this challenge"""
        return self._overpassQL

    @overpassQL.setter
    def overpassQL(self, value):
        self._overpassQL = value

    @property
    def default_priority(self):
        """The default priority for this challenge"""
        return self._default_priority

    @default_priority.setter
    def default_priority(self, value):
        self._default_priority = value

    @property
    def default_zoom(self):
        """The default zoom level for this challenge"""
        return self._default_zoom

    @default_zoom.setter
    def default_zoom(self, value):
        self._default_zoom = value

    @property
    def min_zoom(self):
        """The minimum zoom level for this challenge"""
        return self._min_zoom

    @min_zoom.setter
    def min_zoom(self, value):
        self._min_zoom = value

    @property
    def max_zoom(self):
        """The maximum zoom level for this challenge"""
        return self._max_zoom

    @max_zoom.setter
    def max_zoom(self, value):
        self._max_zoom = value

    def __init__(self, name, id=None, description=None, parent=None, instruction=None, difficulty=None, blurb=None,
                 enabled=None, challenge_type=None, featured=None, overpassQL=None, default_priority=None, default_zoom=None,
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
        self._overpassQL = overpassQL
        self._default_priority = default_priority
        self._default_zoom = default_zoom
        self._min_zoom = min_zoom
        self._max_zoom = max_zoom

    def to_dict(self):
        """Converts all non-null properties of a challenge object into a dictionary"""
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
            "overpassQL": self._overpassQL,
            "defaultPriority": self._default_priority,
            "defaultZoom": self._default_zoom,
            "minZoom": self._min_zoom,
            "maxZoom": self._max_zoom
        }
        return {k: v for (k, v) in properties.items() if v is not None}

    def to_json(self):
        """Converts all non-null properties of a challenge object into a JSON object"""
        return json.dumps(self.to_dict())
