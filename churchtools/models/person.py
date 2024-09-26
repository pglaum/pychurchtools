from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel  # type: ignore

from . import EmptyStrToNone


class Person(BaseModel):
    id: int | None = None
    securityLevelForPerson: int | None = None
    editSecurityLevelForPerson: int | None = None
    title: str | None = None
    firstName: str | None = None
    lastName: str | None = None
    nickname: str | None = None
    job: str | None = None
    street: str | None = None
    addressAddition: str | None = None
    zip: str | None = None
    city: str | None = None
    country: str | None = None
    latitude: EmptyStrToNone[float] | None = None
    longitude: EmptyStrToNone[float] | None = None
    latitudeLoose: EmptyStrToNone[float] | None = None
    longitudeLoose: EmptyStrToNone[float] | None = None
    phonePrivate: str | None = None
    phoneWork: str | None = None
    mobile: str | None = None
    fax: str | None = None
    birthName: str | None = None
    birthday: EmptyStrToNone[date] | None = None
    birthplace: str | None = None
    imageUrl: str | None = None
    familyImageUrl: str | None = None
    sexId: int | None = None
    email: str | None = None
    cmsUserId: str | None = None
    optigemUserId: str | None = None
    nationalityId: int | None = None
    familyStatusId: int | None = None
    weddingDate: EmptyStrToNone[date] | None = None
    campusId: int | None = None
    statusId: int | None = None
    departmentIds: list[int] | None = None
    firstContact: EmptyStrToNone[datetime] | None = None
    dateOfBelonging: EmptyStrToNone[date] | None = None
    dateOfEntry: EmptyStrToNone[datetime] | None = None
    dateOfResign: EmptyStrToNone[datetime] | None = None
    dateOfBaptism: EmptyStrToNone[date] | None = None
    placeOfBaptism: str | None = None
    baptisedBy: str | None = None
    referredBy: str | None = None
    referredTo: str | None = None
    growPathId: int | None = None
    isArchived: bool | None = None

    # TODO: privacyPolicyAgreement
    # TODO: meta

    def __repr__(self) -> str:
        return f"<Person: {self.firstName} {self.lastName} [{self.id}]>"


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
    imageUrl: str | None = None
    domainAttributes: BirthdayPersonDomainAttributes

    def __repr__(self) -> str:
        return f"<BirthdayPerson: {self.title}>"


class Birthday(BaseModel):
    type: str
    date: date
    age: int | None = None
    person: BirthdayPerson

    def __repr__(self) -> str:
        return f"<Birthday: {self.person.title} {self.date} " f"({self.age} years)>"


class Device(BaseModel):
    id: str
    type: str
    ttl: datetime
    version: str
    createdAt: datetime
    updatedAt: datetime
