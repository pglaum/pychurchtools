"""
Resource
========

CRUD methods for Resources

"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from churchtools.models import resource
from churchtools.models.resource import Booking, Resource, ResourceType, StartEndDate


class Resources:
    def __init__(self, ct: Any) -> None:
        """Initialize a Resources object."""

        self.__ct = ct

    def bookings(
        self,
        resource_ids: list[int],
        status_ids: list[int] | None = None,
        from_: datetime | None = None,
        to: datetime | None = None,
    ) -> list[Booking]:
        """Returns all departments"""

        params: dict[str, Any] = {"resource_ids": resource_ids}

        if status_ids:
            params["status_ids"] = status_ids
        if from_:
            params["from"] = f"{from_.year}-{from_.month:02d}-" f"{from_.day:02d}"
        if to:
            params["to"] = f"{to.year}-{to.month:02d}-" f"{to.day:02d}"

        res = self.__ct.make_request("bookings", params=params)

        bookings = []
        if res and "data" in res:
            for item in res["data"]:
                if "base" in item:
                    booking = Booking(**item["base"])

                    # difference to API: add calculated start & endDate into the Booking
                    if "calculated" in item:
                        booking.calculated = StartEndDate(**item["calculated"])

                    bookings.append(booking)

        return bookings

    def masterdata(self) -> tuple[list[ResourceType], list[Resource]]:
        res = self.__ct.make_request("resource/masterdata")

        resource_types = []
        resources = []
        if res and "data" in res:
            if "resourceTypes" in res["data"]:
                for rtype in res["data"]["resourceTypes"]:
                    resource_types.append(ResourceType(**rtype))
            if "resources" in res["data"]:
                for resource in res["data"]["resources"]:
                    resources.append(Resource(**resource))

        return (
            resource_types,
            resources,
        )
