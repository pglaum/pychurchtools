"""
Service
=======

CRUD methods for services & service groups

TODO:

    - servicegroups

"""

from churchtools.ct_types import Service, ServiceGroup
from typing import Any, List


class Services:
    def __init__(self, ct: Any) -> None:

        self.__ct = ct

    def list(self) -> List[Service]:
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

    def groups(self) -> List[ServiceGroup]:
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
