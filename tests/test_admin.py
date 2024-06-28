from tests import get_ct_client


class TestAdmin:
    @classmethod
    def setup_class(cls):
        cls.ct = get_ct_client()

    def test_logs(self):
        logs, pagination = self.ct.admin.logs()
        assert logs
        assert pagination

    def test_get_log(self):
        logs, _ = self.ct.admin.logs()
        assert self.ct.admin.get_log(logs[0].id)

    def test_login_statistics(self):
        login_statistics, pagination = self.ct.admin.logs()
        assert login_statistics
        assert pagination
