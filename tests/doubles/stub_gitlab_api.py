import responses

from tests.doubles import stub_gitlab_api_json_message as doubles

user_api_url = "https://gitlab.com/api/v4/user"
projects_api_url = "https://gitlab.com/api/v4/projects"
my_project_id = 51648656
project_doesnt_exists = 12345678


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

stub_gitlab_api_v4_project_51648656 = responses.Response(
    method="GET",
    url=f"{projects_api_url}/{my_project_id}",
    json=doubles.stub_gitlab_api_v4_project_51648656_json,
    status=200,
)


stub_gitlab_api_v4_project_12345678 = responses.Response(
    method="GET",
    url=f"{projects_api_url}/{project_doesnt_exists}",
    json=doubles.stub_gitlab_api_v4_project_12345678_json,
    status=404,
)
