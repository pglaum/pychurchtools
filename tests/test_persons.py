from __future__ import annotations

from tests import get_ct_client


class TestPersons:
    @classmethod
    def setup_class(cls):
        cls.ct = get_ct_client()
        cls.me = cls.ct.general.whoami()

    def test_get(self):
        assert self.ct.persons.get(self.me.id)

    def test_list(self):
        assert self.ct.persons.get_all()

    # def test_tags(self):
    #    assert self.ct.persons.tags(self.me.id)

    # def test_relationships(self):
    #    assert self.ct.persons.relationships(self.me.id)

    def test_events(self):
        assert self.ct.persons.events(self.me.id)

    def test_groups(self):
        assert self.ct.persons.groups(self.me.id)

    def test_settings(self):
        settings = self.ct.persons.settings(self.me.id)
        assert settings
        assert self.ct.persons.setting(
            self.me.id, settings[0].module, settings[0].attribute
        )

    def test_birthdays(self):
        assert self.ct.persons.birthdays()

    def test_service_requests(self):
        servicerequests = self.ct.persons.servicerequests(self.me.id)
        assert servicerequests
        assert self.ct.persons.servicerequest(self.me.id, servicerequests[0].id)

    # def test_devices(self):
    #    devices = self.ct.persons.devices(self.me.id)
    #    assert devices
    #    assert self.ct.persons.device(self.me.id, devices[0].id)

    def test_logintoken(self):
        assert self.ct.persons.logintoken(self.me.id)

    def test_masterdata(self):
        assert self.ct.persons.masterdata()
