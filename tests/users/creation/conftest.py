import pytest
from lib.loader import load_users
from lib.creator import create_user, delete_user


@pytest.fixture()
def single_user_data():
    yield load_users()[0]
    profile = load_users()[0]['username'].lower()
    delete_user({'profile': profile})


@pytest.fixture()
def user_data():
    yield load_users()
    for user in load_users():
        profile = user['username'].lower()
        delete_user({'profile': profile})


@pytest.fixture()
def user_to_be_deleted():
    create_user([load_users()[0]])
    return load_users()[0]['username'].lower()


@pytest.fixture()
def single_user():
    create_user([load_users()[0]])
    profile = load_users()[0]['username'].lower()
    yield {'username': profile}
    delete_user({'profile': profile})
