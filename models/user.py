from sqlalchemy import Column,Integer,String
from .base import Base #import the shared Base

#the user model reps a user in the system
class User(Base):
    __tablename__='users'
    #unique id for each user
    id=Column(Integer,primary_key=True)
    #unique username for each user
    username=Column(String,unique=True,nullable=False)
    #unique email for each user
    email=Column(String,unique=True,nullable=False)