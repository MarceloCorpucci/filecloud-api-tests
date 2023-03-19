import pytest
from lib.loader import load_groups
from lib.creator import create_group, delete_group_using


@pytest.fixture()
def group_data():
    yield load_groups()[0]
    delete_group_using(load_groups()[0])


@pytest.fixture()
def groups_data():
    yield load_groups()
    for group in load_groups():
        delete_group_using(group)


@pytest.fixture()
def persisted_group():
    create_group([load_groups()[0]])
    yield load_groups()[0]
    delete_group_using(load_groups()[0])


@pytest.fixture()
def groups_to_be_deleted():
    for group in load_groups():
        create_group([group])
    yield load_groups()
