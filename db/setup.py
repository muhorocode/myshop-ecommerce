from sqlalchemy import create_engine

#import for the models and their Base class

from models.base import Base
from models.user import User
from models.product import Product
from models.order import Order
from models.order_item import OrderItem

#db conn url

DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost:5432/myshop_db"

# connect to postgresql db and create all tables defined in the models
def create_tables():
    #create the db engine (conn to the db)
    engine=create_engine(DATABASE_URL)
    #create all the tables in the db(if not existing)
    Base.metadata.create_all(engine)
    print("All tables created successfully!")

if __name__ == "__main__":
    create_tables()
    

