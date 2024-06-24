from datetime import date, datetime
from typing import Any, Dict, Generator, Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel


class Status(BaseModel):
    id: int
    name: str
    shorty: str
    isMember: bool
    isSearchable: bool
    sortKey: int
    securityLevelId: int
