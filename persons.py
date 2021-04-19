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
from typing import Any, Dict, List, Optional


class Persons:

    def __init__(self, ct: Any) -> None:
        """Initialize a Persons object.
        """

        self.__ct = ct

    def get(self, person_id: int) -> Optional[Person]:
        """Get a person by id.

        :param person_id: The ID of the person
        :type person_id: int
        :returns: A person object
        :rtype: Person
        """

        route = f'persons/{person_id}'
        res = self.__ct.make_request(route)

        if res and 'data' in res:
            return Person(**res['data'])

        return None

    def list(self, ids: List[int] = None, status_ids: List[int] = None,
             campus_ids: List[int] = None, birthday_before: datetime = None,
             birthday_after: datetime = None, is_archived: bool = False,
             page: int = 1, limit: int = 10) -> List[Person]:
        """Returns a list of persons, that the logged in user can see.

        :param ids: A list of IDs that is to be queried
        :type ids: List[int]
        :param status_ids: A list of status IDs that is to be queried
        :type status_ids: List[int]
        :param campus_ids: A list of campus IDs that is to be queried
        :type campus_ids: List[int]
        :param birthday_before: Only list persons born before this date
        :type birthday_before: datetime
        :param birthday_after: Only list persons born after this date
        :type birthday_after: datetime
        :param is_archived: List archived persons
        :type is_archived: bool
        :param page: Get this result page number
        :type page: int
        :param limit: Return this many results
        :type limit: int
        :returns: A list of persons that match the query
        :rtype: List[Person]
        """

        # TODO: pagination

        params: Dict[str, Any] = {}

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

        res = self.__ct.make_request('persons', params=params)

        persons = []
        if res and 'data' in res:
            for item in res['data']:
                pers = Person(**item)
                persons.append(pers)

        return persons

    def tags(self, person_id: int) -> List[PersonTag]:
        """Get the tags of a person.

        :param person_id: The ID of the person
        :type person_id: int
        :returns: A list of tags for the person
        :rtype: List[PersonTag]
        """

        route = f'persons/{person_id}/tags'
        res = self.__ct.make_request(route)

        tags = []
        if res and 'data' in res:
            for item in res['data']:
                tags.append(PersonTag(**item))

        return tags

    def relationships(self, person_id: int) -> List[PersonRelationship]:
        """Get relationships for a person.

        :param person_id: The ID of the person
        :type person_id: int
        :returns: A list of relationships
        :rtype: List[PersonRelationship]
        """

        route = f'persons/{person_id}/relationships'
        res = self.__ct.make_request(route)

        rls = []
        if res and 'data' in res:
            for item in res['data']:
                rl = PersonRelationship(**item)
                rls.append(rl)

        return rls

    def events(self, person_id: int, from_date: datetime = None
               ) -> List[Event]:
        """Get events that a person is involved in.

        :param person_id: The ID of the person
        :type person_id: int
        :param from_date: Only query events after this date
        :type from_date: datetime
        :returns: A list of events
        :rtype: List[Event]
        """

        params = {}
        if from_date:
            params['from'] = \
                f'{from_date.year}-{from_date.month:02d}-' \
                f'{from_date.day:02d}'

        route = f'persons/{person_id}/events'
        res = self.__ct.make_request(route, params)

        evs = []
        if 'data' in res:
            for item in res['data']:
                ev = Event(**item)
                evs.append(ev)

        return evs

    def groups(self, person_id: int, show_overdue_groups: bool = False,
               show_inactive_groups: bool = False) -> List[Group]:
        """Get events that a person is part of.

        :param person_id: The ID of the person
        :type person_id: int
        :param show_overdue_groups: Show overdue groups
        :type show_overdue_groups: bool
        :param show_inactive_groups: Show inactive groups
        :type show_inactive_groups: bool
        :returns: A list of groups
        :rtype: List[Group]
        """

        params = {}
        if show_overdue_groups:
            params['show_overdue_groups'] = show_overdue_groups
        if show_inactive_groups:
            params['show_inactive_groups'] = show_inactive_groups

        route = f'persons/{person_id}/groups'
        res = self.__ct.make_request(route, params)

        # TODO: check if we are missing some relevant data.
        #       usually, only the group itself should be interesting.
        grps = []
        for item in res['data']:
            grp = Group(**item['group'])
            grps.append(grp)

        return grps
