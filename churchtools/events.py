"""
Events
======

Endpoints for the event module.

TODO:
    - masterdata

"""

from churchtools.ct_types import Agenda, Event, Song
from datetime import datetime
from typing import Any, List


class Events:
    def __init__(self, ct: Any) -> None:
        """Initialize an Events object."""

        self.__ct = ct

    def get(self, event_id: int) -> Event:
        """Get a single event by id.

        :param event_id: The event id
        :type event_id: int
        :returns: The event
        :rtype: Event
        """

        route = f"events/{event_id}"
        res = self.__ct.make_request(route)

        return Event(**res["data"])

    def list(self, from_date: datetime = None, to_date: datetime = None) -> List[Event]:
        """List upcoming events, or events from or to a date.

        :param from_date: List events after this date. Default: today
        :type from_date: datetime
        :param to_date: List events up to this date. Default: two months from now
        :type to_date: datetime
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

        res = self.__ct.make_request("events", params)

        events = []
        for item in res["data"]:
            ev = Event(**item)
            events.append(ev)

        return events

    def agenda(self, event_id: int) -> Agenda:
        """Get the agenda of an event.

        :param event_id: The ID of the event
        :type event_id: int
        :returns: The agenda of the event
        :rtype: Agenda
        """

        route = f"events/{event_id}/agenda"
        res = self.__ct.make_request(route)

        return Agenda(**res["data"])

    def songs(self, event_id: int) -> List[Song]:
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
