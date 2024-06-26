from typing import List, Union

from pydantic import BaseModel


class Setting(BaseModel):
    module: str
    attribute: str
    value: Union[dict, int, List, str]

    def __repr__(self) -> str:
        return f"<Setting: {self.module}.{self.attribute} = {self.value}>"
