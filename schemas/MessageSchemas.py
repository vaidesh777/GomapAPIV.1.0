from typing import Optional

from pydantic.main import BaseModel


class message(BaseModel):
    id = int
    device = str
    groups = str
    message_id = int
    message = str
    images = str
    schedule = int
    status = int
    created = int