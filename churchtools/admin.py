"""
Admin
=====

Admin relevant endpoints

"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

from churchtools.models.admin import LogEntry, LoginStatistic
from churchtools.models.pagination import MetaPagination


class Admin:
    def __init__(self, ct: Any) -> None:
        """Initialize a Persons object."""

        self.__ct = ct

    def logs(
        self,
        message: Optional[str] = None,
        levels: Optional[List[str]] = None,
        before: Optional[datetime] = None,
        after: Optional[datetime] = None,
        person_id: Optional[int] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Tuple[List[LogEntry], Optional[MetaPagination]]:
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

        params: Dict[str, Any] = {}

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

        logs: List[LogEntry] = []
        pagination = None
        if res and "data" in res:
            for log in res["data"]:
                logs.append(LogEntry(**log))

        if res and "meta" in res:
            pagination = MetaPagination(**res["meta"])

        return logs, pagination

    def get_log(self, id: int) -> Optional[LogEntry]:
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
        order_by: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Tuple[List[LoginStatistic], Optional[MetaPagination]]:
        """Get statistics about login counts of users.

        :param order_by: Order the pagination result. Allowed values: `frequent` and `last`
        :type order_by: str
        :param page: Page number to show page in pagination. If empty, start at first page.
        :type page: int
        :param limit: Number of results per page (default: 10)
        :type limit: int
        :returns: A list of login statistics & pagination
        :rtype: Tuple[List[LogEntry], MetaPagination]
        """

        params: Dict[str, Any] = {}
        if order_by:
            params["order_by"] = order_by
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit

        res = self.__ct.make_request("logs/statistics/login", params=params)

        login_statistics: List[LoginStatistic] = []
        pagination = None
        if res and "data" in res:
            for login in res["data"]:
                login_statistics.append(LoginStatistic(**login))
        if res and "meta" in res:
            pagination = MetaPagination(**res["meta"])

        return login_statistics, pagination
