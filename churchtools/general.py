"""
General
=======

Endpoints of general purpose.

"""

from churchtools.ct_types import Person, SearchResult, VersionInfo
from typing import Any, Dict, List


class General:
    def __init__(self, ct: Any) -> None:
        """Initialize a General object."""

        self.__ct = ct

    def csrftoken(self) -> str:
        """Returns the CSRF-Token for the current user.

        :returns: CSRF-Token for the current user
        :rtype: str
        """

        res = self.__ct.make_request("csrftoken")
        return res["data"]

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

    def search(
        self,
        query: str,
        domain_types: List[str] = ["person", "group", "song", "wiki_page"],
    ) -> List[SearchResult]:
        """Search globally for different or all domain types.

        :param query: The search query
        :type query: str
        :param domain_types: A list of domain types to query. Possible values
          are 'person', 'group', 'song', 'wiki_page'
        :returns: A list of search results
        :rtype: SearchResult
        """

        params: Dict[str, Any] = {}
        params["query"] = query
        params["domainTypes[]"] = domain_types

        res = self.__ct.make_request("search", params=params)

        results = []
        if res and "data" in res:
            for item in res["data"]:
                result = SearchResult(**item)
                results.append(result)

        return results

    def test_route(self, route: str) -> dict:
        """Test an arbitrary route."""

        res = self.__ct.make_request(route)
        return res
