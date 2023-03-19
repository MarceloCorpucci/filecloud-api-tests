import pytest
from lib.support import converter
from lib.loader import load_users, load_groups, load_users_per_groups
from lib.creator import create_user, delete_user, create_group, delete_group_using


@pytest.fixture()
def new_users_per_new_group():
    create_user([load_users()[0]])
    create_user([load_users()[1]])
    user_id1 = load_users()[0]['username'].lower()
    user_id2 = load_users()[1]['username'].lower()

    create_group([load_groups()[0]])

    yield [{'userid': user_id1, 'groupname': load_groups()[0]['groupname']},
           {'userid': user_id2, 'groupname': load_groups()[0]['groupname']}]

    profile1 = load_users()[0]['username'].lower()
    profile2 = load_users()[1]['username'].lower()
    delete_user({'profile': profile1})
    delete_user({'profile': profile2})

    delete_group_using(load_groups()[0])


@pytest.fixture()
def new_users_per_existing_group():
    # user creation
    create_user(load_users())

    # user modification
    test_data = converter.make_field_lower_case_in_users_per_group(load_users_per_groups())

    yield test_data

    # test teardown
    profiles = []
    for prof_entry in load_users():
        profiles.append({'profile': prof_entry['username'].lower()})

    for profile in profiles:
        delete_user(profile)

    for group in load_groups():
        delete_group_using({'groupname': group['groupname']})
