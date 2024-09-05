"""
Admin
=====

Admin relevant endpoints

"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from churchtools.models.admin import LogEntry, LoginStatistic, SecurityLevel
from churchtools.models.pagination import MetaPagination


class Admin:
    def __init__(self, ct: Any) -> None:
        """Initialize a Persons object."""

        self.__ct = ct

    def logs(
        self,
        message: str | None = None,
        levels: list[str] | None = None,
        before: datetime | None = None,
        after: datetime | None = None,
        person_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> tuple[list[LogEntry], MetaPagination | None]:
        """The response is a collection of all log messages you may see and is limited to a specific number of messages.
        You can use the page parameter to browse the list of log messages. The logs are ordered by date.

        :param message: Filter by message text
        :type message: str
        :param levels: Filter by log level ID
        :type levels: List[str]
        :param before: Filter log messages before that date.
        :type before: datetime
        :param after: Filter log messages after that date.
        :type after: datetime
        :param person_id: Filter by person
        :type person_id: int
        :param page: Page number to show page in pagination. If empty, start at first page.
        :type page: int
        :param limit: Number of results per page (default: 10)
        :type limit: int
        :returns: A list of log messages & pagination
        :rtype: Tuple[List[LogEntry], MetaPagination]
        """

        params: dict[str, Any] = {}

        if message:
            params["message"] = message
        if levels:
            params["levels"] = levels
        if before:
            params["before"] = before.strftime("%Y-%m-%dT%H:%M:%SZ")
        if after:
            params["after"] = after.strftime("%Y-%m-%dT%H:%M:%SZ")
        if person_id:
            params["person_id"] = person_id
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit

        res = self.__ct.make_request("logs", params=params)

        logs: list[LogEntry] = []
        pagination = None
        if res and "data" in res:
            for log in res["data"]:
                logs.append(LogEntry(**log))

        if res and "meta" in res:
            pagination = MetaPagination(**res["meta"])

        return logs, pagination

    def get_log(self, id: int) -> LogEntry | None:
        """Fetch one specific log message by its ID

        :param id: ID of the entity
        :type id: int
        :returns: The log entry
        :rtype: Optional[LogEntry]
        """

        res = self.__ct.make_request(f"logs/{id}")

        if res and "data" in res:
            return LogEntry(**res["data"])

        return None

    def login_statistics(
        self,
        order_by: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> tuple[list[LoginStatistic], MetaPagination | None]:
        """Get statistics about login counts of users.

        :param order_by: Order the pagination result. Allowed values: `frequent` and `last`
        :type order_by: str
        :param page: Page number to show page in pagination. If empty, start at first page.
        :type page: int
        :param limit: Number of results per page (default: 10)
        :type limit: int
        :returns: A list of login statistics & pagination
        :rtype: Tuple[List[LogEntry], Optional[MetaPagination]]
        """

        params: dict[str, Any] = {}
        if order_by:
            params["order_by"] = order_by
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit

        res = self.__ct.make_request("logs/statistics/login", params=params)

        login_statistics: list[LoginStatistic] = []
        pagination = None
        if res and "data" in res:
            for login in res["data"]:
                login_statistics.append(LoginStatistic(**login))
        if res and "meta" in res:
            pagination = MetaPagination(**res["meta"])

        return login_statistics, pagination

    def list_security_levels(
        self,
    ) -> tuple[list[SecurityLevel], MetaPagination | None]:
        """Get all security levels

        :returns: A list of security levels & pagination
        :rtype: Tuple[List[LogEntry], Optional[MetaPagination]]
        """

        res = self.__ct.make_request("securitylevels")

        securitylevels: list[SecurityLevel] = []
        pagination = None
        if res and "data" in res:
            for level in res["data"]:
                securitylevels.append(SecurityLevel(**level))
        if res and "meta" in res:
            pagination = MetaPagination(**res["meta"])

        return securitylevels, pagination

    def create_security_level(self, id: int, name: str) -> SecurityLevel | None:
        """Create a new security level.

        :param id: The ID of the new security level
        :type id: int
        :param name: The name of the new security level
        :type name: str
        :returns: The newly created SecurityLevel
        :rtype: Optional[SecurityLevel]
        """

        data: dict[str, Any] = {"name": name}
        res = self.__ct.make_request(f"securitylevels/{id}", method="post", data=data)
        if res:
            return SecurityLevel(**res)

        return None

    def patch_security_level(
        self,
        id: int,
        name: str,
        forcereorder: bool | None = None,
        newid: int | None = None,
    ) -> SecurityLevel | None:
        """Change a security level

        :param id: The ID of the updated security level
        :type id: int
        :param name: The name of the updated security level
        :type name: str
        :param forcereorder: Needs to be true, if security level shall be reordered
        :type forcereorder: bool
        :param newid: The new ID of the updated security level
        :type newid: int
        :returns: The updated SecurityLevel
        :rtype: Optional[SecurityLevel]
        """

        params: dict[str, Any] = {}
        data: dict[str, Any] = {
            "name": name,
            "newid": newid if newid is not None else id,
        }

        if forcereorder is not None:
            params["forcereorder"] = forcereorder
            data["forcereorder"] = forcereorder

        res = self.__ct.make_request(
            f"securitylevels/{id}", params=params, method="patch", data=data
        )
        if res:
            return SecurityLevel(**res)

        return None

    def get_security_level(self, id: int) -> SecurityLevel | None:
        """Get a security level

        :param id: The ID of the updated security level
        :type id: int
        :returns: The SecurityLevel
        :rtype: Optional[SecurityLevel]
        """

        res = self.__ct.make_request(f"securitylevels/{id}")
        if res:
            return SecurityLevel(**res)

        return None

    def delete_security_level(self, id: int) -> bool:
        """Delete a security level

        :param id: The ID of the updated security level
        :type id: int
        :returns: The success
        :rtype: bool
        """

        res = self.__ct.make_request(
            f"securitylevels/{id}", method="delete", return_status_code=True
        )
        return res == 200
