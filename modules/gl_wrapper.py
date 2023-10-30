import gitlab


def print_the_title():
    print("😊 Welcome to Dummy Kata")


def access_token() -> str:
    return open(".gl_token", "r", encoding="UTF-8").read()


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


def get_projects(git_lab: gitlab.Gitlab) -> bool:
    try:
        git_lab.projects.list(iterator=True)
        return True
    # pylint: disable=W0718
    except Exception as exception:
        print("😱 Fatal Exception")
        print(exception)
        return False
