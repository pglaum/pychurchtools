from __future__ import annotations

from tests import get_ct_client


class TestDepartments:
    @classmethod
    def setup_class(cls):
        cls.ct = get_ct_client()

    def test_list(self):
        assert self.ct.departments.get_all()
