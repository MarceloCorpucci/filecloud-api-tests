import os
import json


def load_config() -> dict:
    env = os.getenv('CONFIG_FILE')
    return json.load(open(os.path.join(os.path.dirname(__file__), '..', 'config', env)))


def load_users() -> dict:
    users = os.getenv('USERS_FILE')
    return json.load(open(os.path.join(os.path.dirname(__file__), '..', 'config', users)))


def load_groups() -> dict:
    groups = os.getenv('GROUPS_FILE')
    return json.load(open(os.path.join(os.path.dirname(__file__), '..', 'config', groups)))


def load_users_per_groups() -> dict:
    users_per_groups = os.getenv('USERS_PER_GROUPS_FILE')
    return json.load(open(os.path.join(os.path.dirname(__file__), '..', 'config', users_per_groups)))
