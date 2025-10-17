import pytest

from services.order_item_service import OrderItemService
from services.user_service import UserService
from services.product_service import ProductService
from services.order_service import OrderService


@pytest.fixture
def order_item_service():
    return OrderItemService()


@pytest.fixture
def user_service():
    return UserService()


@pytest.fixture
def product_service():
    return ProductService()


@pytest.fixture
def order_service():
    return OrderService()


def seed_user_product_order(session, user_service, product_service, order_service):
    user = user_service.create_user(session, username="alice", email="alice@example.com")
    product1 = product_service.create_product(session, name="Widget", price=10.0, stock_quantity=100)
    product2 = product_service.create_product(session, name="Gadget", price=20.0, stock_quantity=50)
    order = order_service.create_order(session, user_id=user.id)
    return user, product1, product2, order


def test_add_list_get_update_delete_order_items(session, order_item_service, user_service, product_service, order_service):
    user, product1, product2, order = seed_user_product_order(session, user_service, product_service, order_service)

    # add two items to the order
    item1 = order_item_service.add_order_item(session, order_id=order.id, product_id=product1.id, quantity=2)
    item2 = order_item_service.add_order_item(session, order_id=order.id, product_id=product2.id, quantity=1)

    assert item1.id is not None
    assert item1.order_id == order.id
    assert item1.product_id == product1.id
    assert item1.quantity == 2

    # list all
    all_items = order_item_service.list_order_items(session)
    assert len(all_items) == 2

    # list filtered by order
    order_items = order_item_service.list_order_items(session, order_id=order.id)
    assert len(order_items) == 2
    assert {i.id for i in order_items} == {item1.id, item2.id}

    # get single
    fetched = order_item_service.get_order_item(session, item1.id)
    assert fetched is item1

    # update quantity
    order_item_service.update_order_item(session, item1.id, quantity=3)
    assert item1.quantity == 3

    # update product reference
    order_item_service.update_order_item(session, item1.id, product_id=product2.id)
    assert item1.product_id == product2.id

    # delete second item
    order_item_service.delete_order_item(session, item2.id)
    session.flush()
    assert order_item_service.get_order_item(session, item2.id) is None

    remaining = order_item_service.list_order_items(session, order_id=order.id)
    assert len(remaining) == 1
    assert remaining[0].id == item1.id


def test_add_invalid_quantity(session, order_item_service, user_service, product_service, order_service):
    user, product1, _, order = seed_user_product_order(session, user_service, product_service, order_service)

    with pytest.raises(ValueError):
        order_item_service.add_order_item(session, order_id=order.id, product_id=product1.id, quantity=0)
    with pytest.raises(ValueError):
        order_item_service.add_order_item(session, order_id=order.id, product_id=product1.id, quantity=-1)


def test_update_invalid_quantity_and_not_found(session, order_item_service, user_service, product_service, order_service):
    user, product1, product2, order = seed_user_product_order(session, user_service, product_service, order_service)

    item = order_item_service.add_order_item(session, order_id=order.id, product_id=product1.id, quantity=2)

    # invalid quantity
    with pytest.raises(ValueError):
        order_item_service.update_order_item(session, item.id, quantity=0)
    with pytest.raises(ValueError):
        order_item_service.update_order_item(session, item.id, quantity=-5)

    # not found cases
    with pytest.raises(ValueError):
        order_item_service.update_order_item(session, 99999, product_id=product2.id)
    with pytest.raises(ValueError):
        order_item_service.delete_order_item(session, 99999)
