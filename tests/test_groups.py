from __future__ import annotations

from tests import get_ct_client


class TestGroups:
    @classmethod
    def setup_class(cls):
        cls.ct = get_ct_client()

    def test_agegroups(self):
        assert self.ct.groups.agegroups()
