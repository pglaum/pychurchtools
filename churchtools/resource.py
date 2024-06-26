"""
Resource
========

CRUD methods for Resources

"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

from churchtools.models import resource
from churchtools.models.resource import Booking, Resource, ResourceType


class Resources:
    def __init__(self, ct: Any) -> None:
        """Initialize a Resources object."""

        self.__ct = ct

    def bookings(
        self,
        resource_ids: List[int],
        status_ids: Optional[List[int]] = None,
        from_: Optional[datetime] = None,
        to: Optional[datetime] = None,
    ) -> List[Booking]:
        """Returns all departments"""

        params: Dict[str, Any] = {"resource_ids": resource_ids}

        if status_ids:
            params["status_ids"] = status_ids
        if from_:
            params["from_"] = f"{from_.year}-{from_.month:02d}-" f"{from_.day:02d}"
        if to:
            params["to"] = f"{to.year}-{to.month:02d}-" f"{to.day:02d}"

        res = self.__ct.make_request("bookings", params=params)

        bookings = []
        if res and "data" in res:
            for item in res["data"]:
                if "base" in item:
                    bookings.append(Booking(**item["base"]))

        return bookings

    def masterdata(self) -> Tuple[List[ResourceType], List[Resource]]:
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
