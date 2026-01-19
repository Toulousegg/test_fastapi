from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    email: str
    senha: str
    fullname : str

    class Config:
        from_attributes = True 

class orderschema(BaseModel):
    title: str
    description: str

    class Config:
        from_attributes = True

class loginschema(BaseModel):
    email: str
    password: str

    class Config:
        from_attribuites = True