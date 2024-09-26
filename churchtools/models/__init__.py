from __future__ import annotations

from typing import Any, Generic, TypeVar
from collections.abc import Generator

PydanticField = TypeVar("PydanticField")


class EmptyStrToNone(Generic[PydanticField]):
    @classmethod
    def __get_validators__(cls) -> Generator:
        yield cls.validate

    @classmethod
    def validate(cls, v: PydanticField, field: Any) -> PydanticField | None:
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
