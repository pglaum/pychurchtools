from __future__ import annotations

from pydantic import BaseModel  # type: ignore


class Department(BaseModel):
    id: int
    name: str
    nameTranslated: str | None = None
    sortKey: int

    def __repr__(self) -> str:
        return f"<Department: {self.name} [{self.id}]>"
