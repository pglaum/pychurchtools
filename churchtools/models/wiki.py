from __future__ import annotations

from pydantic import BaseModel

from . import EmptyStrToFalse


class WikiCategory(BaseModel):
    id: int
    name: str
    sortKey: int
    campusId: int | None = None
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
    text: str | None = None
    onStartpage: EmptyStrToFalse[bool]
    redirectTo: str | None = None
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
    imageUrl: str | None = None
    preview: str

    def __repr__(self) -> str:
        return f"<WikiSearchResult: {self.title} ({self.preview})>"
