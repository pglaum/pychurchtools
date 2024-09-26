from __future__ import annotations

from pydantic import BaseModel


class Pagination(BaseModel):
    total: int
    current: int
    limit: int
    lastPage: int


class MetaPagination(BaseModel):
    count: int
    pagination: Pagination | None = None
