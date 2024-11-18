from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel

from churchtools.models.calendar import AppointmentMeta, CalendarMeta


class BookingAdditional(BaseModel):
    date: date | datetime
    id: int
    isRepeated: bool | None = None
    meta: CalendarMeta


class ResourceType(BaseModel):
    campusId: int | None = None
    id: int
    name: str
    nameTranslated: str
    sortKey: int


class Resource(BaseModel):
    adminIds: list[int] | None = None
    doesRequireCalEntry: bool
    iCalLocation: str | None = None
    id: int
    isAutoAccept: bool
    isVirtual: bool
    location: str | None = None
    name: str
    nameTranslated: str
    randomString: str
    resourceTypeId: int
    sortKey: int


class StartEndDate(BaseModel):
    startDate: datetime
    endDate: datetime


class Booking(BaseModel):
    additionals: list[BookingAdditional]
    allDay: bool
    calculated: StartEndDate | None = None
    calId: int | None = None
    caption: str
    endDate: date | datetime
    exceptions: list[BookingAdditional]
    id: int
    location: str | None = None
    meta: AppointmentMeta | None = None
    note: str | None = None
    personId: int | None = None
    repeatFrequency: int | None = None
    repeatId: int
    repeatOption: int | None = None
    repeatUntil: str | None = None
    resource: Resource
    showInCal: bool
    startDate: date | datetime
    statusId: int
    version: int
