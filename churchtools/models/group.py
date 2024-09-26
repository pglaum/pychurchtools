from __future__ import annotations

from pydantic import BaseModel


class AgeGroup(BaseModel):
    end: int | None = None
    id: int
    name: str
    nameTranslated: str | None = None
    start: int | None = None
    sortKey: int | None = None


class GroupDomainAttributes(BaseModel):
    note: str


class Group(BaseModel):
    title: str
    domainType: str
    domainIdentifier: str
    apiUrl: str
    frontendUrl: str
    imageUrl: str | None = None
    domainAttributes: GroupDomainAttributes

    def __repr__(self) -> str:
        return f"<Group: {self.title}>"
