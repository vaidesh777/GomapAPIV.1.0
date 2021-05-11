from datetime import datetime, date


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

class CitySchema(BaseModel):
    id: int
    builder_id: int
    package_id: int
    start_date: date
    end_date: date
    price: int
    extra: datetime
    extras: datetime

