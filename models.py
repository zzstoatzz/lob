from pydantic import BaseModel, Field
from pydantic_extra_types.pendulum_dt import DateTime


class User(BaseModel):
    name: str
    email: str
    signup: DateTime = Field(default_factory=DateTime.now)
