import responses

from tests.doubles import stub_gitlab_api_json_message as doubles

user_api_url = "https://gitlab.com/api/v4/user"
projects_api_url = "https://gitlab.com/api/v4/projects"


stub_gitlab_api_v4_user = responses.Response(
    method="GET", url=user_api_url, json=doubles.stub_gitlab_api_v4_user_json, status=200
)

stub_gitlab_api_v4_user_wrong_token = responses.Response(
    method="GET", url=user_api_url, json=doubles.stub_gitlab_api_v4_401_unauthorized_json, status=401
)


stub_gitlab_api_v4_projects = responses.Response(
    method="GET", url=projects_api_url, json=doubles.stub_gitlab_api_v4_projects_json, status=200
)

stub_gitlab_api_v4_projects_connection_error = responses.Response(
    method="GET",
    url=projects_api_url,
    body=Exception("Fake Connection Error Exception"),
)
