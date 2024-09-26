"""
Department
==========

Find out about departments in ChurchTools

"""

from __future__ import annotations

from typing import Any

from .models.department import Department


class Departments:
    def __init__(self, ct: Any) -> None:
        """Initialize a Persons object."""

        self.__ct = ct

    def get_all(self) -> list[Department]:
        """Returns all departments"""

        res = self.__ct.make_request("departments")

        departments = []
        if res and "data" in res:
            for item in res["data"]:
                department = Department(**item)
                departments.append(department)

        return departments
