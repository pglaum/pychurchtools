from typing import Dict, List, Optional

from pydantic import BaseModel

from churchtools.models.group import AgeGroup
from churchtools.models.person import PersonDomainObject


class GroupHomepageDomainAttributes(BaseModel):
    childGroupIds: Optional[List[int]] = None


class GroupHomepageSimple(BaseModel):
    apiUrl: Optional[str] = None
    domainAttributes: Optional[GroupHomepageDomainAttributes] = None
    frontendUrl: Optional[str] = None
    icon: Optional[str] = None
    imageUrl: Optional[str] = None
    title: Optional[str] = None

    def get_hash(self) -> str:
        if self.apiUrl:
            return self.apiUrl.split("/")[-1]

        return ""


class GroupInformation(BaseModel):
    ageGroups: Optional[List[AgeGroup]] = None
    campus: Optional[Dict] = None
    groupCategory: Optional[Dict] = None
    groupPlaces: Optional[List[Dict]] = None
    imageUrl: Optional[str] = None
    leader: Optional[List[PersonDomainObject]] = None
    meetingTime: Optional[str] = None
    note: Optional[str] = None
    targetGroup: Optional[Dict] = None
    weekday: Optional[Dict] = None


class GroupDetail(BaseModel):
    allowWaitinglist: Optional[bool] = None
    autoAccept: Optional[bool] = None
    canSignUp: Optional[bool] = None
    children: Optional[List[int]] = None
    currentMemberCount: Optional[int] = None
    id: Optional[int] = None
    information: Optional[GroupInformation] = None
    maxMemberCount: Optional[int] = None
    name: Optional[str] = None
    requestedPlacesCount: Optional[int] = None
    requestedWaitinglistPlacesCount: Optional[int] = None
    signUpConditions: Optional[Dict] = None
    signUpHeadline: Optional[str] = None
    signUpPersons: Optional[Dict] = None


class GroupHomepage(BaseModel):
    defaultView: Optional[str] = None
    filter: Optional[List[Dict]] = None
    groups: List[GroupDetail]
    id: Optional[int] = None
    isEnabled: Optional[bool] = None
    meta: Optional[Dict] = None
    orderDirection: Optional[str] = None
    parentGroup: Optional[int] = None
    randomUrl: Optional[str] = None
    showFilter: Optional[bool] = None
    showGroups: Optional[bool] = None
    showLeader: Optional[bool] = None
    showMap: Optional[bool] = None
    sortBy: Optional[str] = None
