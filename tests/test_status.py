from __future__ import annotations

from tests import get_ct_client


class TestStatus:
    @classmethod
    def setup_class(cls):
        cls.ct = get_ct_client()

    def test_get(self):
        statuses = self.ct.status.get_all()
        assert statuses
        assert self.ct.status.get(statuses[0].id)
