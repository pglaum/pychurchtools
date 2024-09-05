from __future__ import annotations

from pydantic import BaseModel

from churchtools.models.group import AgeGroup
from churchtools.models.person import PersonDomainObject


class GroupHomepageDomainAttributes(BaseModel):
    childGroupIds: list[int] | None = None


class GroupHomepageSimple(BaseModel):
    apiUrl: str | None = None
    domainAttributes: GroupHomepageDomainAttributes | None = None
    frontendUrl: str | None = None
    icon: str | None = None
    imageUrl: str | None = None
    title: str | None = None

    def get_hash(self) -> str:
        if self.apiUrl:
            return self.apiUrl.split("/")[-1]

        return ""


class GroupInformation(BaseModel):
    ageGroups: list[AgeGroup] | None = None
    campus: dict | None = None
    groupCategory: dict | None = None
    groupPlaces: list[dict] | None = None
    imageUrl: str | None = None
    leader: list[PersonDomainObject] | None = None
    meetingTime: str | None = None
    note: str | None = None
    targetGroup: dict | None = None
    weekday: dict | None = None


class GroupDetail(BaseModel):
    allowWaitinglist: bool | None = None
    autoAccept: bool | None = None
    canSignUp: bool | None = None
    children: list[int] | None = None
    currentMemberCount: int | None = None
    id: int | None = None
    information: GroupInformation | None = None
    maxMemberCount: int | None = None
    name: str | None = None
    requestedPlacesCount: int | None = None
    requestedWaitinglistPlacesCount: int | None = None
    signUpConditions: dict | None = None
    signUpHeadline: str | None = None
    signUpPersons: dict | None = None


class GroupHomepage(BaseModel):
    defaultView: str | None = None
    filter: list[dict] | None = None
    groups: list[GroupDetail]
    id: int | None = None
    isEnabled: bool | None = None
    meta: dict | None = None
    orderDirection: str | None = None
    parentGroup: int | None = None
    randomUrl: str | None = None
    showFilter: bool | None = None
    showGroups: bool | None = None
    showLeader: bool | None = None
    showMap: bool | None = None
    sortBy: str | None = None
