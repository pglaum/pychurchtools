from datetime import date, datetime
from typing import Generator, Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel  # type: ignore
from pydantic.fields import ModelField

PydanticField = TypeVar("PydanticField")


class EmptyStrToNone(Generic[PydanticField]):
    @classmethod
    def __get_validators__(cls) -> Generator:
        yield cls.validate

    @classmethod
    def validate(cls, v: PydanticField, field: ModelField) -> Optional[PydanticField]:
        if v == "":
            return None
        return v


class EmptyStrToFalse(Generic[PydanticField]):
    @classmethod
    def __get_validators__(cls) -> Generator:
        yield cls.validate

    @classmethod
    def validate(cls, v: PydanticField, field: ModelField) -> bool:
        if v == "" or not v:
            return False
        return True


class Person(BaseModel):

    id: int
    securityLevelForPerson: int
    editSecurityLevelForPerson: int
    title: Optional[str]
    firstName: Optional[str]
    lastName: Optional[str]
    nickname: Optional[str]
    job: Optional[str]
    street: Optional[str]
    addressAddition: Optional[str]
    zip: Optional[str]
    city: Optional[str]
    country: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    latidudeLoose: Optional[float]
    longitudeLoose: Optional[float]
    phonePrivate: Optional[str]
    phoneWork: Optional[str]
    mobile: Optional[str]
    fax: Optional[str]
    birthName: Optional[str]
    birthday: Optional[EmptyStrToNone[date]]
    birthplace: Optional[str]
    imageUrl: Optional[str]
    familyImageUrl: Optional[str]
    sexId: Optional[int]
    email: Optional[str]
    cmsUserId: Optional[str]
    optigemUserId: Optional[str]
    nationalityId: Optional[int]
    familyStatusId: Optional[int]
    weddingDate: Optional[EmptyStrToNone[date]]
    campusId: Optional[int]
    statusId: Optional[int]
    departmentIds: Optional[List[int]]
    firstContact: Optional[EmptyStrToNone[datetime]]
    dateOfBelonging: Optional[EmptyStrToNone[date]]
    dateOfEntry: Optional[EmptyStrToNone[datetime]]
    dateOfResign: Optional[EmptyStrToNone[datetime]]
    dateOfBaptism: Optional[EmptyStrToNone[date]]
    placeOfBaptism: Optional[str]
    baptisedBy: Optional[str]
    referredBy: Optional[str]
    referredTo: Optional[str]
    growPathId: Optional[int]
    isArchived: Optional[bool]

    # TODO: privacyPolicyAgreement
    # TODO: meta

    def __repr__(self) -> str:

        return f"<Person: {self.firstName} {self.lastName} [{self.id}]>"


class AgendaSong(BaseModel):

    songId: int
    arrangementId: int
    title: str
    arrangement: str
    category: str
    key: str
    bpm: str
    defaultArrangement: Optional[str]


class AgendaItem(BaseModel):

    id: int
    position: int
    type: str
    title: str
    note: Optional[str]
    duration: int
    start: datetime
    isBeforeEvent: bool
    song: Optional[AgendaSong]

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
    items: List[AgendaItem]

    # TODO: meta

    def __repr__(self) -> str:

        return f"<Agenda: {self.name} [{self.id}]>"


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
    sendServiceRequestMails: Optional[bool]
    allowControlLiveAgenda: bool
    groupIds: Optional[str]
    tagIds: Optional[str]
    calTextTemplate: str
    allowChat: bool

    def __repr__(self) -> str:

        return f"<Service: {self.name} [{self.id}]>"


class ServiceGroup(BaseModel):

    id: int
    name: str
    sortKey: int
    viewAll: Optional[bool]
    campusId: Optional[int]
    onlyVisibleInCampusFilter: Optional[bool]

    def __repr__(self) -> str:

        return f"<ServiceGroup: {self.name} [{self.id}]>"


class EventService(BaseModel):

    id: int
    name: Optional[str]
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
    description: str
    startDate: datetime
    endDate: datetime
    chatStatus: str
    eventServices: Optional[List[EventService]]

    # TODO: permissions
    # TODO: calendar

    def __repr__(self) -> str:

        return (
            f"<Event: {self.startDate.day:02}."
            f"{self.startDate.month:02} {self.startDate.hour:02}:"
            f'{self.startDate.minute:02} "{self.name}" [{self.id}]>'
        )


