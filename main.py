from lib import loader
from lib import creator
from lib.support import converter


if __name__ == '__main__':
    creator.create_user(loader.load_users())
    creator.create_group(loader.load_groups())
    assignation_data = converter.make_field_lower_case_in_users_per_group(loader.load_users_per_groups())
    creator.add_user_to_group(assignation_data)
