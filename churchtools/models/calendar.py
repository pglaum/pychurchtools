from datetime import date, datetime
from typing import Optional, Union

from pydantic import BaseModel, field_serializer  # type: ignore

from . import EmptyStrToNone


class Calendar(BaseModel):
    campusId: Optional[int] = None
    color: str
    eventTemplateId: Optional[int] = None
    iCalSourceUrl: Optional[str] = None
    id: int
    isPrivate: bool
    isPublic: bool
    name: str
    nameTranslated: str
    randomUrl: str
    sortKey: int

    # TODO: meta


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


class Appointment(BaseModel):
    id: Optional[Union[int, str]] = None
    caption: str
    note: Optional[str] = None
    address: Optional[Address] = None
    version: int = 0
    calendar: Optional[Calendar] = None
    information: Optional[str] = None
    image: Optional[str] = None
    link: Optional[str] = None
    isInternal: bool = True
    startDate: Union[date, datetime]
    endDate: Union[date, datetime]
    allDay: bool = False
    repeatId: int = 0
    repeatFrequency: Optional[int] = None
    repeatUntil: Optional[str] = None
    repeatOption: Optional[int] = None

    @field_serializer("startDate")
    def serialize_startDate(self, dt: datetime, _info):
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    @field_serializer("endDate")
    def serialize_endDate(self, dt: datetime, _info):
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    # TODO: additions, exceptions, meta
