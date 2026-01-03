from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    username: str
    email: str
    senha: str
    fullname : str

    class Config:
        from_attributes = True 