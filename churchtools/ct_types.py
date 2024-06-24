from datetime import date, datetime
from typing import Any, Dict, Generator, Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel  # type: ignore

PydanticField = TypeVar("PydanticField")


class EmptyStrToNone(Generic[PydanticField]):
    @classmethod
    def __get_validators__(cls) -> Generator:
        yield cls.validate

    @classmethod
    def validate(cls, v: PydanticField, field: Any) -> Optional[PydanticField]:
        if v == "":
            return None
        return v


class EmptyStrToFalse(Generic[PydanticField]):
    @classmethod
    def __get_validators__(cls) -> Generator:
        yield cls.validate

    @classmethod
    def validate(cls, v: PydanticField, field: Any) -> bool:
        if v == "" or not v:
            return False
        return True


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


class GroupDomainAttributes(BaseModel):
    note: str


class Group(BaseModel):
    title: str
    domainType: str
    domainIdentifier: str
    apiUrl: str
    frontendUrl: str
    imageUrl: Optional[str] = None
    domainAttributes: GroupDomainAttributes

    def __repr__(self) -> str:
        return f"<Group: {self.title}>"


class Setting(BaseModel):
    module: str
    attribute: str
    value: Union[dict, int, List, str]

    def __repr__(self) -> str:
        return f"<Setting: {self.module}.{self.attribute} = {self.value}>"


class CTStatus(BaseModel):
    id: int
    name: str
    shorty: str
    isMember: bool
    isSearchable: bool
    sortKey: int
    securityLevelId: int


class WikiCategory(BaseModel):
    id: int
    name: str
    sortKey: int
    campusId: Optional[int] = None
    inMenu: bool
    fileAccessWithoutPermission: bool
    nameTranslated: str

    def __repr__(self) -> str:
        return f"<WikiCategory: {self.name} [{self.id}]>"


class WikiPermission(BaseModel):
    canEdit: bool


class WikiPage(BaseModel):
    identifier: str
    wikiCategory: WikiCategory
    title: str
    version: int
    text: Optional[str] = None
    onStartpage: EmptyStrToFalse[bool]
    redirectTo: Optional[str] = None
    permissions: WikiPermission
    isMarkdown: bool

    # TODO: meta

    def __repr__(self) -> str:
        return f"<WikiPage: {self.title} [{self.identifier}]>"


class WikiSearchResult(BaseModel):
    title: str
    domainType: str
    domainIdentifier: str
    apiUrl: str
    frontendUrl: str
    imageUrl: Optional[str] = None
    preview: str

    def __repr__(self) -> str:
        return f"<WikiSearchResult: {self.title} ({self.preview})>"


class BirthdayPersonDomainAttributes(BaseModel):
    firstName: str
    lastName: str
    guid: str


class BirthdayPerson(BaseModel):
    title: str
    domainType: str
    domainIdentifier: str
    apiUrl: str
    frontendUrl: str
    imageUrl: Optional[str] = None
    domainAttributes: BirthdayPersonDomainAttributes

    def __repr__(self) -> str:
        return f"<BirthdayPerson: {self.title}>"


class Birthday(BaseModel):
    type: str
    date: date
    age: Optional[int] = None
    person: BirthdayPerson

    def __repr__(self) -> str:
        return f"<Birthday: {self.person.title} {self.date} " f"({self.age} years)>"


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


class Device(BaseModel):
    id: str
    type: str
    ttl: datetime
    version: str
    createdAt: datetime
    updatedAt: datetime


class Pagination(BaseModel):
    total: int
    current: int
    limit: int
    lastPage: int


class MetaPagination(BaseModel):
    count: int
    pagination: Pagination
