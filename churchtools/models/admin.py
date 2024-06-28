from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class LogEntry(BaseModel):
    date: datetime
    domainId: int
    domainType: str
    id: int
    level: int
    message: str
    personId: int
    simulatePersonId: Optional[int] = None
