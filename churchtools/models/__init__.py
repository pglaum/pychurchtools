from datetime import date, datetime
from typing import Any, Dict, Generator, Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel  # type: ignore

PydanticField = TypeVar("PydanticField")


class EmptyStrToNone(Generic[PydanticField]):
    @classmethod
    def __get_validators__(cls) -> Generator:
        yield cls.validate

    @classmethod
    def validate(cls, v: PydanticField, field: Any) -> Optional[PydanticField]:
        if v == "":
            return None
        return v
