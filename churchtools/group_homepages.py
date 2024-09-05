"""
GroupHomepages
======

Groups we love

"""

from __future__ import annotations

from typing import Any

from .models.group_homepage import GroupHomepage, GroupHomepageSimple


class GroupHomepages:
    def __init__(self, ct: Any) -> None:
        self.__ct = ct

    def get_all(self) -> list[GroupHomepageSimple]:
        """Get all GroupHomepages

        :returns: A list of all group homepages
        :rtype: List[GroupHomepageSimple]
        """

        res = self.__ct.make_request("grouphomepages")

        homepages = []
        if res and "data" in res:
            for item in res["data"]:
                homepages.append(GroupHomepageSimple(**item))

        return homepages

    def get(self, hash: str) -> GroupHomepage:
        """Get a GroupHomepage by hash

        :returns: A GroupHomepage
        :rtype: GroupHomepage
        """

        res = self.__ct.make_request("grouphomepages/" + hash)

        return GroupHomepage(**res["data"])
