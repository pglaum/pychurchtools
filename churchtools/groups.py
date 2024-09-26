"""
Groups
======

Groups we love

"""

from __future__ import annotations

from typing import Any

from .models.group import AgeGroup


class Groups:
    def __init__(self, ct: Any) -> None:
        self.__ct = ct

    def agegroups(self) -> list[AgeGroup]:
        """Get agegroups

        :returns: A list of all age groups
        :rtype: List[AgeGroup]
        """

        res = self.__ct.make_request("group/agegroups")

        agegroups = []
        if res and "data" in res:
            for item in res["data"]:
                agegroups.append(AgeGroup(**item))

        return agegroups
