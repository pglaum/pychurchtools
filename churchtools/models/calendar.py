from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, field_serializer, Field  # type: ignore

from . import EmptyStrToNone


class CalendarMeta(BaseModel):
    modifiedDate: date | datetime
    modifiedPid: int


class Calendar(BaseModel):
    campusId: int | None = None
    color: str
    eventTemplateId: int | None = None
    iCalSourceUrl: str | None = None
    id: int
    isPrivate: bool
    isPublic: bool
    meta: CalendarMeta | None = None
    name: str
    nameTranslated: str
    randomUrl: str
    sortKey: int


class Address(BaseModel):
    meetingAt: str | None = None
    street: str | None = None
    addition: str | None = None
    district: str | None = None
    zip: str | None = None
    city: str | None = None
    country: str | None = None
    latitude: EmptyStrToNone[float] | None = None
    longitude: EmptyStrToNone[float] | None = None


class AppointmentAddition(BaseModel):
    date: date | datetime
    isRepeated: bool | None = False


class AppointmentException(BaseModel):
    date: date | datetime
    id: int
    meta: CalendarMeta


class PersonWithOnlyId(BaseModel):
    id: int


class AppointmentMeta(BaseModel):
    createdDate: date | datetime
    createdPerson: PersonWithOnlyId
    modifiedDate: date | datetime
    modifiedPerson: PersonWithOnlyId


class Appointment(BaseModel):
    additions: list[AppointmentAddition] = Field(default_factory=list)
    address: Address | None = None
    allDay: bool = False
    calendar: Calendar | None = None
    caption: str
    endDate: date | datetime
    exceptions: list[AppointmentException] = Field(default_factory=list)
    id: int | str | None = None
    image: str | None = None
    information: str | None = None
    isInternal: bool = True
    link: str | None = None
    meta: AppointmentMeta | None = None
    note: str | None = None
    onBehalfOfPid: int | None = None
    startDate: date | datetime
    repeatFrequency: int | None = None
    repeatId: int = 0
    repeatOption: int | None = None
    repeatUntil: str | None = None
    version: int = 0

    @field_serializer("startDate")
    def serialize_startDate(self, dt: datetime, _info):
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    @field_serializer("endDate")
    def serialize_endDate(self, dt: datetime, _info):
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
