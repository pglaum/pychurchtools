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


class Person(BaseModel):
    id: Optional[int] = None
    securityLevelForPerson: Optional[int] = None
    editSecurityLevelForPerson: Optional[int] = None
    title: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    nickname: Optional[str] = None
    job: Optional[str] = None
    street: Optional[str] = None
    addressAddition: Optional[str] = None
    zip: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[EmptyStrToNone[float]] = None
    longitude: Optional[EmptyStrToNone[float]] = None
    latitudeLoose: Optional[EmptyStrToNone[float]] = None
    longitudeLoose: Optional[EmptyStrToNone[float]] = None
    phonePrivate: Optional[str] = None
    phoneWork: Optional[str] = None
    mobile: Optional[str] = None
    fax: Optional[str] = None
    birthName: Optional[str] = None
    birthday: Optional[EmptyStrToNone[date]] = None
    birthplace: Optional[str] = None
    imageUrl: Optional[str] = None
    familyImageUrl: Optional[str] = None
    sexId: Optional[int] = None
    email: Optional[str] = None
    cmsUserId: Optional[str] = None
    optigemUserId: Optional[str] = None
    nationalityId: Optional[int] = None
    familyStatusId: Optional[int] = None
    weddingDate: Optional[EmptyStrToNone[date]] = None
    campusId: Optional[int] = None
    statusId: Optional[int] = None
    departmentIds: Optional[List[int]] = None
    firstContact: Optional[EmptyStrToNone[datetime]] = None
    dateOfBelonging: Optional[EmptyStrToNone[date]] = None
    dateOfEntry: Optional[EmptyStrToNone[datetime]] = None
    dateOfResign: Optional[EmptyStrToNone[datetime]] = None
    dateOfBaptism: Optional[EmptyStrToNone[date]] = None
    placeOfBaptism: Optional[str] = None
    baptisedBy: Optional[str] = None
    referredBy: Optional[str] = None
    referredTo: Optional[str] = None
    growPathId: Optional[int] = None
    isArchived: Optional[bool] = None

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
    defaultArrangement: Optional[str] = None


class AgendaItem(BaseModel):
    id: int
    position: int
    type: str
    title: str
    note: Optional[str] = None
    duration: int
    start: datetime
    isBeforeEvent: bool
    song: Optional[AgendaSong] = None

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


class EventService(BaseModel):
    id: int
    name: Optional[str] = None
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
    description: Optional[str] = None
    startDate: datetime
    endDate: datetime
    chatStatus: str
    eventServices: Optional[List[EventService]] = None

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
    imageUrl: Optional[str] = None
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
    duration: int
    note: str
    links: List[ArrangementLink]
    files: List[ArrangementFile]

    # TODO: meta


class SongCategory(BaseModel):
    id: int
    name: str
    nameTranslated: str
    sortKey: int
    campusId: Optional[int] = None


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


class Department(BaseModel):
    id: int
    name: str
    nameTranslated: Optional[str] = None
    sortKey: int

    def __repr__(self) -> str:
        return f"<Department: {self.name} [{self.id}]>"


class SearchResult(BaseModel):
    apiUrl: str
    domainIdentifier: str
    domainType: str
    frontendUrl: str
    icon: str
    imageUrl: Optional[str] = None
    title: str

    # TODO: domainAttributes

    def __repr__(self) -> str:
        return f"<SearchResult: {self.title} [{self.domainType}]>"


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


class AgeGroup(BaseModel):
    end: Optional[int] = None
    id: int
    name: str
    nameTranslated: Optional[str] = None
    start: Optional[int] = None
    sortKey: Optional[int] = None


class GroupHomepageDomainAttributes(BaseModel):
    childGroupIds: Optional[List[int]] = None


class GroupHomepageSimple(BaseModel):
    apiUrl: Optional[str] = None
    domainAttributes: Optional[GroupHomepageDomainAttributes] = None
    frontendUrl: Optional[str] = None
    icon: Optional[str] = None
    imageUrl: Optional[str] = None
    title: Optional[str] = None

    def get_hash(self) -> str:
        if self.apiUrl:
            return self.apiUrl.split("/")[-1]

        return ""


class GroupInformation(BaseModel):
    ageGroups: Optional[List[AgeGroup]] = None
    campus: Optional[Dict] = None
    groupCategory: Optional[str] = None
    groupPlaces: Optional[List[Dict]] = None
    imageUrl: Optional[str] = None
    leader: Optional[List[PersonDomainObject]] = None
    meetingTime: Optional[str] = None
    note: Optional[str] = None
    targetGroup: Optional[Dict] = None
    weekday: Optional[Dict] = None


class GroupDetail(BaseModel):
    allowWaitinglist: Optional[bool] = None
    autoAccept: Optional[bool] = None
    canSignUp: Optional[bool] = None
    children: Optional[List[int]] = None
    currentMemberCount: Optional[int] = None
    id: Optional[int] = None
    information: Optional[GroupInformation] = None
    maxMemberCount: Optional[int] = None
    name: Optional[str] = None
    requestedPlacesCount: Optional[int] = None
    requestedWaitinglistPlacesCount: Optional[int] = None
    signUpConditions: Optional[Dict] = None
    signUpHeadline: Optional[str] = None
    signUpPersons: Optional[Dict] = None


class GroupHomepage(BaseModel):
    defaultView: Optional[str] = None
    filter: Optional[List[Dict]] = None
    groups: List[GroupDetail]
    id: Optional[int] = None
    isEnabled: Optional[bool] = None
    meta: Optional[Dict] = None
    orderDirection: Optional[str] = None
    parentGroup: Optional[int] = None
    randomUrl: Optional[str] = None
    showFilter: Optional[bool] = None
    showGroups: Optional[bool] = None
    showLeader: Optional[bool] = None
    showMap: Optional[bool] = None
    sortBy: Optional[str] = None
