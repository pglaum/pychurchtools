from datetime import date, datetime
from typing import Any, Dict, Generator, Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel


class AgeGroup(BaseModel):
    end: Optional[int] = None
    id: int
    name: str
    nameTranslated: Optional[str] = None
    start: Optional[int] = None
    sortKey: Optional[int] = None


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
