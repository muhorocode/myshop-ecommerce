from sqlalchemy import Column, Integer, ForeignKey
from .base import Base

#the order_item model reps a product within a customer order

class OrderItem(Base):
    __tablename__='order_items'
    #unique id for each order item
    id=Column(Integer,primary_key=True)
    #link to the order this item belongs to
    order_id=Column(Integer,ForeignKey('orders.id'),nullable=False)
    #link to the product being ordered
    product_id=Column(Integer,ForeignKey('products.id'),nullable=False)
    #how many products of this type are in the order
    quantity=Column(Integer,nullable=False)