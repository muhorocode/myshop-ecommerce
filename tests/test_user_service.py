import pytest

from services.user_service import UserService
from models.user import User


@pytest.fixture
def user_service():
    return UserService()


def test_create_user_success(session, user_service):
    user = user_service.create_user(session, username="alice", email="alice@example.com")
    assert user.id is not None
    assert user.username == "alice"
    assert user.email == "alice@example.com"


def test_create_user_invalid(session, user_service):
    with pytest.raises(ValueError):
        user_service.create_user(session, username="", email="alice@example.com")
    with pytest.raises(ValueError):
        user_service.create_user(session, username="alice", email="")


def test_list_users_and_limit(session, user_service):
    # seed
    for i in range(5):
        user_service.create_user(session, username=f"user{i}", email=f"user{i}@example.com")
    session.commit()

    all_users = user_service.list_users(session)
    assert len(all_users) == 5
    assert [u.username for u in all_users] == ["user0", "user1", "user2", "user3", "user4"]

    limited = user_service.list_users(session, limit=2)
    assert len(limited) == 2
    assert [u.username for u in limited] == ["user0", "user1"]


def test_get_update_delete_user(session, user_service):
    u = user_service.create_user(session, username="bob", email="bob@example.com")

    fetched = user_service.get_user(session, u.id)
    assert fetched is u

    # update
    user_service.update_user(session, u.id, username="bobby", email="bobby@example.com")
    assert u.username == "bobby"
    assert u.email == "bobby@example.com"

    # delete
    user_service.delete_user(session, u.id)
    session.flush()
    assert user_service.get_user(session, u.id) is None


def test_update_delete_not_found(session, user_service):
    with pytest.raises(ValueError):
        user_service.update_user(session, 999, username="nope")
    with pytest.raises(ValueError):
        user_service.delete_user(session, 999)
