from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class LogEntry(BaseModel):
    date: datetime
    domainId: int
    domainType: str
    id: int
    level: int
    message: str
    personId: int
    simulatePersonId: int | None = None


class LoginPersonColor(BaseModel):
    key: str
    shade: int


class LoginPersonDomainAttributes(BaseModel):
    firstName: str
    guid: str | None = None
    lastName: str


class LoginPerson(BaseModel):
    apiUrl: str
    color: LoginPersonColor | None = None
    domainIdentifier: str
    frontendUrl: str
    imageUrl: str | None = None
    initials: str
    title: str
    domainAttributes: LoginPersonDomainAttributes
    domainType: str
    icon: str
    infos: list[str]


class LoginStatistic(BaseModel):
    lastLogin: datetime
    person: LoginPerson
    totalLogins: int


class SecurityLevel(BaseModel):
    id: int
    name: str
    sortkey: int
