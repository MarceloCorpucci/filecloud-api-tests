from lib import creator
from hamcrest.core import assert_that
from hamcrest import is_


def test_user_assignation_to_a_new_group(new_users_per_new_group):
    responses = creator.add_user_to_group(new_users_per_new_group)
    for response in responses:
        assert_that(response.status_code, is_(200))


def test_user_assignation_to_an_existing_group(new_users_per_existing_group):
    responses = creator.add_user_to_group(new_users_per_existing_group)
    for response in responses:
        assert_that(response.status_code, is_(200))
