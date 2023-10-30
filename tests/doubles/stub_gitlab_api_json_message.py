import json

stub_gitlab_api_v4_user_json = json.loads(
    (
        "{"
        '"id": 18503717,'
        '"username": "project_51648656_bot_cf8fee5361c1f81143b20c1d38860e94",'
        '"name": "GitHub",'
        '"state": "active",'
        '"locked": false,'
        '"avatar_url": "https://secure.gravatar.com/avatar/0f6b9438a785de51cc940904f0294b91?s=80&d=identicon",'
        '"web_url": "https://gitlab.com/project_51648656_bot_cf8fee5361c1f81143b20c1d38860e94",'
        '"created_at": "2023-10-27T16:21:38.693Z",'
        '"bio": "",'
        '"location": "",'
        '"public_email": null,'
        '"skype": "",'
        '"linkedin": "",'
        '"twitter": "",'
        '"discord": "",'
        '"website_url": "",'
        '"organization": "",'
        '"job_title": "",'
        '"pronouns": null,'
        '"bot": true,'
        '"work_information": null,'
        '"local_time": null,'
        '"last_sign_in_at": null,'
        '"confirmed_at": "2023-10-27T16:21:38.667Z",'
        '"last_activity_on": "2023-10-27",'
        '"email": "project_51648656_bot_cf8fee5361c1f81143b20c1d38860e94@noreply.gitlab.com",'
        '"theme_id": 3,'
        '"color_scheme_id": 1,'
        '"projects_limit": 100000,'
        '"current_sign_in_at": null,'
        '"identities": [],'
        '"can_create_group": true,'
        '"can_create_project": true,'
        '"two_factor_enabled": false,'
        '"external": false,'
        '"private_profile": false,'
        '"commit_email": "project_51648656_bot_cf8fee5361c1f81143b20c1d38860e94@noreply.gitlab.com",'
        '"shared_runners_minutes_limit": null,'
        '"extra_shared_runners_minutes_limit": null,'
        '"scim_identities": []'
        "}"
    )
)


stub_gitlab_api_v4_401_unauthorized_json = json.loads('{"message": "401 Unauthorized"}')


stub_gitlab_api_v4_projects_json = json.loads(
    (
        "[{"
        '  "id": 51708305,'
        '  "description": "description_for_test_search",'
        '  "name": "ex02.20 - Medidas de um círculo",'
        '  "name_with_namespace": "Deitel Cpp Como Programar - 5ª edição / Capítulo 02 / Exercícios / ex02.20 - Medidas de um círculo",'
        '  "path": "ex02.20-medidas-de-um-circulo",'
        '  "path_with_namespace": "deitel-cpp-como-programar-5-edicao/capitulo-02/exercicios/ex02.20-medidas-de-um-circulo",'
        '  "created_at": "2023-10-30T10:54:23.427Z",'
        '  "default_branch": "main",'
        '  "tag_list": [],'
        '  "topics": [],'
        '  "ssh_url_to_repo": "git@gitlab.com:deitel-cpp-como-programar-5-edicao/capitulo-02/exercicios/ex02.20-medidas-de-um-circulo.git",'
        '  "http_url_to_repo": "https://gitlab.com/deitel-cpp-como-programar-5-edicao/capitulo-02/exercicios/ex02.20-medidas-de-um-circulo.git",'
        '  "web_url": "https://gitlab.com/deitel-cpp-como-programar-5-edicao/capitulo-02/exercicios/ex02.20-medidas-de-um-circulo",'
        '  "readme_url": "https://gitlab.com/deitel-cpp-como-programar-5-edicao/capitulo-02/exercicios/ex02.20-medidas-de-um-circulo/-/blob/main/README.md",'
        '  "forks_count": 0,'
        '  "avatar_url": null,'
        '  "star_count": 0,'
        '  "last_activity_at": "2023-10-30T10:54:23.427Z",'
        '  "namespace": {'
        '      "id": 76920210,'
        '      "name": "Exercícios",'
        '      "path": "exercicios",'
        '      "kind": "group",'
        '      "full_path": "deitel-cpp-como-programar-5-edicao/capitulo-02/exercicios",'
        '      "parent_id": 76634432,'
        '      "avatar_url": null,'
        '      "web_url": "https://gitlab.com/groups/deitel-cpp-como-programar-5-edicao/capitulo-02/exercicios"'
        "}"
        "},"
        "{"
        '  "id": 51708266,'
        '  "description": null,'
        '  "name": "News Bulletin",'
        '  "name_with_namespace": "vanshika baghel / News Bulletin",'
        '  "path": "news-bulletin",'
        '  "path_with_namespace": "baghel2/news-bulletin",'
        '  "created_at": "2023-10-30T10:53:01.657Z",'
        '  "default_branch": "main",'
        '  "tag_list": [],'
        '  "topics": [],'
        '  "ssh_url_to_repo": "git@gitlab.com:baghel2/news-bulletin.git",'
        '  "http_url_to_repo": "https://gitlab.com/baghel2/news-bulletin.git",'
        '  "web_url": "https://gitlab.com/baghel2/news-bulletin",'
        '  "readme_url": "https://gitlab.com/baghel2/news-bulletin/-/blob/main/README.md",'
        '  "forks_count": 0,'
        '  "avatar_url": null,'
        '  "star_count": 0,'
        '  "last_activity_at": "2023-10-30T10:53:01.657Z",'
        '  "namespace": {'
        '      "id": 66272390,'
        '      "name": "vanshika baghel",'
        '      "path": "baghel2",'
        '      "kind": "user",'
        '      "full_path": "baghel2",'
        '      "parent_id": null,'
        '      "avatar_url": "/uploads/-/system/user/avatar/14274097/avatar.png",'
        '      "web_url": "https://gitlab.com/baghel2"'
        "  }"
        "}]"
    )
)
