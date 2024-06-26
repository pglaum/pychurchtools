from typing import Optional

from pydantic import BaseModel

from . import EmptyStrToFalse


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
