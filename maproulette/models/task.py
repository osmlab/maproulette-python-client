"""This module contains the definition of a Task object in MapRoulette."""

import json
import os


class TaskModel:
    """Definition for a MapRoulette Task"""
    READONLY = ["id"]

    @property
    def path(self):
        """The path to the task"""
        return os.path.join("task", str(self._id))

    @property
    def id(self):
        """The ID of the task"""
        return self._id

    @property
    def name(self):
        """The internal name of the task"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def parent(self):
        """The parent ID for the task"""
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def geometries(self):
        """The geometries of the task"""
        return self._geometries

    @geometries.setter
    def geometries(self, value):
        self._geometries = value

    @property
    def instruction(self):
        """The instruction for the task"""
        return self._instruction

    @instruction.setter
    def instruction(self, value):
        self._instruction = value

    @property
    def location(self):
        """The location of the task"""
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def suggested_fix(self):
        """The suggested fix for the task"""
        return self._suggested_fix

    @suggested_fix.setter
    def suggested_fix(self, value):
        self._suggested_fix = value

    @property
    def status(self):
        """The status of the task"""
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def mapped_on(self):
        """The mapped on date for the task"""
        return self._mapped_on

    @mapped_on.setter
    def mapped_on(self, value):
        self._mapped_on = value

    @property
    def review(self):
        """Whether this task needs to be reviewed or not"""
        return self._review

    @review.setter
    def review(self, value):
        self._review = value

    @property
    def priority(self):
        """The priority of this task"""
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value

    @property
    def changeset_id(self):
        """The changeset ID for this task"""
        return self._changeset_id

    @changeset_id.setter
    def changeset_id(self, value):
        self._changeset_id = value

    @property
    def completion_responses(self):
        """The completion response for this task"""
        return self._completion_responses

    @completion_responses.setter
    def completion_responses(self, value):
        self._completion_responses = value

    @property
    def bundle_id(self):
        """The bundle ID for this task"""
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value

    @property
    def is_bundle_primary(self):
        """Whether or not this task is the bundle primary"""
        return self._is_bundle_primary

    @is_bundle_primary.setter
    def is_bundle_primary(self, value):
        self._is_bundle_primary = value

    @property
    def mapillary_images(self):
        """The mapillary images for this task"""
        return self._mapillary_images

    @mapillary_images.setter
    def mapillary_images(self, value):
        self._mapillary_images = value

    @property
    def cooperative_work(self):
        """A tag that is or will be used for a new type of task resolution"""
        return self._cooperative_work

    @cooperative_work.setter
    def cooperative_work(self, value):
        self._cooperative_work = value

    def __init__(self, name, parent, geometries, id=None, instruction=None, location=None, suggested_fix=None,
                 status=None, mapped_on=None, review=None, priority=None, changeset_id=None,
                 completion_responses=None, bundle_id=None, is_bundle_primary=None, mapillary_images=None,
                 cooperative_work=None):
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
        self._cooperative_work = cooperative_work

    def to_dict(self):
        """Converts all non-null properties of a task object into a dictionary"""
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
            "mapillaryImages": self._mapillary_images,
            "cooperativeWork": self._cooperative_work
        }
        return {k: v for (k, v) in properties.items() if v is not None}

    def to_json(self):
        """Converts all non-null properties of a task object into a JSON object"""
        return json.dumps(self.to_dict())
