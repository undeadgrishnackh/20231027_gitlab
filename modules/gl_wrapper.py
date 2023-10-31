import gitlab
from gitlab.v4.objects import Project


USER_TOKEN_FILE = ".gl_token.user"


def access_token() -> str:
    return open(USER_TOKEN_FILE, "r", encoding="UTF-8").read()


def init_gl_api(token: str) -> gitlab.Gitlab:
    return gitlab.Gitlab(url="https://gitlab.com", private_token=token)


def authenticate(git_lab: gitlab.Gitlab) -> bool:
    try:
        git_lab.auth()
        return True
    except gitlab.exceptions.GitlabAuthenticationError as exception:
        print("😱 Authentication error")
        print(exception.response_body)
        return False


def get_projects(git_lab: gitlab.Gitlab) -> [Project]:
    try:
        return git_lab.projects.list()
    # pylint: disable=W0718
    except Exception as exception:
        print("😱 Fatal Exception")
        print(exception)
        return None


def get_project_details(git_lab: gitlab.Gitlab, project_id: int) -> Project | None:
    try:
        return git_lab.projects.get(project_id)
    # pylint: disable=W0718
    except Exception as exception:
        print("😱 Fatal Exception")
        print(exception)
        return None
