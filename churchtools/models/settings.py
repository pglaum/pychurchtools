from __future__ import annotations

from pydantic import BaseModel


class Setting(BaseModel):
    module: str
    attribute: str
    value: dict | int | list | str

    def __repr__(self) -> str:
        return f"<Setting: {self.module}.{self.attribute} = {self.value}>"
