from __future__ import annotations

from uuid import uuid4

from tests import get_ct_client


class TestGeneral:
    @classmethod
    def setup_class(cls):
        cls.ct = get_ct_client()

    def test_config(self):
        assert self.ct.general.config()

    def test_config_update(self):
        new_brand = str(uuid4())
        assert self.ct.general.config_update({"brand": new_brand})
        conf = self.ct.general.config()
        assert conf.brand == new_brand

    def test_info(self):
        assert self.ct.general.info()

    def test_search(self):
        assert self.ct.general.search("Gott")

    def test_simulate(self):
        persons, _ = self.ct.persons.get_all()
        me = self.ct.general.whoami()
        persons_other_than_me = [p for p in persons if p.id != me.id]
        person_to_simulate = persons_other_than_me[0]
        assert self.ct.general.simulate(person_to_simulate.id)
        simulated_me = self.ct.general.whoami()
        assert simulated_me.id == person_to_simulate.id
        assert self.ct.general.simulate_stop()
        new_me = self.ct.general.whoami()
        assert new_me.id == me.id

    def test_whoami(self):
        assert self.ct.general.whoami()
