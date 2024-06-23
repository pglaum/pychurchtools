from tests import get_ct_client


class TestGroupHomepages:
    @classmethod
    def setup_class(cls):
        cls.ct = get_ct_client()
        cls.homepages = cls.ct.group_homepages.list()

    def test_list(self):
        assert self.ct.group_homepages.list()

    def test_get(self):
        assert self.homepages and len(self.homepages) > 0
        assert self.ct.group_homepages.get(self.homepages[0].frontendUrl.split("/")[-1])
