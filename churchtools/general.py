"""
General
=======

Endpoints of general purpose.

"""

from churchtools.ct_types import Person, VersionInfo
from typing import Any


class General:
    def __init__(self, ct: Any) -> None:
        """Initialize a General object."""

        self.__ct = ct

    def info(self) -> VersionInfo:
        """Information about the API.

        The API envoles and dependes on the ChurchTools version.
        This endpoint provides the build version and CT version.

        :returns: The version info and build number
        :rtype: VersionInfo
        """

        res = self.__ct.make_request("info")
        return VersionInfo(**res)

    def whoami(self) -> Person:
        """Currently logged in user.

        This endpoint returns the current user.
        If the request is unauthorized, the anonymous user (aka public user)
        is returned.

        .. note:: In the API there is a parameter defined
            (only_allow_authenticated). We ignore this, as it has no use here.

        :returns: The current user, that is using the API
        :rtype: Person
        """

        res = self.__ct.make_request("whoami")
        return Person(**res["data"])

    def test_route(self, route: str) -> dict:
        """Test an arbitrary route."""

        res = self.__ct.make_request(route)
        return res
