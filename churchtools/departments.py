"""
Department
==========

Find out about departments in ChurchTools

"""

from churchtools.ct_types import Department
from typing import Any, List


class Departments:
    def __init__(self, ct: Any) -> None:
        """Initialize a Persons object."""

        self.__ct = ct

    def list(self) -> List[Department]:
        """Returns all departments"""

        res = self.__ct.make_request("departments")

        departments = []
        if res and "data" in res:
            for item in res["data"]:
                department = Department(**item)
                departments.append(department)

        return departments
