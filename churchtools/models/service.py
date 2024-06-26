from datetime import datetime
from typing import Optional

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
    sendServiceRequestMails: Optional[bool] = None
    allowControlLiveAgenda: bool
    groupIds: Optional[str] = None
    tagIds: Optional[str] = None
    calTextTemplate: str
    allowChat: bool

    def __repr__(self) -> str:
        return f"<Service: {self.name} [{self.id}]>"


class ServiceGroup(BaseModel):
    id: int
    name: str
    sortKey: int
    viewAll: Optional[bool] = None
    campusId: Optional[int] = None
    onlyVisibleInCampusFilter: Optional[bool] = None

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
