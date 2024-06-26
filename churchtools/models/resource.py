from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import BaseModel

from churchtools.models.calendar import AppointmentMeta, CalendarMeta


class BookingAdditional(BaseModel):
    date: Union[date, datetime]
    id: int
    isRepeated: Optional[bool] = None
    meta: CalendarMeta


class ResourceType(BaseModel):
    campusId: Optional[int] = None
    id: int
    name: str
    nameTranslated: str
    sortKey: int


class Resource(BaseModel):
    adminIds: Optional[List[int]] = None
    doesRequireCalEntry: bool
    iCalLocation: Optional[str] = None
    id: int
    isAutoAccept: bool
    isVirtual: bool
    location: Optional[str] = None
    name: str
    nameTranslated: str
    randomString: str
    resourceTypeId: int
    sortKey: int


class Booking(BaseModel):
    additionals: List[BookingAdditional]
    allDay: bool
    calId: Optional[int] = None
    caption: str
    endDate: Union[date, datetime]
    exceptions: List[BookingAdditional]
    id: int
    location: Optional[str] = None
    meta: Optional[AppointmentMeta] = None
    note: Optional[str] = None
    personId: Optional[int] = None
    repeatFrequency: Optional[int] = None
    repeatId: int
    repeatOption: Optional[int] = None
    repeatUntil: Optional[str] = None
    resource: Resource
    showInCal: bool
    startDate: Union[date, datetime]
    statusId: int
    version: int
