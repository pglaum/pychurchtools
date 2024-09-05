"""
Events
======

Endpoints for the event module.

TODO:
    - export
    - ical
    - send
    - chat

"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from .models.event import Agenda, Event
from .models.song import Song


class Events:
    def __init__(self, ct: Any) -> None:
        """Initialize an Events object."""

        self.__ct = ct

    def get(self, event_id: int) -> Event | None:
        """Get a single event by id.

        :param event_id: The event id
        :type event_id: int
        :returns: The event
        :rtype: Event
        """

        route = f"events/{event_id}"
        res = self.__ct.make_request(route)

        if res and res["data"]:
            return Event(**res["data"])

        return None

    def get_all(
        self,
        from_date: datetime | None = None,
        to_date: datetime | None = None,
        include: str | None = None,
    ) -> list[Event]:
        """List upcoming events, or events from or to a date.

        :param from_date: List events after this date. Default: today
        :type from_date: datetime
        :param to_date: List events up to this date. Default: two months from now
        :type to_date: datetime
        :param include: Include additional data (e.g. "eventServices")
        :type include: str
        :returns: A list of events
        :rtype: List[Event]
        """

        params = {}

        if to_date:
            params["to_date"] = (
                f"{to_date.year}-{to_date.month:02d}-" f"{to_date.day:02d}"
            )
        if from_date:
            params["from_date"] = (
                f"{from_date.year}-{from_date.month:02d}-" f"{from_date.day:02d}"
            )
        if include:
            params["include"] = include

        res = self.__ct.make_request("events", params)

        events = []
        if "data" in res:
            for item in res["data"]:
                ev = Event(**item)
                events.append(ev)

        return events

    def agenda(self, event_id: int) -> Agenda | None:
        """Get the agenda of an event.

        :param event_id: The ID of the event
        :type event_id: int
        :returns: The agenda of the event
        :rtype: Agenda
        """

        route = f"events/{event_id}/agenda"
        res = self.__ct.make_request(route)

        if res and res["data"]:
            return Agenda(**res["data"])

        return None

    def songs(self, event_id: int) -> list[Song]:
        """Get the songs of an event.

        :param event_id: The ID of the event
        :type event_id: int
        :returns: A list of songs, that is set for the event (unordered).
        :rtype: List[Song]
        """

        route = f"events/{event_id}/agenda/songs"
        res = self.__ct.make_request(route)

        sngs = []
        for item in res["data"]:
            sng = Song(**item)
            sngs.append(sng)

        return sngs

    def masterdata(self) -> dict:
        """Get masterdata for module `event`.

        The master data are the backbone of ChurchTools. This endpoint returns
        all data for that module to work with. Different endpoints don't
        include the master data directly but only state the ID for this data
        and this endpoint provides the data with all its details.
        """

        route = "event/masterdata"
        res = self.__ct.make_request(route)

        return res
