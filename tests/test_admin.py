from tests import get_ct_client


class TestAdmin:
    @classmethod
    def setup_class(cls):
        cls.ct = get_ct_client()

    def test_logs(self):
        logs, pagination = self.ct.admin.logs()
        assert logs
        assert pagination
