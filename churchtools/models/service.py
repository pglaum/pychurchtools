from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class Service(BaseModel):
    id: int
    name: str
    serviceGroupId: int
    commentOnConfirmation: bool
    sortKey: int
    allowDecline: bool
    allowExchange: bool
    comment: str
    standard: bool
    hidePersonName: bool
    sendReminderMails: bool
    sendServiceRequestMails: bool | None = None
    allowControlLiveAgenda: bool
    groupIds: str | None = None
    tagIds: str | None = None
    calTextTemplate: str
    allowChat: bool

    def __repr__(self) -> str:
        return f"<Service: {self.name} [{self.id}]>"


class ServiceGroup(BaseModel):
    id: int
    name: str
    sortKey: int
    viewAll: bool | None = None
    campusId: int | None = None
    onlyVisibleInCampusFilter: bool | None = None

    def __repr__(self) -> str:
        return f"<ServiceGroup: {self.name} [{self.id}]>"


class ServiceRequest(BaseModel):
    id: int
    personId: int
    name: str
    serviceId: int
    agreed: bool
    isValid: bool
    requestedDate: datetime
    requesterPersonId: int
    comment: str
    counter: int

    # TODO: person
    # TODO: requesterPerson

    def __repr__(self) -> str:
        return f"<ServiceRequest: {self.name} {self.serviceId} [{self.id}]>"
