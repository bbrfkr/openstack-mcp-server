import os
from keystoneauth1 import session
from keystoneauth1.identity import v3


def get_keystone_session():
    password = v3.PasswordMethod(
        username=os.getenv("OS_USERNAME"),
        password=os.getenv("OS_PASSWORD"),
        user_domain_name=os.getenv("OS_USER_DOMAIN_NAME"),
    )
    auth = v3.Auth(
        auth_url=os.getenv("OS_AUTH_URL"),
        auth_methods=[password],
        project_name=os.getenv("OS_PROJECT_NAME"),
        project_domain_name=os.getenv("OS_PROJECT_DOMAIN_NAME"),
    )
    sess = session.Session(auth=auth)
    return sess
