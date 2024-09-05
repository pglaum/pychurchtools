from __future__ import annotations

import os

from churchtools import ChurchTools


def get_env_or_die(env_name):
    res = os.getenv(env_name)
    if not res:
        print(f"${env_name} is not set")
        exit(1)

    return res


def get_ct_client() -> ChurchTools:
    ct_url = get_env_or_die("CHURCHTOOLS_URL")
    ct_user = get_env_or_die("CHURCHTOOLS_USER")
    ct_password = get_env_or_die("CHURCHTOOLS_PASSWORD")

    ct = ChurchTools(ct_url)
    ct.login(ct_user, ct_password)

    return ct
