from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

#the product model reps items that are on sale in the shop
class Product(Base):
    __tablename__='products'
    #unique id for each product
    id=Column(Integer,primary_key=True)
    #name of product
    name=Column(String,nullable=False)
    #price of product
    price=Column(Float,nullable=False)
    #no of products in stock
    stock_quantity=Column(Integer,nullable=False)
