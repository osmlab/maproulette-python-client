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
    def high_priority_rule(self):
        """The high priority for this challenge"""
        return self._high_priority_rule

    @high_priority_rule.setter
    def high_priority_rule(self, value):
        self._high_priority_rule = value

    @property
    def medium_priority_rule(self):
        """The medium priority for this challenge"""
        return self._medium_priority_rule

    @medium_priority_rule.setter
    def high_priority_rule(self, value):
        self._medium_priority_rule = value

    @property
    def low_priority_rule(self):
        """The low priority of this challenge"""
        return self._low_priority_rule

    @low_priority_rule.setter
    def low_priority_rule(self, value):
        self._low_priority_rule = value

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

    @property
    def osm_id_property(self):
        """The id property of an osm feature"""
        return self._osm_id_property

    @osm_id_property.setter
    def osm_id_property(self, value):
        self._osm_id_property = value

    @property
    def cooperative_type(self):
        """"""
        return self._cooperative_type

    @cooperative_type.setter
    def cooperative_type(self, value):
        self._cooperative_type = value

    @property
    def popularity(self):
        """The popularity of a challenge"""
        return self._popularity

    @popularity.setter
    def popularity(self, value):
        self._popularity = value

    @property
    def check_in_comment(self):
        """Comment to be associated with changes made by users"""
        return self._check_in_comment

    @check_in_comment.setter
    def check_in_comment(self, value):
        self._check_in_comment = value

    @property
    def check_in_source(self):
        """Hashtag appended to changeset comments"""
        return self._check_in_source

    @check_in_source.setter
    def check_in_source(self, value):
        self._check_in_source = value

    @property
    def requires_local(self):
        """Whether or not tasks require local knowledge to complete"""
        return self._requires_local

    @requires_local.setter
    def requires_local(self, value):
        self._requires_local = value

    @property
    def default_basemap(self):
        """The default basemap to use for this challenge"""
        return self._default_basemap

    @default_basemap.setter
    def default_basemap(self, value):
        self._default_basemap = value

    @property
    def default_basemap_id(self):
        """The id of the default basemap"""
        return self._default_basemap_id

    @default_basemap_id.setter
    def default_basemap_id(self, value):
        self._default_basemap_id = value

    @property
    def custom_basemap(self):
        """The custom basemap of this challenge"""
        return self._custom_basemap

    @custom_basemap.setter
    def custom_basemap(self, value):
        self._custom_basemap = value

    @property
    def update_tasks(self):
        """Whether or not to periodically delete old tasks"""
        return self._update_tasks

    @update_tasks.setter
    def update_tasks(self, value):
        self._update_tasks = value

    @property
    def exportable_properties(self):
        """Comma separated list of properties to be exportable"""
        return self._exportable_properties

    @exportable_properties.setter
    def exportable_properties(self, value):
        self._exportable_properties = value

    @property
    def preferred_tags(self):
        """List of preferred tags the user can use when completing tasks"""
        return self._preferred_tags

    @preferred_tags.setter
    def preferred_tags(self, value):
        self._preferred_tags = value

    @property
    def task_styles(self):
        """Custom task styling based on specific task feature properties"""
        return self._task_styles

    @task_styles.setter
    def task_styles(self, value):
        self._task_styles = value

    @property
    def remote_geojson(self):
        """Create a challenge from a GeoJSON URL"""
        return self._remote_geojson

    @remote_geojson.setter
    def remote_geojson(self, value):
        self._remote_geojson = value

    def __init__(self, name, id=None, description=None, parent=None, instruction=None, difficulty=None, blurb=None,
                 enabled=None, challenge_type=None, featured=None, overpassQL=None, default_priority=None,
                 high_priority_rule=None, medium_priority_rule=None, low_priority_rule=None, default_zoom=None, min_zoom=None, max_zoom=None,
                 osm_id_property=None, cooperative_type=None, popularity=None, check_in_comment=None,
                 check_in_source=None, requires_local=None, default_basemap=None, default_basemap_id=None,
                 custom_basemap=None, update_tasks=None, exportable_properties=None, preferred_tags=None,
                 task_styles=None, remote_geojson=None):
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
        self._high_priority_rule = high_priority_rule
        self._medium_priority_rule = medium_priority_rule
        self._low_priority_rule = low_priority_rule
        self._default_zoom = default_zoom
        self._min_zoom = min_zoom
        self._max_zoom = max_zoom
        self._osm_id_property = osm_id_property
        self._cooperative_type = cooperative_type
        self._popularity = popularity
        self._check_in_comment = check_in_comment
        self._check_in_source = check_in_source
        self._requires_local = requires_local
        self._default_basemap = default_basemap
        self._default_basemap_id = default_basemap_id
        self._custom_basemap = custom_basemap
        self._update_tasks = update_tasks
        self._exportable_properties = exportable_properties
        self._preferred_tags = preferred_tags
        self._task_styles = task_styles
        self._remote_geojson = remote_geojson

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
            "highPriorityRule": self._high_priority_rule,
            "mediumPriorityRule": self._medium_priority_rule,
            "lowPriorityRule": self._low_priority_rule,
            "defaultZoom": self._default_zoom,
            "minZoom": self._min_zoom,
            "maxZoom": self._max_zoom,
            "osmIdProperty": self._osm_id_property,
            "cooperativeType": self._cooperative_type,
            "popularity": self._popularity,
            "checkInComment": self._check_in_comment,
            "checkInSource": self._check_in_source,
            "requiresLocal": self._requires_local,
            "defaultBasemap": self._default_basemap,
            "defautlBasemapId": self._default_basemap_id,
            "customBasemap": self._custom_basemap,
            "updateTasks": self._update_tasks,
            "exportableProperties": self._exportable_properties,
            "preferredTags": self._preferred_tags,
            "taskStyles": self._task_styles,
            "remoteGeoJson": self.remote_geojson
        }
        return {k: v for (k, v) in properties.items() if v is not None}

    def to_json(self):
        """Converts all non-null properties of a challenge object into a JSON object"""
        return json.dumps(self.to_dict())
