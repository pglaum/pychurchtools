from typing import Any, Generator, Generic, Optional, TypeVar

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


class EmptyStrToFalse(Generic[PydanticField]):
    @classmethod
    def __get_validators__(cls) -> Generator:
        yield cls.validate

    @classmethod
    def validate(cls, v: PydanticField, field: Any) -> bool:
        if v == "" or not v:
            return False
        return True
