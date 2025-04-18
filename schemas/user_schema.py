from bson import ObjectId
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Union

class UserSchema(BaseModel):
    id: Optional[Union[str, ObjectId]] = Field(alias="_id")
    name: str
    email: str

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
        "json_encoders": {ObjectId: str},
    }

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str

class UserOut(BaseModel):
    email: EmailStr
    name: str

class Token(BaseModel):
    access_token: str
    token_type: str
