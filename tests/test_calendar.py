from __future__ import annotations

from datetime import datetime, timedelta

from churchtools.models.calendar import Appointment
from tests import get_ct_client


class TestCalendar:
    appointment_id = 0

    @classmethod
    def setup_class(cls):
        cls.ct = get_ct_client()
        cls.calendars = cls.ct.calendars.get_all()

    def test_list(self):
        assert self.ct.calendars.get_all()

    def test_create_appointment(self):
        appt = Appointment(
            caption="Calendar caption",
            isInternal=False,
            startDate=datetime.now(),
            endDate=datetime.now() + timedelta(hours=2),
        )
        new_appt = self.ct.calendars.create_appointment(self.calendars[0].id, appt)
        assert new_appt
        self.__class__.appointment_id = new_appt.id

    def test_appointments(self):
        assert self.ct.calendars.appointments([self.calendars[0].id])

    def test_put_appointment(self):
        appt = Appointment(
            id=self.__class__.appointment_id,
            caption="Calendar caption 2",
            isInternal=False,
            startDate=datetime.now(),
            endDate=datetime.now() + timedelta(hours=2),
        )
        assert self.ct.calendars.update_appointment(
            self.calendars[0].id, self.__class__.appointment_id, appt
        )

    def test_get_appointment(self):
        appt = self.ct.calendars.get_appointment(
            self.calendars[0].id, self.__class__.appointment_id
        )
        assert appt.caption == "Calendar caption 2"

    def test_delete_appointment(self):
        assert self.ct.calendars.delete_appointment(
            self.calendars[0].id, self.__class__.appointment_id
        )
