from __future__ import annotations

from tests import get_ct_client


class TestEvents:
    @classmethod
    def setup_class(cls):
        cls.ct = get_ct_client()
        cls.events = cls.ct.events.get_all()

    def test_list(self):
        assert self.ct.events.get_all(include="eventServices")

    def test_get(self):
        assert self.events and len(self.events) > 0
        assert self.ct.events.get(self.events[0].id)

    def test_agenda(self):
        # TODO: find an event with agenda more reliably
        next_services = [evt for evt in self.events if "Gottesdienst" in evt.name]
        assert len(next_services) > 0
        assert self.ct.events.agenda(next_services[0].id)

    def test_songs(self):
        # TODO: find an event with songs more reliably
        next_services = [evt for evt in self.events if "Gottesdienst" in evt.name]
        assert len(next_services) > 0
        assert self.ct.events.songs(next_services[0].id)

    def test_masterdata(self):
        assert self.ct.events.masterdata()
