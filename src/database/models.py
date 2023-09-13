from sqlalchemy import Column, Integer, String, Date
# from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(50), nullable=False, index=True)
    lastname = Column(String(50), index=True)
    email = Column(String(40), unique=True, index=True)
    phone = Column(String(50), index=True)
    birthdate = Column('birth', Date)
    otherinform = Column(String(150), nullable=True)
    