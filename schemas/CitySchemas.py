from typing import Optional

from pydantic.main import BaseModel


class CitySchema(BaseModel):
    id: Optional[int] = None
    name: str
