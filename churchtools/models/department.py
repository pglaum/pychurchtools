from typing import Optional

from pydantic import BaseModel  # type: ignore


class Department(BaseModel):
    id: int
    name: str
    nameTranslated: Optional[str] = None
    sortKey: int

    def __repr__(self) -> str:
        return f"<Department: {self.name} [{self.id}]>"
