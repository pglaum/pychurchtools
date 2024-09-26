from __future__ import annotations

from tests import get_ct_client


class TestServices:
    @classmethod
    def setup_class(cls):
        cls.ct = get_ct_client()

    def test_list(self):
        self.ct.services.get_all()

    def test_groups(self):
        self.ct.services.groups()
