from __future__ import annotations

from pydantic import BaseModel


class Status(BaseModel):
    id: int
    name: str
    shorty: str
    isMember: bool
    isSearchable: bool
    sortKey: int
    securityLevelId: int
