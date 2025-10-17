import pytest

from services.order_service import OrderService
from services.user_service import UserService


@pytest.fixture
def order_service():
    return OrderService()


@pytest.fixture
def user_service():
    return UserService()


def test_create_list_get_update_delete_order(session, order_service, user_service):
    # We need a user to create an order
    user = user_service.create_user(session, username="chris", email="chris@example.com")

    order = order_service.create_order(session, user_id=user.id)
    assert order.id is not None
    assert order.user_id == user.id

    # list
    all_orders = order_service.list_orders(session)
    assert len(all_orders) == 1
    assert all_orders[0].id == order.id

    # update
    new_user = user_service.create_user(session, username="dana", email="dana@example.com")
    order_service.update_order(session, order.id, user_id=new_user.id)
    assert order.user_id == new_user.id

    # delete
    order_service.delete_order(session, order.id)
    session.flush()
    assert order_service.get_order(session, order.id) is None


def test_update_delete_not_found(session, order_service):
    with pytest.raises(ValueError):
        order_service.update_order(session, 999, user_id=1)
    with pytest.raises(ValueError):
        order_service.delete_order(session, 999)
