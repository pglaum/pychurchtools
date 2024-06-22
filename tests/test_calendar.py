from tests import get_ct_client


class TestCalendar:
    @classmethod
    def setup_class(cls):
        cls.ct = get_ct_client()

    def test_list_and_appointments(self):
        calendars = self.ct.calendars.list()
        public_calendars = [calendar for calendar in calendars if calendar.isPublic]
        assert len(public_calendars) > 0
        print(public_calendars[0])
        assert self.ct.calendars.appointments([public_calendars[0].id])
