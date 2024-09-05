from __future__ import annotations

from churchtools.models.admin import SecurityLevel
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

    def test_security_levels(self):
        securitylevels, pagination = self.ct.admin.list_security_levels()
        assert securitylevels
        assert pagination
        new_level = self.ct.admin.create_security_level(99, "pytest level")
        assert new_level
        new_level = self.ct.admin.patch_security_level(99, "pytest level patched")
        assert new_level
        new_level = self.ct.admin.get_security_level(99)
        assert new_level
        assert new_level.name == "pytest level patched"
        assert self.ct.admin.delete_security_level(99)
