from fastapi import FastAPI, Depends, status, HTTPException, Query
from src.database.db import get_db
from sqlalchemy.orm import Session
from src.schemas import ContactResponse, ContactUpdate
from src.database.models import Contact
from typing import List
from datetime import date, timedelta


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/contacts/{params}", response_model=list[ContactResponse], tags=['contacts'])
async def search_contacts(
    db: Session = Depends(get_db),
    firstname_: str = Query(None, description="Firstname: "),
    lastname_: str = Query(None, description="Lastname: "),
    email_: str = Query(None, description="Email: "),
):       
    if firstname_:
        contacts = db.query(Contact).filter(Contact.firstname==firstname_).all()
    elif lastname_:
        contacts = db.query(Contact).filter(Contact.lastname==lastname_).all()
    elif email_:
        contacts = db.query(Contact).filter(Contact.email==email_).all()
    else:
        contacts = db.query(Contact).all()

    return contacts

@app.post("/contacts", response_model=ContactResponse, tags=["contacts"])
async def create_contact(body: ContactResponse, db: Session = Depends(get_db)):
    contact = Contact(**body.model_dump())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

@app.get("/contacts", response_model=list[ContactResponse], tags=['contacts'])
async def get_contacts(db: Session = Depends(get_db)):
    contacts = db.query(Contact).all()
    return contacts    

@app.get("/contacts/{contact_id}", response_model=ContactResponse, tags=['contacts'])
async def get_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact 

@app.patch("/contacts/{contact_id}", response_model=ContactResponse, tags=['contacts'])
async def update_contact(
    contact_id: int, body: ContactUpdate, db: Session = Depends(get_db)
):
    contact = (db.query(Contact).filter_by(id=contact_id).first()
    )
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")

    contact.email = body.email
    contact.phone = body.phone

    db.commit()
    return contact  

@app.get("/contacts/{birthday}", response_model=list[ContactResponse], tags=['contacts'])
async def get_birthday(db: Session = Depends(get_db)):
    todaydate = date.today()
    nextdate = todaydate + timedelta(days=6)

    contact = (db.query(Contact).filter(((Contact.birthdate) <= nextdate)&((Contact.birthdate) >= todaydate)).all())
    
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")

    return contact


@app.delete("/contacts/{contact_id}", status_code=status.HTTP_204_NO_CONTENT, tags=['contacts'])
async def remove_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = (db.query(Contact).filter_by(id=contact_id).first()
    )
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    db.delete(contact)
    db.commit()
    return contact

# @app.get("/contacts/{params}", response_model=list[ContactResponse], tags=['contacts'])
# async def search_contacts(
#     db: Session = Depends(get_db),
#     firstname_: str = Query(None, description="Firstname: "),
#     lastname_: str = Query(None, description="Lastname: "),
#     email_: str = Query(None, description="Email: "),
# ):    
    
#     # if firstname_:
#     #     contacts = db.query(Contact).filter(Contact.firstname==firstname_).all()
#     # elif lastname_:
#     #     contacts = db.query(Contact).filter(Contact.lastname==lastname_).all()
#     # elif email_:
#     #     contacts = db.query(Contact).filter(Contact.email==email_).all()
#     # else:
#     contacts = db.query(Contact).all()

#     return contacts

