from datetime import date, datetime
from typing import Optional, Union

from pydantic import BaseModel  # type: ignore

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
    id: Union[int, str]
    caption: str
    note: Optional[str] = None
    address: Optional[Address] = None
    version: int
    calendar: Calendar
    information: Optional[str] = None
    image: Optional[str] = None
    link: Optional[str] = None
    isInternal: bool
    startDate: Union[date, datetime]
    endDate: Union[date, datetime]
    allDay: bool
    repeatId: int
    repeatFrequency: Optional[int] = None
    repeatUntil: Optional[str] = None
    repeatOption: Optional[int] = None

    # TODO: additions, exceptions, meta
