"""
Events
======

Endpoints for the event module.

"""

from ct_types import Event


class Events:

    def __init__(self, CT):

        self.CT = CT

    def events(self):

        res = self.CT.make_request('events')

        events = []
        if 'data' in res:
            for item in res['data']:
                events.append(Event(item))

        return events

    def persons_events(self, person_id):

        route = f'persons/{person_id}/events'
        res = self.CT.make_request(route)

        events = []
        if 'data' in res:
            for item in res['data']:
                events.append(Event(item))

        return events
