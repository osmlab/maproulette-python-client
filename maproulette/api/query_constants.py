"""
This module holds string constants to be used in conjunction with API calls to MapRoulette.
"""

# Query string parameters
QUERY_PARAMETER_Q = "q="
QUERY_PARAMETER_PARENT_IDENTIFIER = "parentId="
QUERY_PARAMETER_LIMIT = "limit="
QUERY_PARAMETER_PAGE = "page="
QUERY_PARAMETER_ONLY_ENABLED = "onlyEnabled="
# Common URIs
API_VERSION = "/api/v2"
URI_FIND = "s/find?"
# Project URIs
URI_PROJECT_GET_BY_NAME = API_VERSION + "/projectByName/%s"
URI_PROJECT_BASE = API_VERSION + "/project/%s"
URI_PROJECT_POST = API_VERSION + "/project"
URI_PROJECT_FIND = URI_PROJECT_POST + URI_FIND
URI_PROJECT_CHILDREN = URI_PROJECT_BASE + "/children"
# Challenge URIs
URI_CHALLENGES = URI_PROJECT_BASE + "/challenges"
URI_CHALLENGE_GET_BY_NAME = API_VERSION + "/project/%d/challenge/%s"
URI_CHALLENGE_BASE = API_VERSION + "/challenge/%s"
URI_CHALLENGE_POST = API_VERSION + "/challenge"
URI_CHALLENGE_FIND = URI_CHALLENGE_POST + URI_FIND
URI_CHALLENGE_CHILDREN = URI_CHALLENGE_BASE + "/tasks"
# Task URIs
URI_TASK_GET_BY_NAME = API_VERSION + "/challenge/%d/task/%s"
URI_TASK_BASE = API_VERSION + "/task/%s"
URI_TASK_POST = API_VERSION + "/task"
URI_TASK_FIND = URI_TASK_POST + URI_FIND
# Flags
FLAG_IMMEDIATE_DELETE = "immediate"
