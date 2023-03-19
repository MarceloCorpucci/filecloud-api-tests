from lib import creator, loader
from hamcrest.core import assert_that
from hamcrest import is_, contains_string


def test_create_single_group(group_data):
    responses = creator.create_group([group_data])
    for response in responses:
        assert_that(response.status_code, is_(200))


def test_create_groups(groups_data):
    responses = creator.create_group(groups_data)
    for response in responses:
        assert_that(response.status_code, is_(200))


def test_get_group_by_name(persisted_group):
    response = creator.get_group_by_name(persisted_group)
    assert_that(response.text, contains_string(loader.load_groups()[0]['groupname']))


def test_delete_group(groups_to_be_deleted):
    for group in groups_to_be_deleted:
        response = creator.delete_group_using(group)
        assert_that(response.status_code, is_(200))
