import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base
# Import models so they are registered with Base.metadata before table creation
from models import user as _user_model  # noqa: F401
from models import product as _product_model  # noqa: F401
from models import order as _order_model  # noqa: F401
from models import order_item as _order_item_model  # noqa: F401


@pytest.fixture
def session():
    """
    Provides a fresh SQLAlchemy session backed by an in-memory SQLite database
    for each test. Ensures tables are created before tests and dropped after.
    """
    engine = create_engine("sqlite:///:memory:", future=True)
    Base.metadata.create_all(engine)

    TestingSessionLocal = sessionmaker(
        bind=engine, autoflush=True, autocommit=False, expire_on_commit=False
    )

    db = TestingSessionLocal()
    try:
        yield db
        db.commit()
    finally:
        db.close()
        Base.metadata.drop_all(engine)
