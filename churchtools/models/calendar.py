from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import BaseModel, field_serializer  # type: ignore

from . import EmptyStrToNone


class CalendarMeta(BaseModel):
    modifiedDate: Union[date, datetime]
    modifiedPid: int


class Calendar(BaseModel):
    campusId: Optional[int] = None
    color: str
    eventTemplateId: Optional[int] = None
    iCalSourceUrl: Optional[str] = None
    id: int
    isPrivate: bool
    isPublic: bool
    meta: Optional[CalendarMeta] = None
    name: str
    nameTranslated: str
    randomUrl: str
    sortKey: int


class Address(BaseModel):
    meetingAt: Optional[str] = None
    street: Optional[str] = None
    addition: Optional[str] = None
    district: Optional[str] = None
    zip: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[EmptyStrToNone[float]] = None
    longitude: Optional[EmptyStrToNone[float]] = None


class AppointmentAddition(BaseModel):
    date: Union[date, datetime]
    isRepeated: Optional[bool] = False


class AppointmentException(BaseModel):
    date: Union[date, datetime]
    id: int
    meta: CalendarMeta


class PersonWithOnlyId(BaseModel):
    id: int


class AppointmentMeta(BaseModel):
    createdDate: Union[date, datetime]
    createdPerson: PersonWithOnlyId
    modifiedDate: Union[date, datetime]
    modifiedPerson: PersonWithOnlyId


class Appointment(BaseModel):
    additions: List[AppointmentAddition] = []
    address: Optional[Address] = None
    allDay: bool = False
    calendar: Optional[Calendar] = None
    caption: str
    endDate: Union[date, datetime]
    exceptions: List[AppointmentException] = []
    id: Optional[Union[int, str]] = None
    image: Optional[str] = None
    information: Optional[str] = None
    isInternal: bool = True
    link: Optional[str] = None
    meta: Optional[AppointmentMeta] = None
    note: Optional[str] = None
    onBehalfOfPid: Optional[int] = None
    startDate: Union[date, datetime]
    repeatFrequency: Optional[int] = None
    repeatId: int = 0
    repeatOption: Optional[int] = None
    repeatUntil: Optional[str] = None
    version: int = 0

    @field_serializer("startDate")
    def serialize_startDate(self, dt: datetime, _info):
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    @field_serializer("endDate")
    def serialize_endDate(self, dt: datetime, _info):
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
