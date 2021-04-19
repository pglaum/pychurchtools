from events import Events
from general import General
from persons import Persons
from services import Services
from songs import Songs
from status import Status

from typing import Any
import json
import requests
import traceback


class CT:

    base_url = 'https://wetzlar.church.tools/api/'
    debugging = 0
    cookie = None

    def __init__(self, cookie=None):

        if cookie:
            self.cookie = cookie

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

        rurl = f'{self.base_url}{endpoint}'

        if self.debugging > 1:
            for line in traceback.format_stack():
                print(line.strip())

        if binary:
            return requests.get(rurl, params=params,
                                cookies=self.cookie).content

        resp = requests.get(rurl, params=params, cookies=self.cookie)
        rstr = resp.content.decode()

        r_ok = self.check_response(resp)
        if not r_ok:
            if self.debugging > 0:
                print(rurl, '->', resp.status_code)
                print(rstr)

            return None

        robj = json.loads(rstr)

        # if 'data' in robj:
        #     robj = robj['data']

        if self.debugging > 0:
            print(rurl, '->', resp.status_code)
            print(rstr)
            print()

        return robj

    def check_response(self, resp):

        # rstr = resp.content.decode()

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

    def login(self, email, password):
        """Login to the ChurchTools API.

        BE CAREFUL what you do with your passwords!
        """

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

        if self.debugging > 0:
            print('login successful')

        cookie = response.cookies.items()[0]
        self.cookie = {cookie[0]: cookie[1]}
