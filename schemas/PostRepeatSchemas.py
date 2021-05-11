from pydantic.main import BaseModel


class PostRepeatSchema(BaseModel):
    id = int
    sch_id = str
    message = str
    images = int
    email = str
    mobile = str
    created = int

