import json
from unittest.mock import ANY

import pytest
import requests
import responses
import urllib3
from gitlab.v4.objects import Project
from requests import PreparedRequest
from responses import BaseResponse

from modules import gl_wrapper
from gitlab._backends import requests_backend

from tests.doubles import stub_gitlab_api as doubles


def describe_wrapper_for_the_gitlab_api_library():
    """📂 wrapper for the gitlab api library"""

    def test_get_access_token_cfg():
        """🧪 should get the access token from the configuration file"""
        assert gl_wrapper.USER_TOKEN_FILE == ".gl_token.user"

    def test_get_access_token():
        """🧪 should get the access token"""
        expected_token = open(".gl_token.user", "r", encoding="UTF-8").read()
        assert gl_wrapper.access_token() == expected_token

    def test_init_gl_api():
        """🧪 should instantiate the gitlab api library"""
        fake_access_token = "fake_access_token"
        gl = gl_wrapper.init_gl_api(fake_access_token)
        assert gl is not None
        assert gl.user is None
        assert gl.url == "https://gitlab.com"
        assert gl.private_token == fake_access_token

    @responses.activate
    def should_be_authenticated_via_private_token():
        """🧪🎭 👍 🔒 should be authenticated via private token"""
        mock_gitlab_v4_api_user: BaseResponse = responses.add(doubles.stub_gitlab_api_v4_user)

        valid_access_token = gl_wrapper.access_token()
        gl = gl_wrapper.init_gl_api(valid_access_token)
        assert gl_wrapper.authenticate(gl) is True
        assert gl.private_token == valid_access_token
        assert gl.oauth_token is None
        assert gl.job_token is None

        # Code behavioral test to check how the GitLab API v4 is called trapping it into a responses spy
        assert mock_gitlab_v4_api_user.call_count == 1
        assert responses.calls[0].request.method == "GET"
        assert responses.calls[0].request.url == "https://gitlab.com/api/v4/user"
        assert responses.calls[0].request.headers["PRIVATE-TOKEN"] == valid_access_token

    @responses.activate
    def should_not_be_authenticated_via_a_wrong_private_token():
        """🧪🎭 👎 🔒 should NOT be authenticated via a WRONG private token"""
        mock_gitlab_v4_api_user_wrong_token: BaseResponse = responses.add(doubles.stub_gitlab_api_v4_user_wrong_token)

        invalid_private_token = "this_is_an_invalid_private_token"
        gl = gl_wrapper.init_gl_api(invalid_private_token)
        assert gl_wrapper.authenticate(gl) is False
        assert gl.private_token == invalid_private_token
        assert gl.oauth_token is None
        assert gl.job_token is None

        # Code behavioral test to check how the GitLab API v4 is called trapping it into a responses spy
        assert mock_gitlab_v4_api_user_wrong_token.call_count == 1
        assert responses.calls[0].request.method == "GET"
        assert responses.calls[0].request.url == "https://gitlab.com/api/v4/user"
        assert responses.calls[0].request.headers["PRIVATE-TOKEN"] == invalid_private_token
        assert responses.calls[0].response.json() == {"message": "401 Unauthorized"}

    @responses.activate
    def should_get_the_projects_list():
        """🧪🎭 👍 🗂️ should get the projects list"""
        _mock_gitlab_v4_api_user: BaseResponse = responses.add(doubles.stub_gitlab_api_v4_user)
        mock_gitlab_v4_api_project_valid_token: BaseResponse = responses.add(doubles.stub_gitlab_api_v4_projects)

        valid_access_token = gl_wrapper.access_token()
        gl = gl_wrapper.init_gl_api(valid_access_token)
        gl_wrapper.authenticate(gl)
        projects_list = gl_wrapper.get_projects(gl)
        assert isinstance(projects_list[0], Project)
        assert projects_list[0].id == 51708305
        assert projects_list[0].description == "description_for_test_search"

        # Code behavioral test to check how the GitLab API v4 is called trapping it into a responses spy
        assert mock_gitlab_v4_api_project_valid_token.call_count == 1
        assert responses.calls[1].request.method == "GET"
        assert responses.calls[1].request.url == "https://gitlab.com/api/v4/projects"
        assert responses.calls[1].request.headers["PRIVATE-TOKEN"] == valid_access_token
        assert "description_for_test_search" in responses.calls[1].response.json()[0]["description"]

    @responses.activate
    def should_not_get_the_projects_list_due_to_connection_error():
        """🧪🎭 👎 🗂️ should NOT get the projects due to connection error"""
        mock_gitlab_v4_api_projects_connection_error: BaseResponse = responses.add(
            doubles.stub_gitlab_api_v4_projects_connection_error
        )

        invalid_access_token = "invalid_token_trying_to_avoid_authentication"
        gl = gl_wrapper.init_gl_api(invalid_access_token)
        projects_list = gl_wrapper.get_projects(gl)
        assert projects_list is None

        # Code behavioral test to check how the GitLab API v4 is called trapping it into a responses spy
        assert mock_gitlab_v4_api_projects_connection_error.call_count == 1
        assert responses.calls[0].request.method == "GET"
        assert responses.calls[0].request.url == "https://gitlab.com/api/v4/projects"
        assert responses.calls[0].request.headers["PRIVATE-TOKEN"] == invalid_access_token

    @responses.activate
    def should_get_the_details_of_my_own_gitlab_project_with_real_id_51648656():
        """🧪🎭 👍 ℹ️ should get the details of my own GitLab project with real ID 51648656"""
        _mock_gitlab_v4_api_user: BaseResponse = responses.add(doubles.stub_gitlab_api_v4_user)
        mock_gitlab_v4_api_project_51648656: BaseResponse = responses.add(doubles.stub_gitlab_api_v4_project_51648656)

        my_gitlab_project_id = 51648656
        valid_access_token = gl_wrapper.access_token()
        gl = gl_wrapper.init_gl_api(valid_access_token)
        gl_wrapper.authenticate(gl)
        project_details = gl_wrapper.get_project_details(gl, project_id=my_gitlab_project_id)
        assert isinstance(project_details, Project)
        assert project_details.id == my_gitlab_project_id
        assert project_details.name == "GitLabAPI"
        assert project_details.description is None

        # Code behavioral test to check how the GitLab API v4 is called trapping it into a responses spy
        assert mock_gitlab_v4_api_project_51648656.call_count == 1
        assert responses.calls[1].request.method == "GET"
        assert responses.calls[1].request.url == f"https://gitlab.com/api/v4/projects/{my_gitlab_project_id}"
        assert responses.calls[1].request.headers["PRIVATE-TOKEN"] == valid_access_token

    @responses.activate
    def should_not_get_the_details_of_a_not_found_project():
        """🧪🎭 👎 ℹ️ should NOT get the details of a not found project"""
        _mock_gitlab_v4_api_user: BaseResponse = responses.add(doubles.stub_gitlab_api_v4_user)
        mock_gitlab_v4_api_project_doesnt_exists: BaseResponse = responses.add(
            doubles.stub_gitlab_api_v4_project_12345678
        )

        project_doesnt_exists = 12345678
        valid_access_token = gl_wrapper.access_token()
        gl = gl_wrapper.init_gl_api(valid_access_token)
        gl_wrapper.authenticate(gl)
        project_details = gl_wrapper.get_project_details(gl, project_id=project_doesnt_exists)
        assert project_details is None

        # Code behavioral test to check how the GitLab API v4 is called trapping it into a responses spy
        assert mock_gitlab_v4_api_project_doesnt_exists.call_count == 1
        assert responses.calls[1].request.method == "GET"
        assert responses.calls[1].request.url == f"https://gitlab.com/api/v4/projects/{project_doesnt_exists}"
        assert responses.calls[1].request.headers["PRIVATE-TOKEN"] == valid_access_token
