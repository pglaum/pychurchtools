from datetime import date, datetime
from typing import Any, Dict, Generator, Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel


class Setting(BaseModel):
    module: str
    attribute: str
    value: Union[dict, int, List, str]

    def __repr__(self) -> str:
        return f"<Setting: {self.module}.{self.attribute} = {self.value}>"
