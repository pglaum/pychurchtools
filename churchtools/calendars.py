from datetime import datetime, timedelta
from typing import Any, Dict, List

from churchtools.ct_types import Appointment, Calendar


class Calendars:
    def __init__(self, ct: Any) -> None:
        """Initialize an Calendar object."""

        self.__ct = ct

    def list(self) -> List[Calendar]:
        """Get all calendars

        :returns: A list of calendars
        :rtype: List[Calendar]
        """

        route = f"calendars"
        res = self.__ct.make_request(route)

        calendars = []
        if "data" in res:
            for item in res["data"]:
                cal = Calendar(**item)
                calendars.append(cal)

        return calendars

    def appointments(
            self,
            calendar_ids: List[int],
            start_date: datetime = datetime.now(),
            end_date: datetime = datetime.now() + timedelta(weeks=4)) -> List[Appointment]:
        """Get all appointments

        :returns: A list of appointments
        :rtype: List[Appointment]
        """

        params: Dict[str, Any] = {}

        params["calendar_ids"] = calendar_ids

        if start_date:
            params["startDate"] = (
                f"{start_date.year}-{start_date.month:02d}-"
                f"{start_date.day:02d}"
            )
        if end_date:
            params["endDate"] = (
                f"{end_date.year}-{end_date.month:02d}-"
                f"{end_date.day:02d}"
            )

        route = f"calendars/appointments"
        res = self.__ct.make_request(route, params=params)

        apps = []
        if "data" in res:
            for item in res["data"]:
                if 'base' in item:
                    app = Appointment(**item['base'])
                    apps.append(app)

        return apps
