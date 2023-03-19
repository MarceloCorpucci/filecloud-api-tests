from lib import creator
from lib import loader
from hamcrest.core import assert_that
from hamcrest import is_, contains_string


def test_create_single_user(single_user_data):
    responses = creator.create_user([single_user_data])
    for response in responses:
        assert_that(response.status_code, is_(200))


def test_create_users(user_data):
    responses = creator.create_user(user_data)
    for response in responses:
        assert_that(response.status_code, is_(200))


def test_get_user(single_user):
    response = creator.get_user(single_user)
    assert_that(response.text, contains_string(loader.load_users()[0]['username'].lower()))


def test_delete_user(user_to_be_deleted):
    response = creator.delete_user({'profile': user_to_be_deleted})
    assert_that(response.status_code, is_(200))


