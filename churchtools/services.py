"""
Service
=======

CRUD methods for services & service groups

TODO:

    - servicegroups

"""

from __future__ import annotations

from typing import Any

from .models.service import Service, ServiceGroup


class Services:
    def __init__(self, ct: Any) -> None:
        self.__ct = ct

    def get_all(self) -> list[Service]:
        """List all services.

        :returns: A list of all services
        :rtype: List[Service]
        """

        res = self.__ct.make_request("services")

        services = []
        if res and "data" in res:
            for item in res["data"]:
                services.append(Service(**item))

        return services

    def groups(self) -> list[ServiceGroup]:
        """List all service groups.

        :returns: A list of all service groups
        :rtype: List[ServiceGroup]
        """

        res = self.__ct.make_request("services")

        sgroups = []
        if res and "data" in res:
            for item in res["data"]:
                sgroups.append(ServiceGroup(**item))

        return sgroups
