import pytest

from services.product_service import ProductService
from models.product import Product


@pytest.fixture
def product_service():
    return ProductService()


def test_create_product_success(session, product_service):
    product = product_service.create_product(session, name="Laptop", price=999.99, stock_quantity=10)
    assert product.id is not None
    assert product.name == "Laptop"
    assert product.price == 999.99
    assert product.stock_quantity == 10


def test_create_product_invalid(session, product_service):
    with pytest.raises(ValueError):
        product_service.create_product(session, name="", price=10.0, stock_quantity=1)
    with pytest.raises(ValueError):
        product_service.create_product(session, name="Phone", price=-1.0, stock_quantity=1)
    with pytest.raises(ValueError):
        product_service.create_product(session, name="Phone", price=1.0, stock_quantity=-5)


def test_list_products_and_limit(session, product_service):
    # seed
    for i in range(5):
        product_service.create_product(session, name=f"P{i}", price=float(i), stock_quantity=i)
    session.commit()

    all_products = product_service.list_products(session)
    assert len(all_products) == 5
    assert [p.name for p in all_products] == ["P0", "P1", "P2", "P3", "P4"]

    limited = product_service.list_products(session, limit=2)
    assert len(limited) == 2
    assert [p.name for p in limited] == ["P0", "P1"]


def test_get_update_delete_product(session, product_service):
    p = product_service.create_product(session, name="Tablet", price=100.0, stock_quantity=5)

    fetched = product_service.get_product(session, p.id)
    assert fetched is p

    # update
    product_service.update_product(session, p.id, name="Tab", price=120.0, stock_quantity=7)
    assert p.name == "Tab"
    assert p.price == 120.0
    assert p.stock_quantity == 7

    # reduce stock
    product_service.reduce_stock(session, p.id, 2)
    assert p.stock_quantity == 5

    # delete
    product_service.delete_product(session, p.id)
    session.flush()
    assert product_service.get_product(session, p.id) is None


def test_update_delete_not_found(session, product_service):
    with pytest.raises(ValueError):
        product_service.update_product(session, 999, name="X")
    with pytest.raises(ValueError):
        product_service.delete_product(session, 999)


def test_reduce_stock_errors(session, product_service):
    p = product_service.create_product(session, name="TV", price=200.0, stock_quantity=1)

    with pytest.raises(ValueError):
        product_service.reduce_stock(session, p.id, 0)
    with pytest.raises(ValueError):
        product_service.reduce_stock(session, p.id, -3)
    with pytest.raises(ValueError):
        product_service.reduce_stock(session, 12345, 1)
    with pytest.raises(ValueError):
        product_service.reduce_stock(session, p.id, 5)
