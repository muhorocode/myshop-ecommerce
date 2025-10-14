from sqlalchemy import Column,Integer,ForeignKey,DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base=declarative_base()

#the order model reps a cutomer order in the system
class Order(Base):
    __tablename__='orders'
    #unique id for each order
    id=Column(Integer,primary_key=True)
    #link to the user who placed the order
    user_id=Column(Integer,ForeignKey('users.id'),nullable=False)
    #when the order was placed/created
    created_at=Column(DateTime,default=datetime.datetime.utcnow)