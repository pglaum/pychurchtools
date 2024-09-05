from __future__ import annotations

from tests import get_ct_client


class TestResources:
    appointment_id = 0

    @classmethod
    def setup_class(cls):
        cls.ct = get_ct_client()
        cls.resource_types, cls.resources = cls.ct.resources.masterdata()

    def test_masterdata(self):
        assert self.ct.resources.masterdata()

    def test_bookings(self):
        ids = [r.id for r in self.resources]
        # self.ct.set_debugging_level(2)
        assert self.ct.resources.bookings(ids)
