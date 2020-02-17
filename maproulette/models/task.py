"""
This module contains the definition of a Task object in MapRoulette.
"""

import os


class TaskModel:
    """
    Definition for a MapRoulette Task
    """
    READONLY = ["id"]

    @property
    def path(self):
        return os.path.join("task", str(self._id))

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
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def geometries(self):
        return self._geometries

    @geometries.setter
    def geometries(self, value):
        self._geometries = value

    @property
    def instruction(self):
        return self._instruction

    @instruction.setter
    def instruction(self, value):
        self._instruction = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def suggested_fix(self):
        return self._suggested_fix

    @suggested_fix.setter
    def suggested_fix(self, value):
        self._suggested_fix = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def mapped_on(self):
        return self._mapped_on

    @mapped_on.setter
    def mapped_on(self, value):
        self._mapped_on = value

    @property
    def review(self):
        return self._review

    @review.setter
    def review(self, value):
        self._review = value

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value

    @property
    def changeset_id(self):
        return self._changeset_id

    @changeset_id.setter
    def changeset_id(self, value):
        self._changeset_id = value

    @property
    def completion_responses(self):
        return self._completion_responses

    @completion_responses.setter
    def completion_responses(self, value):
        self._completion_responses = value

    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value

    @property
    def is_bundle_primary(self):
        return self._is_bundle_primary

    @is_bundle_primary.setter
    def is_bundle_primary(self, value):
        self._is_bundle_primary = value

    @property
    def mapillary_images(self):
        return self._mapillary_images

    @mapillary_images.setter
    def mapillary_images(self, value):
        self._mapillary_images = value

    def __init__(self, name, parent, geometries, id=None, instruction=None, location=None, suggested_fix=None,
                 status=None, mapped_on=None, review=None, priority=None, changeset_id=None, completion_responses=None,
                 bundle_id=None, is_bundle_primary=None, mapillary_images=None):
        self._id = id
        self._name = name
        self._parent = parent
        self._geometries = geometries
        self._instruction = instruction
        self._location = location
        self._suggested_fix = suggested_fix
        self._status = status
        self._mapped_on = mapped_on
        self._review = review
        self._priority = priority
        self._changeset_id = changeset_id
        self._completion_responses = completion_responses
        self._bundle_id = bundle_id
        self._is_bundle_primary = is_bundle_primary
        self._mapillary_images = mapillary_images

    def to_json(self):
        properties = {
            "id": self._id,
            "name": self._name,
            "parent": self._parent,
            "instruction": self._instruction,
            "location": self._location,
            "suggestedFix": self._suggested_fix,
            "status": self._status,
            "mappedOn": self._mapped_on,
            "review": self._review,
            "priority": self._priority,
            "changesetId": self._changeset_id,
            "completionResponses": self._completion_responses,
            "bundleId": self._bundle_id,
            "isBundlePrimary": self._is_bundle_primary,
            "mapillaryImages": self._mapillary_images
        }
        return {k: v for (k, v) in properties.items() if v is not None}
