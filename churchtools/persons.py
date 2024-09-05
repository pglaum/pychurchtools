"""
Person
======

Find out about persons in ChurchTools

TODO:

    - information
    - persons POST
    - duplicates
    - properties
    - person DELETE, PATCH
    - archive
    - device DELETE, PUT
    - invite
    - merge GET, PATCH
    - servicerequest DELETE, PUT
    - undo servicerequest
    - attribute DELETE, PUT

"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any

from .models.event import Event
from .models.group import Group
from .models.pagination import MetaPagination
from .models.person import Birthday, Device, Person, PersonRelationship, PersonTag
from .models.service import ServiceRequest
from .models.settings import Setting


class Persons:
    def __init__(self, ct: Any) -> None:
        """Initialize a Persons object."""

        self.__ct = ct

    def get(self, person_id: int) -> Person | None:
        """Get a person by id.

        :param person_id: The ID of the person
        :type person_id: int
        :returns: A person object
        :rtype: Person
        """

        route = f"persons/{person_id}"
        res = self.__ct.make_request(route)

        if res and "data" in res:
            return Person(**res["data"])

        return None

    def get_all(
        self,
        ids: list[int] | None = None,
        status_ids: list[int] | None = None,
        campus_ids: list[int] | None = None,
        birthday_before: datetime | None = None,
        birthday_after: datetime | None = None,
        is_archived: bool = False,
        page: int = 1,
        limit: int = 10,
    ) -> tuple[list[Person], MetaPagination | None]:
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

        params: dict[str, Any] = {}

        if ids:
            params["ids"] = ids
        if status_ids:
            params["status_ids"] = status_ids
        if campus_ids:
            params["campus_ids"] = campus_ids
        if birthday_before:
            params["birthday_before"] = (
                f"{birthday_before.year}-{birthday_before.month:02d}-"
                f"{birthday_before.day:02d}"
            )
        if birthday_after:
            params["birthday_after"] = (
                f"{birthday_after.year}-{birthday_after.month:02d}-"
                f"{birthday_after.day:02d}"
            )
        if is_archived:
            params["is_archived"] = is_archived
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit

        res = self.__ct.make_request("persons", params=params)

        persons = []
        if res and "data" in res:
            for item in res["data"]:
                pers = Person(**item)
                persons.append(pers)

        pagination = None
        if res and "meta" in res:
            pagination = MetaPagination(**res["meta"])

        return persons, pagination

    def tags(self, person_id: int) -> list[PersonTag]:
        """Get the tags of a person.

        :param person_id: The ID of the person
        :type person_id: int
        :returns: A list of tags for the person
        :rtype: List[PersonTag]
        """

        route = f"persons/{person_id}/tags"
        res = self.__ct.make_request(route)

        tags = []
        if res and "data" in res:
            for item in res["data"]:
                tags.append(PersonTag(**item))

        return tags

    def relationships(self, person_id: int) -> list[PersonRelationship]:
        """Get relationships for a person.

        :param person_id: The ID of the person
        :type person_id: int
        :returns: A list of relationships
        :rtype: List[PersonRelationship]
        """

        route = f"persons/{person_id}/relationships"
        res = self.__ct.make_request(route)

        rls = []
        if res and "data" in res:
            for item in res["data"]:
                rl = PersonRelationship(**item)
                rls.append(rl)

        return rls

    def events(self, person_id: int, from_date: datetime | None = None) -> list[Event]:
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
            params["from"] = (
                f"{from_date.year}-{from_date.month:02d}-" f"{from_date.day:02d}"
            )

        route = f"persons/{person_id}/events"
        res = self.__ct.make_request(route, params)

        evs = []
        if "data" in res:
            for item in res["data"]:
                ev = Event(**item)
                evs.append(ev)

        return evs

    def groups(
        self,
        person_id: int,
        show_overdue_groups: bool = False,
        show_inactive_groups: bool = False,
    ) -> list[Group]:
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
            params["show_overdue_groups"] = show_overdue_groups
        if show_inactive_groups:
            params["show_inactive_groups"] = show_inactive_groups

        route = f"persons/{person_id}/groups"
        res = self.__ct.make_request(route, params)

        grps = []
        for item in res["data"]:
            grp = Group(**item["group"])
            grps.append(grp)

        return grps

    def settings(self, person_id: int, module: str | None = None) -> list[Setting]:
        """Get the settings for a person.

        :param person_id: The ID of the person
        :type person_id: int
        :param module: Only list settings for a module
        :type module: str
        :returns: A list of settings
        :rtype: List[Setting]
        """

        route = f"persons/{person_id}/settings"
        if module:
            route = f"{route}/{module}"

        res = self.__ct.make_request(route)

        sttngs = []

        for item in res["data"]:
            sttng = Setting(**item)
            sttngs.append(sttng)

        return sttngs

    def setting(self, person_id: int, module: str, attribute: str) -> Setting:
        """Get a setting for a person.

        :param person_id: The ID of the person
        :type person_id: int
        :param module: The settings module
        :type module: str
        :param attribute: The wanted attribute
        :type attribute: str
        :returns: The setting
        :rtype: Setting
        """

        route = f"persons/{person_id}/settings/{module}/{attribute}"

        res = self.__ct.make_request(route)

        sttng = Setting(**res["data"])
        return sttng

    def birthdays(
        self, start_date: date | None = None, end_date: date | None = None
    ) -> list[Birthday]:
        """Get all birthdays in a time span.

        :param start_date: Start date of the timespan (default: yesterday)
        :type start_date: date
        :param end_date: End date of the timespan (default: 30 days from now)
        :type end_date: date
        :returns: A list of birthdays, including ages and persons
        :rtype: List[Birthday]
        """

        route = "persons/birthdays"

        params = {}
        if start_date:
            params["start_date"] = start_date.strftime("%Y-%m-%d")
        if end_date:
            params["end_date"] = end_date.strftime("%Y-%m-%d")

        res = self.__ct.make_request(route, params)

        bdays = []

        for item in res["data"]:
            bday = Birthday(**item)
            bdays.append(bday)

        return bdays

    def servicerequests(self, person_id: int) -> list[ServiceRequest]:
        """Get all service requests for a person.

        :param person_id: The ID of the person
        :type person_id: int
        :returns: A list of service requests
        :rtype: List[ServiceRequest]
        """

        route = f"persons/{person_id}/servicerequests"
        res = self.__ct.make_request(route)

        rqsts = []

        for item in res["data"]:
            rqst = ServiceRequest(**item)
            rqsts.append(rqst)

        return rqsts

    def servicerequest(self, person_id: int, servicerequest_id: int) -> ServiceRequest:
        """Get all service requests for a person.

        :param person_id: The ID of the person
        :type person_id: int
        :param servicerequest_id: The ID of the service request
        :type servicerequest_id: int
        :returns: A service request
        :rtype: ServiceRequest
        """

        route = f"persons/{person_id}/servicerequests/{servicerequest_id}"
        res = self.__ct.make_request(route)

        rqst = ServiceRequest(**res["data"])
        return rqst

    def devices(self, person_id: int) -> list[Device]:
        """Get all in ChurchTools registered devices of a person.

        These are all registered smartphones/tablets with the CT app.

        :param person_id: The ID of the person
        :type person_id: int
        :returns: A list of registered devices
        :rtype: List[Device]
        """

        route = f"persons/{person_id}/devices"
        res = self.__ct.make_request(route)

        dvcs = []
        for item in res["data"]:
            dvc = Device(**item)
            dvcs.append(dvc)

        return dvcs

    def device(self, person_id: int, device_id: str) -> Device:
        """Get all information about one device.

        :param person_id: The ID of the person
        :type person_id: int
        :param device_id: The ID of the device
        :type device_id: str
        :returns: A list of registered devices
        :rtype: List[Device]
        """

        route = f"persons/{person_id}/devices/{device_id}"
        res = self.__ct.make_request(route)

        dvc = Device(**res["data"])
        return dvc

    def logintoken(self, person_id: int) -> str:
        """Fetch login token for person.

        If a token does not yet exist, a new one is created on the fly.
        """

        route = f"persons/{person_id}/logintoken"
        res = self.__ct.make_request(route)

        return res["data"]

    def masterdata(self) -> dict:
        """Fetch all master data for the module `people & groups`.

        The master data are the backbone of ChurchTools. You can add new db
        fields, or change the available countries. This endpoint returns all
        data for that module to work with. Different endpoints don't include
        the master data directly but only state the ID for this data and this
        endpoint provides the data with all its details.
        """

        route = "person/masterdata"
        res = self.__ct.make_request(route)

        return res
