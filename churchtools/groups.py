"""
Groups
======

Groups we love

"""

from churchtools.ct_types import AgeGroup
from typing import Any, List


class Groups:
    def __init__(self, ct: Any) -> None:

        self.__ct = ct

    def agegroups(self) -> List[AgeGroup]:
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
