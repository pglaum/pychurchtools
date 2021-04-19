"""
Person
======

Find out about persons in ChurchTools

TODO:

    - settings
    - servicerequests
    - devices

"""

from ct_types import Event, Group, Person, PersonRelationship, PersonTag
from datetime import datetime
from typing import List


class Persons:

    def __init__(self, CT):

        self.CT = CT

    def get(self, person_id: int):

        route = f'persons/{person_id}'
        res = self.CT.make_request(route)

        if res and 'data' in res:
            return Person(**res['data'])

        return None

    def list(self, ids: List[int] = None, status_ids: List[int] = None,
             campus_ids: List[int] = None, birthday_before: datetime = None,
             birthday_after: datetime = None, is_archived: bool = False,
             page: int = 1, limit: int = 10):

        # TODO: pagination

        params = {}

        if ids:
            params['ids'] = ids
        if status_ids:
            params['status_ids'] = status_ids
        if campus_ids:
            params['campus_ids'] = campus_ids
        if birthday_before:
            params['birthday_before'] = \
                f'{birthday_before.year}-{birthday_before.month:02d}-' \
                f'{birthday_before.day:02d}'
        if birthday_after:
            params['birthday_after'] = \
                f'{birthday_after.year}-{birthday_after.month:02d}-' \
                f'{birthday_after.day:02d}'
        if is_archived:
            params['is_archived'] = is_archived
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit

        res = self.CT.make_request('persons', params=params)

        persons = []
        if res and 'data' in res:
            for item in res['data']:
                pers = Person(**item)
                persons.append(pers)

        return persons

    def tags(self, person_id: int):

        route = f'persons/{person_id}/tags'
        res = self.CT.make_request(route)

        tags = []
        if res and 'data' in res:
            for item in res['data']:
                tags.append(PersonTag(**item))

        return tags

    def relationships(self, person_id: int):

        route = f'persons/{person_id}/relationships'
        res = self.CT.make_request(route)

        rls = []
        if res and 'data' in res:
            for item in res['data']:
                rl = PersonRelationship(**item)
                rls.append(rl)

        return rls

    def events(self, person_id: int, from_date: datetime = None):

        params = {}
        if from_date:
            params['from'] = \
                f'{from_date.year}-{from_date.month:02d}-' \
                f'{from_date.day:02d}'

        route = f'persons/{person_id}/events'
        res = self.CT.make_request(route, params)

        evs = []
        if 'data' in res:
            for item in res['data']:
                ev = Event(**item)
                evs.append(ev)

        return evs

    def groups(self, person_id: int, show_overdue_groups: bool = False,
               show_inactive_groups: bool = False):

        params = {}
        if show_overdue_groups:
            params['show_overdue_groups'] = show_overdue_groups
        if show_inactive_groups:
            params['show_inactive_groups'] = show_inactive_groups

        route = f'persons/{person_id}/groups'
        res = self.CT.make_request(route, params)

        # TODO: check if we are missing some relevant data.
        #       usually, only the group itself should be interesting.
        grps = []
        for item in res['data']:
            grp = Group(**item['group'])
            grps.append(grp)

        return grps
