"""
Events
======

Endpoints for the event module.

TODO:
    - masterdata

"""

from ct_types import Agenda, Event, Song
from datetime import datetime
from typing import List


class Events:

    def __init__(self, CT):

        self.CT = CT

    def get(self, event_id: int) -> Event:

        route = f'events/{event_id}'
        res = self.CT.make_request(route)

        return Event(**res['data'])

    def list(self, from_date: datetime = None, to_date: datetime = None
             ) -> List[Event]:

        # TODO: pagination

        params = {}

        if to_date:
            params['to_date'] = \
                f'{to_date.year}-{to_date.month:02d}-' \
                f'{to_date.day:02d}'
        if from_date:
            params['from_date'] = \
                f'{from_date.year}-{from_date.month:02d}-' \
                f'{from_date.day:02d}'

        res = self.CT.make_request('events', params)

        events = []
        for item in res['data']:
            ev = Event(**item)
            events.append(ev)

        return events

    def agenda(self, event_id: int) -> Agenda:

        route = f'events/{event_id}/agenda'
        res = self.CT.make_request(route)

        return Agenda(**res['data'])

    def songs(self, event_id: int) -> List[Song]:

        route = f'events/{event_id}/agenda/songs'
        res = self.CT.make_request(route)

        sngs = []
        for item in res['data']:
            sng = Song(**item)
            sngs.append(sng)

        return sngs
