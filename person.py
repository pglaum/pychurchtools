"""
Person
======

Find out about persons in ChurchTools

"""

from ct_types import Event, Person, PersonRelationship, PersonTag
from datetime import datetime
from typing import List


class CTPerson:

    def __init__(self, CT):

        self.CT = CT

    def persons(self, ids: List[int] = None, status_ids: List[int] = None,
                campus_ids: List[int] = None, birthday_before: datetime = None,
                birthday_after: datetime = None, is_archived: bool = False,
                page: int = 1, limit: int = 10):

        # TODO: implement parameters

        res = self.CT.make_request('persons')

        persons = []
        if res and 'data' in res:
            for item in res['data']:
                persons.append(Person(item))

        return persons

    def person(self, person_id: int):

        route = f'persons/{person_id}'
        res = self.CT.make_request(route)

        if res and 'data' in res:
            return Person(res['data'])

        return None

    def tags(self, person_id: int):

        route = f'persons/{person_id}/tags'
        res = self.CT.make_request(route)

        tags = []
        if res and 'data' in res:
            for item in res['data']:
                tags.append(PersonTag(item))

        return tags

    def relationships(self, person_id: int):

        route = f'persons/{person_id}/relationships'
        res = self.CT.make_request(route)

        relationships = []
        if res and 'data' in res:
            for item in res['data']:
                relationships.append(PersonRelationship(item))

        return relationships

    def events(self, person_id):

        # TODO: implement parameters

        route = f'persons/{person_id}/events'
        res = self.CT.make_request(route)

        events = []
        if res and 'data' in res:
            for item in res['data']:
                events.append(Event(item))

        return events
