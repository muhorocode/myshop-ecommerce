"""This provides for the SQLAlchemy Engine,SessionLocal: session factory,
get_session(): context manager yielding a Session, test_connection(): quick connectivity check (returns True/False)"""

from contextlib import contextmanager #used to create the context manager(get_session)
import os #used to read the DATABASE_URL env variable

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

#read the DATABASE_URL from the env if present else use the default value
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:password@localhost:5432/myshop_db",
)

#create the engine the echo keeps the sql output quiet for now, future=true enables SQLAlchemy 2.0 style usage
engine = create_engine(DATABASE_URL, echo=False, future=True)

#the session factory for how SQLAlchemy keeps a unit of work and tracks changes to objects
SessionLocal = sessionmaker(bind=engine, autoflush=True, autocommit=False, expire_on_commit=False)


#creates a session
@contextmanager
def get_session() -> Session:

    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

#return true if able to connect to the db else false
def test_connection() -> bool:
    try:
        with engine.connect() as conn:
            return True
    except Exception:
        return False
