from typing import Optional

from pydantic import BaseModel


class Pagination(BaseModel):
    total: int
    current: int
    limit: int
    lastPage: int


class MetaPagination(BaseModel):
    count: int
    pagination: Optional[Pagination] = None
