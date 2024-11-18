"""
pychurchtools
=============

This is the entrypoint for the ChurchTools API.

Currently, only `GET`-type methods are implemented (-> read-only).
In the future, maybe `POST`, `DELETE`, etc. may also be of interest.

TODO (for 100% completion):

    - Absence
    - Admin
    - Calendar
    - Campus
    - Checkin
    - Chat
    - Contact Label
    - Field
    - File
    - Finance
    - Groups
    - GroupHomepage
    - Job
    - Masterdata
    - Permission
    - Resource
    - Sync
    - Tag
    - Translation
    - Queue
    - Widgets

"""

from __future__ import annotations

import json
import traceback
from typing import Any
from urllib.parse import urljoin

import requests  # type: ignore

from churchtools.admin import Admin
from churchtools.calendars import Calendars
from churchtools.departments import Departments
from churchtools.events import Events
from churchtools.general import General
from churchtools.group_homepages import GroupHomepages
from churchtools.groups import Groups
from churchtools.persons import Persons
from churchtools.resource import Resources
from churchtools.services import Services
from churchtools.songs import Songs
from churchtools.status import Status
from churchtools.wiki import Wiki


class ChurchTools:
    __base_url = ""
    __debugging = 0
    __cookie = None

    def __init__(self, base_url: str, cookie: dict[str, str] | None = None) -> None:
        """Initialize a CT object.

        The login cookie can look like this:

        .. code-block ::

            cookie = {
                'ChurchTools_ct_<church_name>': 'some_random_text',
            }

        :param base_url: Set the base_url to the API. It typically looks like
            this: https://<church_name>.church.tools/api/
        :type base_url: str
        :param cookie: The login cookie
        :type cookie: dict
        :returns: An initialized CT object
        :rtype: CT
        """

        self.__base_url = base_url
        if cookie:
            self.__cookie = cookie
        else:
            self.__cookie = None

        self.admin = Admin(self)
        self.calendars = Calendars(self)
        self.departments = Departments(self)
        self.events = Events(self)
        self.general = General(self)
        self.groups = Groups(self)
        self.group_homepages = GroupHomepages(self)
        self.persons = Persons(self)
        self.resources = Resources(self)
        self.services = Services(self)
        self.songs = Songs(self)
        self.status = Status(self)
        self.wiki = Wiki(self)

    def make_request(
        self,
        endpoint: str,
        params: Any | None = None,
        binary: bool = False,
        method: str = "get",
        data: Any | None = None,
        return_status_code: bool = False,
    ) -> Any:
        """Make a request to the churchtools API.

        :param endpoint: The url endpoint (excluding base_url), that is called.
        :type endpoint: str
        :param params: Parameters that are to be sent along
        :type params: list, dict, or str
        :param binary: Return the binary answer.
        :type binary: bool
        :param method: The http request method
        :type method: str
        :type return_status_code: Only return status code
        :param return_status_code: bool
        :returns: The result of the request
        :rtype: binary, dict, or string
        """

        # TODO: implement lists in params (e.g. ids for songs.list())

        rurl = urljoin(self.__base_url, "api/") + endpoint

        if self.__debugging > 1:
            print("request to:", rurl)
            for line in traceback.format_stack():
                print(line.strip())

        param_str = "?"
        if isinstance(params, dict):
            for key, value in params.items():
                if isinstance(value, list):
                    for item in value:
                        param_str += f"{key}[]={item}&"
                else:
                    param_str += f"{key}={value}&"

        if param_str[-1] == "&":
            param_str = param_str[:-1]

        if binary:
            return requests.get(rurl, params=params, cookies=self.__cookie).content

        if method == "post":
            resp = requests.post(rurl, params=params, json=data, cookies=self.__cookie)
        elif method == "put":
            resp = requests.put(rurl, params=params, json=data, cookies=self.__cookie)
        elif method == "patch":
            resp = requests.patch(rurl, params=params, json=data, cookies=self.__cookie)
        elif method == "delete":
            resp = requests.delete(rurl, params=params, cookies=self.__cookie)
        else:
            if param_str:
                resp = requests.get(rurl + param_str, cookies=self.__cookie)
            else:
                resp = requests.get(rurl, params=params, cookies=self.__cookie)

        if return_status_code:
            if self.__debugging > 0:
                print(rurl, "->", resp.status_code)
                print(params, "->", param_str)
                if resp.content:
                    print(resp.content.decode())
            return resp.status_code

        rstr = resp.content.decode()

        r_ok = self.check_response(resp)
        if not r_ok:
            if self.__debugging > 0:
                print(rurl, "->", resp.status_code)
                print(params, "->", param_str)
                print(rstr)

            return None

        if self.__debugging > 0:
            print(rurl, "->", resp.status_code)
            print(params, "->", param_str)
            print(rstr)
            print()

        robj = json.loads(rstr)
        return robj

    def check_response(self, resp: requests.models.Response) -> bool:
        """Check a response for errors.

        :param resp: The API response
        :type resp: requsts.models.Response
        :returns: Status of the response (successful/not successful)
        :rtype: bool
        """

        if resp.status_code == 400:
            if self.__debugging > 0:
                print("Error: 400 No Authorization")
            return False
        if resp.status_code == 401:
            if self.__debugging > 0:
                print("Error: 401 Unauthorized")
            return False
        if resp.status_code == 403:
            if self.__debugging > 0:
                print("Error: 403 Forbidden")
            return False
        if resp.status_code == 404:
            if self.__debugging > 0:
                print("Error: 404 Not Found")
            return False

        if resp.status_code == 503:
            if self.__debugging > 0:
                print("Error: 503 Service Unavailable")
            return False

        return True

    def login(self, username: str, password: str, remember_me: bool = False) -> bool:
        """Login to the ChurchTools API.

        The login cookie is saved to the CT object.

        BE CAREFUL what you do with your passwords!

        :param username: The user name for the ChurchTools login
        :type username: str
        :param password: Password for the ChurchTools login
        :type password: str
        :returns: Success
        :rtype: bool
        """

        rurl = urljoin(self.__base_url, "api/login")

        params: dict[str, Any] = {}
        params["password"] = password
        params["username"] = username
        params["rememberMe"] = remember_me
        response = requests.post(rurl, data=params, cookies=self.__cookie)

        if not self.check_response(response):
            if self.__debugging > 0:
                print("login unsuccessful")
            return False

        if self.__debugging > 0:
            print("login successful")

        cookie = response.cookies.items()[0]
        self.__cookie = {cookie[0]: cookie[1]}

        return True

    def logout(self) -> bool:
        """Logs out the current user and destroys the associated session

        :returns: Logout success
        :rtype: bool
        """

        res = self.make_request("logout", method="post", return_status_code=True)

        if res == 204:
            self.__cookie = None
            return True

        return False

    def is_authenticated(self) -> bool:
        """Check if the current object is authenticated with curchtools.

        :returns: If the object is authenticated
        :rtype: bool
        """

        # check if no cookie is set
        if not self.__cookie:
            return False

        # check if the user is 'anonymous'
        i_am = self.general.whoami()
        if not i_am or not i_am.id or i_am.id < 0:
            return False

        return True

    def set_base_url(self, base_url: str) -> None:
        """Set the base URL.

        The URL has to point to a churchtools instance.

        :param base_url: The new base_url
        :type base_url: str
        """

        self.__base_url = base_url

    def set_debugging_level(self, level: int) -> None:
        """Set the debug level.

        0: No debugging messages, only error message
        1: Some debugging messages, including full ChurchTools response
        2: Very many debugging messages, including stacktrace for every
           API query

        :param level: The debug level (0 - 2)
        :type level: int
        """

        self.__debugging = level

    def set_login_cookie(self, cookie: dict) -> None:
        """Set the login cookie.

        This cookie will be sent with every API query.
        Alternatively, you can login using func:`CT.login()`, where the cookie
        is set automatically

        Example:

        .. code-block ::

            cookie = {
                'ChurchTools_ct_<church_name>': 'some_random_text',
            }

        :param cookie: The login cookie
        :type cookie: dict
        """

        self.__cookie = cookie

    def get_login_cookie(self) -> dict | None:
        """Get the login cookie.

        :returns: the login cookie
        :rtype: dict
        """

        return self.__cookie
