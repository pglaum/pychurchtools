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
    keyOfArrangement: str
    bpm: str
    beat: str
    duration: int
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
    author: str
    ccli: str
    copyright: str
    note: str
    arrangements: list[Arrangement]

    # TODO: meta

    def __repr__(self) -> str:
        return f"<Song: {self.name} [{self.id}]>"
