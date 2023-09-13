from pydantic import BaseModel, EmailStr
from datetime import date


class ContactBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    phone: str
    birthdate: date
    otherinform: str


# class ContactCreate(ContactBase):
#     pass


class ContactUpdate(ContactBase):
    email: EmailStr
    phone: str


class ContactResponse(ContactBase):
    id: int
    # firstname: str
    # lastname: str
    # email: EmailStr

    class Config:
        orm_mode = True