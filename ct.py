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

from events import Events
from general import General
from persons import Persons
from services import Services
from songs import Songs
from status import Status

from typing import Any, Dict
import json
import requests
import traceback


class CT:

    __base_url = 'https://wetzlar.church.tools/api/'
    __debugging = 0
    __cookie = None

    def __init__(self, cookie: Dict[str, str] = None) -> None:
        """Initialize a CT object.

        The login cookie can look like this:

        .. code-block ::

            cookie = {
                'ChurchTools_ct_wetzlar': 'some_random_text',
            }

        :param cookie: The login cookie
        :type cookie: dict
        :returns: An initialized CT object
        :rtype: CT
        """

        if cookie:
            self.__cookie = cookie

        self.events = Events(self)
        self.general = General(self)
        self.persons = Persons(self)
        self.services = Services(self)
        self.songs = Songs(self)
        self.status = Status(self)

    def make_request(self, endpoint: str, params: Any = None,
                     binary: bool = False) -> Any:
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

        rurl = f'{self.__base_url}{endpoint}'

        if self.__debugging > 1:
            for line in traceback.format_stack():
                print(line.strip())

        if binary:
            return requests.get(rurl, params=params,
                                cookies=self.__cookie).content

        resp = requests.get(rurl, params=params, cookies=self.__cookie)
        rstr = resp.content.decode()

        r_ok = self.check_response(resp)
        if not r_ok:
            if self.__debugging > 0:
                print(rurl, '->', resp.status_code)
                print(rstr)

            return None

        robj = json.loads(rstr)

        if self.__debugging > 0:
            print(rurl, '->', resp.status_code)
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
            print('Error: 401 Unauthorized')
            return False
        if resp.status_code == 403:
            print('Error: 403 Forbidden')
            return False
        if resp.status_code == 404:
            print('Error: 404 Not Found')
            return False

        return True

    def login(self, email: str, password: str, login_url: str = None) -> None:
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
        """

        if not login_url:
            # TODO: generalize this
            login_url = 'https://wetzlar.church.tools/index.php?q=login/ajax'

        data = {
            'func': 'login',
            'email': email,
            'password': password,
        }
        response = requests.post(login_url, data=data)

        if not self.check_response(response):
            print('login unsuccessful')
            return

        if self.__debugging > 0:
            print('login successful')

        cookie = response.cookies.items()[0]
        self.__cookie = {cookie[0]: cookie[1]}

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
                'ChurchTools_ct_wetzlar': 'some_random_text',
            }

        :param cookie: The login cookie
        :type cookie: dict
        """

        self.__cookie = cookie
