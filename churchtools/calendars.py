from __future__ import annotations

import json
from datetime import datetime, timedelta
from typing import Any

from .models.calendar import Appointment, Calendar


class Calendars:
    def __init__(self, ct: Any) -> None:
        """Initialize an Calendar object."""

        self.__ct = ct

    def get_all(self) -> list[Calendar]:
        """Get all calendars

        :returns: A list of calendars
        :rtype: List[Calendar]
        """

        route = "calendars"
        res = self.__ct.make_request(route)

        calendars = []
        if "data" in res:
            for item in res["data"]:
                cal = Calendar(**item)
                calendars.append(cal)

        return calendars

    def appointments(
        self,
        calendar_ids: list[int],
        start_date: datetime | None = None,
        end_date: datetime | None = None,
    ) -> list[Appointment]:
        """Get all appointments

        :returns: A list of appointments
        :rtype: List[Appointment]
        """
        start_date = datetime.now() if start_date is None else start_date
        end_date = datetime.now() + timedelta(weeks=4) if end_date is None else end_date

        params: dict[str, Any] = {}

        params["calendar_ids"] = calendar_ids

        if start_date:
            params["from"] = (
                f"{start_date.year}-{start_date.month:02d}-" f"{start_date.day:02d}"
            )
        if end_date:
            params["to"] = (
                f"{end_date.year}-{end_date.month:02d}-" f"{end_date.day:02d}"
            )

        route = "calendars/appointments"
        res = self.__ct.make_request(route, params=params)

        apps = []
        if "data" in res:
            for item in res["data"]:
                if "base" in item:
                    item["base"]["startDate"] = item["calculated"]["startDate"]
                    item["base"]["endDate"] = item["calculated"]["endDate"]
                    try:
                        app = Appointment(**item["base"])
                        apps.append(app)
                    except Exception as e:
                        print(item)
                        print(e)

        return apps

    def create_appointment(
        self, calendar_id: int, appointment: Appointment
    ) -> Appointment | None:
        """Create a new appointment

        .. note:: Dates have to be UTC!

        :param calendar_id: The ID of the calendar
        :type calendar_id: int
        :param appointment: The new appointment
        :type appointment: Appointment
        :returns: The newly created appointment
        :rtype: Appointment
        """

        route = f"calendars/{calendar_id}/appointments"
        res = self.__ct.make_request(
            route, method="post", data=json.loads(appointment.json())
        )

        if "data" in res:
            return Appointment(**res["data"])

        return None

    def get_appointment(
        self, calendar_id: int, appointment_id: int
    ) -> Appointment | None:
        """Get an appointment by ID

        :param calendar_id: The ID of the calendar
        :type calendar_id: int
        :param appointment_id: The ID of the appointment
        :type appointment_id: int
        :returns: The Appointment
        :rtype: Appointment
        """

        route = f"calendars/{calendar_id}/appointments/{appointment_id}"
        res = self.__ct.make_request(route)

        if "data" in res:
            if "appointment" in res["data"]:
                return Appointment(**res["data"]["appointment"])

        return None

    def update_appointment(
        self, calendar_id: int, appointment_id: int, appointment: Appointment
    ) -> Appointment | None:
        """Update an appointment

        .. note:: Dates have to be UTC!

        :param calendar_id: The ID of the calendar
        :type calendar_id: int
        :param appointment_id: The ID of the appointment
        :type appointment_id: int
        :param appointment: The updated appointment
        :type appointment: Appointment
        :returns: The updated appointment
        :rtype: Appointment
        """

        route = f"calendars/{calendar_id}/appointments/{appointment_id}"
        res = self.__ct.make_request(
            route, method="put", data=json.loads(appointment.json())
        )

        if "data" in res:
            return Appointment(**res["data"])

        return None

    def delete_appointment(self, calendar_id: int, appointment_id: int) -> bool:
        """Delete an appointment

        :param calendar_id: The ID of the calendar
        :type calendar_id: int
        :param appointment_id: The ID of the appointment
        :type appointment_id: int
        :param appointment: The updated appointment
        :type appointment: Appointment
        :returns: Success
        :rtype: bool
        """

        route = f"calendars/{calendar_id}/appointments/{appointment_id}"
        status_code = self.__ct.make_request(
            route, method="delete", return_status_code=True
        )
        return status_code == 204
