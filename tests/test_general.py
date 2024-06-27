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

    def test_whoami(self):
        assert self.ct.general.whoami()

    def test_search(self):
        assert self.ct.general.search("Gott")