class GroupDomainAttributes(BaseModel):

    note: str


class Group(BaseModel):

    title: str
    domainType: str
    domainIdentifier: str
    apiUrl: str
    frontendUrl: str
    imageUrl: Optional[str]
    domainAttributes: GroupDomainAttributes

    def __repr__(self) -> str:

        return f"<Group: {self.title}>"


class ArrangementLink(BaseModel):

    domainType: str
    domainId: str
    name: str
    filename: str
    fileUrl: str


class ArrangementFile(BaseModel):

    domainType: str
    domainId: str
    name: str
    filename: str
    fileUrl: str


class Arrangement(BaseModel):

    id: int
    name: str
    isDefault: bool
    keyOfArrangement: str
    bpm: str
    beat: str
    duration: str
    note: str
    links: List[ArrangementLink]
    files: List[ArrangementFile]

    # TODO: meta


class SongCategory(BaseModel):

    id: int
    name: str
    nameTranslated: str
    sortKey: int
    campusId: Optional[int]


class Song(BaseModel):

    id: int
    name: str
    category: SongCategory
    shouldPractice: bool
    author: str
    ccli: str
    copyright: str
    note: str
    arrangements: List[Arrangement]

    # TODO: meta

    def __repr__(self) -> str:

        return f"<Song: {self.name} [{self.id}]>"


class VersionInfo(BaseModel):

    build: str
    version: str

    def __repr__(self) -> str:

        return f"<Version: {self.version} (build: {self.build})>"


class PersonTag(BaseModel):

    id: int
    name: str
    count: int


class PersonDomainAttributes(BaseModel):

    firstName: str
    lastName: str
    guid: str


class PersonDomainObject(BaseModel):

    domainAttributes: PersonDomainAttributes
    imageUrl: str
    frontendUrl: str
    apiUrl: str
    domainType: str
    title: str
    domainIdentifier: str


class PersonRelationship(BaseModel):

    relative: PersonDomainObject
    degreeOfRelationship: str
    relationshipName: str
    relationshipTypeId: int

    def __repr__(self) -> str:

        return (
            f"<Relationship: {self.relative.title} " f"({self.degreeOfRelationship})>"
        )


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
    campusId: Optional[int]
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
    text: Optional[str]
    onStartpage: EmptyStrToFalse[bool]
    redirectTo: Optional[str]
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
    imageUrl: Optional[str]
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
    imageUrl: Optional[str]
    domainAttributes: BirthdayPersonDomainAttributes

    def __repr__(self) -> str:

        return f"<BirthdayPerson: {self.title}>"


class Birthday(BaseModel):

    type: str
    date: date
    age: Optional[int]
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


class Department(BaseModel):

    id: int
    name: str
    nameTranslated: Optional[str]
    sortKey: int

    def __repr__(self) -> str:

        return f"<Department: {self.name} [{self.id}]>"


class SearchResult(BaseModel):

    apiUrl: str
    domainIdentifier: str
    domainType: str
    frontendUrl: str
    icon: str
    imageUrl: Optional[str]
    title: str

    # TODO: domainAttributes

    def __repr__(self) -> str:

        return f"<SearchResult: {self.title} [{self.domainType}]>"


class Calendar(BaseModel):

    campusId: Optional[int]
    color: str
    eventTemplateId: Optional[int]
    iCalSourceUrl: Optional[str]
    id: int
    isPrivate: bool
    isPublic: bool
    name: str
    nameTranslated: str
    randomUrl: str
    sortKey: int

    # TODO: meta


class Address(BaseModel):

    meetingAt: Optional[str]
    street: Optional[str]
    addition: Optional[str]
    district: Optional[str]
    zip: Optional[str]
    city: Optional[str]
    country: Optional[str]
    latitude: Optional[float]
    longitued: Optional[float]


class Appointment(BaseModel):
    id: Union[int, str]
    caption: str
    note: str
    address: Optional[Address]
    version: int
    calendar: Calendar
    information: Optional[str]
    image: Optional[str]
    link: str
    isInternal: bool
    startDate: Union[date, datetime]
    endDate: Union[date, datetime]
    allDay: bool
    repeatId: int
    repeatFrequency: Optional[int]
    repeatUntil: Optional[str]
    repeatOption: Optional[int]

    # TODO: additions, exceptions, meta
