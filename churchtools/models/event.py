from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel  # type: ignore


class AgendaSong(BaseModel):
    songId: int
    arrangementId: int
    title: str
    arrangement: str
    category: str
    key: str
    bpm: str
    defaultArrangement: str | None = None


class AgendaItem(BaseModel):
    id: int
    position: int
    type: str
    title: str
    note: str | None = None
    duration: int
    start: datetime
    isBeforeEvent: bool
    song: AgendaSong | None = None

    # TODO: responsible
    # TODO: serviceGroupNotes
    # TODO: meta


class Agenda(BaseModel):
    id: int
    name: str
    series: str
    isFinal: bool
    calendarId: int
    total: int
    items: list[AgendaItem]

    # TODO: meta

    def __repr__(self) -> str:
        return f"<Agenda: {self.name} [{self.id}]>"


class EventService(BaseModel):
    id: int
    name: str | None = None
    serviceId: int
    agreed: bool
    isValid: bool
    requestedDate: datetime
    comment: str
    counter: int
    allowChat: bool

    # TODO: person
    # TODO: requesterPerson

    def __repr__(self) -> str:
        return f"<EventService: {self.name}>"


class Event(BaseModel):
    id: int
    guid: str
    name: str
    description: str | None = None
    startDate: datetime
    endDate: datetime
    chatStatus: str
    eventServices: list[EventService] | None = None

    # TODO: permissions
    # TODO: calendar

    def __repr__(self) -> str:
        return (
            f"<Event: {self.startDate.day:02}."
            f"{self.startDate.month:02} {self.startDate.hour:02}:"
            f'{self.startDate.minute:02} "{self.name}" [{self.id}]>'
        )
