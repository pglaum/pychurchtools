from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class LogEntry(BaseModel):
    date: datetime
    domainId: int
    domainType: str
    id: int
    level: int
    message: str
    personId: int
    simulatePersonId: Optional[int] = None


class LoginPersonColor(BaseModel):
    key: str
    shade: int


class LoginPersonDomainAttributes(BaseModel):
    firstName: str
    guid: Optional[str]
    lastName: str


class LoginPerson(BaseModel):
    apiUrl: str
    color: Optional[LoginPersonColor]
    domainIdentifier: str
    frontendUrl: str
    imageUrl: Optional[str]
    initials: str
    title: str
    domainAttributes: LoginPersonDomainAttributes
    domainType: str
    icon: str
    infos: List[str]


class LoginStatistic(BaseModel):
    lastLogin: datetime
    person: LoginPerson
    totalLogins: int
