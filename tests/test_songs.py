from tests import get_ct_client


class TestSongs:
    @classmethod
    def setup_class(cls):
        cls.ct = get_ct_client()
        cls.songs, _ = cls.ct.songs.list()

    def test_list(self):
        assert self.ct.songs.list()

    def test_get(self):
        assert self.songs
        assert self.ct.songs.get(self.songs[0].id)
