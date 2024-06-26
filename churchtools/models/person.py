from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel  # type: ignore

from . import EmptyStrToNone


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


class Device(BaseModel):
    id: str
    type: str
    ttl: datetime
    version: str
    createdAt: datetime
    updatedAt: datetime
