"""
General
=======

Endpoints of general purpose.

"""

from __future__ import annotations

from typing import Any

from .models.general import Config, SearchResult, SimulateStop, VersionInfo
from .models.person import Person


class General:
    def __init__(self, ct: Any) -> None:
        """Initialize a General object."""

        self.__ct = ct

    def config(self) -> Config | None:
        """Get the ChurchTools-Config

        :returns: The current churchtools config
        :rtype: Config
        """

        res = self.__ct.make_request("config")
        if not res:
            return None

        return Config(**res)

    def config_update(self, updates: dict) -> bool:
        """Change the ChurchTools-config

        :param updates: The field you want to update
        :type updates: dict
        :returns: The success
        :rtype: bool
        """

        res = self.__ct.make_request(
            "config", method="put", data=updates, return_status_code=True
        )
        return res == 204

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

    def search(
        self, query: str, domain_types: list[str] | None = None
    ) -> list[SearchResult]:
        """Search globally for different or all domain types.

        :param query: The search query
        :type query: str
        :param domain_types: A list of domain types to query. Possible values
          are 'person', 'group', 'song', 'wiki_page'
        :returns: A list of search results
        :rtype: SearchResult
        """
        domain_types = (
            ["person", "group", "song", "wiki_page"]
            if domain_types is None
            else domain_types
        )

        params: dict[str, Any] = {}
        params["query"] = query
        params["domainTypes"] = domain_types

        res = self.__ct.make_request("search", params=params)

        results = []
        if res and "data" in res:
            for item in res["data"]:
                result = SearchResult(**item)
                results.append(result)

        return results

    def simulate(self, person_id: int) -> bool:
        """Starts the simulation of another person

        :param person_id: The ID of the person you want to simulate
        :type person_id: int
        :returns: The success
        :rtype: bool
        """

        params: dict[str, Any] = {"personId": person_id}
        res = self.__ct.make_request(
            "simulate", method="post", data=params, return_status_code=True
        )
        return res == 204

    def simulate_stop(self) -> SimulateStop | None:
        """Stops the simulation of another person

        :returns: The simulate stop data
        :rtype: SimulateStop
        """

        res = self.__ct.make_request("simulate", method="delete")

        if "data" in res:
            return SimulateStop(**res["data"])
        return None

    def test_route(self, route: str) -> dict:
        """Test an arbitrary route."""

        res = self.__ct.make_request(route)
        return res

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
