from __future__ import annotations

from pydantic import BaseModel  # type: ignore


class ArrangementLink(BaseModel):
    domainType: str
    domainId: str
    name: str
    filename: str
    fileUrl: str


class ArrangementFile(BaseModel):
    domainType: str
    domainId: str
    name: str
    filename: str
    fileUrl: str


class Arrangement(BaseModel):
    id: int
    name: str
    isDefault: bool
    keyOfArrangement: str | None = None
    bpm: int | None = None
    beat: str | None = None
    duration: int | None = None
    note: str
    links: list[ArrangementLink]
    files: list[ArrangementFile]

    # TODO: meta


class SongCategory(BaseModel):
    id: int
    name: str
    nameTranslated: str
    sortKey: int
    campusId: int | None = None


class Song(BaseModel):
    id: int
    name: str
    category: SongCategory
    shouldPractice: bool
    author: str | None = None
    ccli: str | None = None
    copyright: str | None = None
    note: str
    arrangements: list[Arrangement] | None = None
    tags: list[SongTag] | None = None

    # TODO: meta

    def __repr__(self) -> str:
        return f"<Song: {self.name} [{self.id}]>"


class SongTag(BaseModel):
    id: int
    name: str
    description: str | None = None
    color: str | None = None

    def __repr__(self) -> str:
        return f"<SongTag: {self.name} [{self.id}]>"
