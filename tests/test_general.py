from tests import get_ct_client


class TestGeneral:
    @classmethod
    def setup_class(cls):
        cls.ct = get_ct_client()

    def test_info(self):
        assert self.ct.general.info()

    def test_whoami(self):
        assert self.ct.general.whoami()

    def test_search(self):
        assert self.ct.general.search("Gott")
