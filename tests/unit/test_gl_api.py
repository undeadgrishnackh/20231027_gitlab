import json
from unittest.mock import ANY

import pytest
import requests
import responses
import urllib3
from gitlab.v4.objects import Project
from requests import PreparedRequest

from modules import gl_wrapper
from gitlab._backends import requests_backend

from tests.doubles import stub_gitlab_api as doubles


def describe_wrapper_for_the_gitlab_api_library():
    """📂 wrapper for the gitlab api library"""

    def test_get_access_token():
        """🧪 should get the access token"""
        expected_token = open(".gl_token", "r").read()
        assert gl_wrapper.access_token() == expected_token

    def test_init_gl_api(mocker):
        """🧪 should instantiate the gitlab api library"""
        fake_access_token = "fake_access_token"
        gl = gl_wrapper.init_gl_api(fake_access_token)
        assert gl is not None
        assert gl.user is None
        assert gl.url == "https://gitlab.com"
        assert gl.private_token == fake_access_token

    @responses.activate
    def should_be_authenticated_via_private_token():
        """🧪🎭 👍 🔑 should be authenticated via private token"""
        mock_gitlab_v4_api_user = responses.add(doubles.stub_gitlab_api_v4_user)

        valid_access_token = gl_wrapper.access_token()
        gl = gl_wrapper.init_gl_api(valid_access_token)
        assert gl_wrapper.authenticate(gl) is True
        assert gl.private_token == valid_access_token
        assert gl.oauth_token is None
        assert gl.job_token is None

        assert mock_gitlab_v4_api_user.call_count == 1
        assert responses.calls[0].request.method == "GET"
        assert responses.calls[0].request.url == "https://gitlab.com/api/v4/user"
        assert responses.calls[0].request.headers["PRIVATE-TOKEN"] == valid_access_token

    @responses.activate
    def should_not_be_authenticated_via_a_wrong_private_token(mocker, capsys):
        """🧪🎭 👎 🔒 should NOT be authenticated via a WRONG private token"""
        mock_gitlab_v4_api_user_wrong_token = responses.add(doubles.stub_gitlab_api_v4_user_wrong_token)

        invalid_private_token = "this_is_an_invalid_private_token"
        gl = gl_wrapper.init_gl_api(invalid_private_token)

        assert gl_wrapper.authenticate(gl) is False
        assert gl.private_token == invalid_private_token
        assert gl.oauth_token is None
        assert gl.job_token is None

        assert mock_gitlab_v4_api_user_wrong_token.call_count == 1
        assert responses.calls[0].request.method == "GET"
        assert responses.calls[0].request.url == "https://gitlab.com/api/v4/user"
        assert responses.calls[0].request.headers["PRIVATE-TOKEN"] == invalid_private_token
        assert responses.calls[0].response.json() == {"message": "401 Unauthorized"}

    @responses.activate
    def should_get_the_projects_list():
        """🧪🎭 👍 🗂️ should get the projects list"""
        mock_gitlab_v4_api_user = responses.add(doubles.stub_gitlab_api_v4_user)
        mock_gitlab_v4_api_project_valid_token = responses.add(doubles.stub_gitlab_api_v4_projects)

        valid_access_token = gl_wrapper.access_token()
        gl = gl_wrapper.init_gl_api(valid_access_token)
        gl_wrapper.authenticate(gl)
        get_projects_list = gl_wrapper.get_projects(gl)

        assert get_projects_list is True
        assert responses.calls[1].request.method == "GET"
        assert responses.calls[1].request.url == "https://gitlab.com/api/v4/projects"
        assert responses.calls[1].request.headers["PRIVATE-TOKEN"] == valid_access_token
        assert "description_for_test_search" in responses.calls[1].response.json()[0]["description"]

    @responses.activate
    def should_not_get_the_projects_list_due_to_connection_error():
        """🧪🎭 👎 🗂️ should NOT get the projects due to connection error"""
        mock_gitlab_v4_api_project_valid_token = responses.add(doubles.stub_gitlab_api_v4_projects_connection_error)

        invalid_access_token = "invalid_token_trying_to_avoid_authentication"
        gl = gl_wrapper.init_gl_api(invalid_access_token)
        get_projects_list = gl_wrapper.get_projects(gl)

        assert get_projects_list is False
        assert responses.calls[0].request.method == "GET"
        assert responses.calls[0].request.url == "https://gitlab.com/api/v4/projects"
        assert responses.calls[0].request.headers["PRIVATE-TOKEN"] == invalid_access_token


# def describe_spike_on_worldwide_time_api():
#     """📂 spike on worldwide time api"""
#
#     @responses.activate
#     def should_get_the_time_from_the_ww_api(mocker):
#         """🧪🎭 should get the time from the WW api"""
#         stub_response_worldwide_time_api_at_21_46_14 = responses.Response(
#             method="GET",
#             url='https://worldtimeapi.org/api/timezone/Europe/Paris',
#             json=json.loads('{"abbreviation":"CEST","client_ip":"45.156.113.16","datetime":"2023-10-27T21:46:14.764773+02:00","day_of_week":5,"day_of_year":300,"dst":true,"dst_from":"2023-03-26T01:00:00+00:00","dst_offset":3600,"dst_until":"2023-10-29T01:00:00+00:00","raw_offset":3600,"timezone":"Europe/Rome","unixtime":1698435974,"utc_datetime":"2023-10-27T19:46:14.764773+00:00","utc_offset":"+02:00","week_number":43}')
#         )
#         spy_worldwide_time_api = responses.add(stub_response_worldwide_time_api_at_21_46_14)
#
#         assert gl_wrapper.get_time_wwapi() == '21:46:14'
#         assert spy_worldwide_time_api.call_count == 1
