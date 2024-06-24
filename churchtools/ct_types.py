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
