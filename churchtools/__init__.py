"""
pychurchtools
=============

This is the entrypoint for the ChurchTools API.

Currently, only `GET`-type methods are implemented (-> read-only).
In the future, maybe `POST`, `DELETE`, etc. may also be of interest.

TODO (primary):

    - groups

TODO (for 100% completion):

    - publicgroups
    - campus
    - fields
    - tags
    - departments
    - admin
    - calendar
    - masterdata
    - translations
    - finance
    - queue
    - permissions
    - sync
    - checkin
    - absence
    - files
    - chat
    - contactlabels
    - jobs

"""

from churchtools.events import Events
from churchtools.general import General
from churchtools.persons import Persons
from churchtools.services import Services
from churchtools.songs import Songs
from churchtools.status import Status
from churchtools.wiki import Wiki

from typing import Any, Dict
from urllib.parse import urljoin
import json
import requests
import traceback


class CT:

    __base_url = ""
    __debugging = 0
    __cookie = None

    def __init__(self, base_url: str, cookie: Dict[str, str] = None) -> None:
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

        self.events = Events(self)
        self.general = General(self)
        self.persons = Persons(self)
        self.services = Services(self)
        self.songs = Songs(self)
        self.status = Status(self)
        self.wiki = Wiki(self)

    def make_request(
        self, endpoint: str, params: Any = None, binary: bool = False
    ) -> Any:
        """Make a request to the churchtools API.

        :param endpoint: The url endpoint (excluding base_url), that is called.
        :type endpoint: str
        :param params: Parameters that are to be sent along
        :type params: list, dict, or str
        :param binary: Return the binary answer.
        :type binary: bool
        :returns: The result of the request
        :rtype: binary, dict, or string
        """

        # TODO: implement lists in params (e.g. ids for songs.list())

        rurl = urljoin(self.__base_url, "api/") + endpoint

        if self.__debugging > 1:
            print("request to:", rurl)
            for line in traceback.format_stack():
                print(line.strip())

        if binary:
            return requests.get(rurl, params=params, cookies=self.__cookie).content

        resp = requests.get(rurl, params=params, cookies=self.__cookie)
        rstr = resp.content.decode()

        r_ok = self.check_response(resp)
        if not r_ok:
            if self.__debugging > 0:
                print(rurl, "->", resp.status_code)
                print(rstr)

            return None

        robj = json.loads(rstr)

        if self.__debugging > 0:
            print(rurl, "->", resp.status_code)
            print(rstr)
            print()

        return robj

    def check_response(self, resp: requests.models.Response) -> bool:
        """Check a response for errors.

        :param resp: The API response
        :type resp: requsts.models.Response
        :returns: Status of the response (successful/not successful)
        :rtype: bool
        """

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

        return True

    def login(self, email: str, password: str, login_url: str = None) -> bool:
        """Login to the ChurchTools API.

        The login cookie is saved to the CT object.

        BE CAREFUL what you do with your passwords!

        :param email: Email address for the ChurchTools login
        :type email: str
        :param password: Password for the ChurchTools login
        :type password: str
        :param login_url: The URL to the AJAX function.
            This parameter typically ends in: `/index.php?q=login/ajax`
        :type login_url: str
        :returns: Success
        :rtype: bool
        """

        if not login_url:
            login_url = urljoin(self.__base_url, "/index.php?q=login/ajax")

        data = {
            "func": "login",
            "email": email,
            "password": password,
        }
        response = requests.post(login_url, data=data)

        if not self.check_response(response):
            if self.__debugging > 0:
                print("login unsuccessful")
            return False

        if self.__debugging > 0:
            print("login successful")

        cookie = response.cookies.items()[0]
        self.__cookie = {cookie[0]: cookie[1]}

        return True

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
        if i_am.id < 0:
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

    def get_login_cookie(self) -> dict:
        """Get the login cookie.

        :returns: the login cookie
        :rtype: dict
        """

        return self.__cookie
