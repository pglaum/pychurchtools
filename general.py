"""
General
=======

Endpoints of general purpose.

"""

from ct_types import Person, VersionInfo


class General:

    def __init__(self, CT):

        self.CT = CT

    def info(self):
        """Information about the API.

        The API envoles and dependes on the ChurchTools version.
        This endpoint provides the build version and CT version.
        """

        res = self.CT.make_request('info')
        return VersionInfo(**res)

    def whoami(self):
        """Currently logged in user.

        This endpoint returns the current user.
        If the request is unauthorized, the anonymous user (aka public user)
        is returned.

        .. note:: In the API there is a parameter defined
            (only_allow_authenticated). We ignore this, as it has no use here.
        """

        res = self.CT.make_request('whoami')
        return Person(**res['data'])

    def test_route(self, route):
        """Test an arbitrary route.
        """

        res = self.CT.make_request(route)
        return res
