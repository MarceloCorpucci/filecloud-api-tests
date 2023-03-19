import logging
from lib.loader import load_config
from lib.executor import post_request
from lib.support import converter
from typing import List
from requests import Response


def create_user(user_details) -> List[Response]:
    endpoint = f"{load_config()['base_url']}/admin/adduser"
    responses: List[Response] = []

    for user_detail in user_details:
        response = post_request(url=endpoint, data=user_detail)
        logging.info(f"{response.status_code} | {response.text}")
        responses.append(response)

    return responses


def get_user(user_name) -> Response:
    endpoint = f"{load_config()['base_url']}/admin/getuser"
    response = post_request(url=endpoint, data=user_name)
    logging.info(f"{response.status_code} | {response.text}")

    return response


def delete_user(user_profile) -> Response:
    endpoint = f"{load_config()['base_url']}/admin/deleteuser"
    response = post_request(url=endpoint, data=user_profile)
    logging.info(f"{response.status_code} | {response.text}")
    return response


def create_group(group_details) -> List[Response]:
    endpoint = f"{load_config()['base_url']}/admin/addgroup"
    responses: List[Response] = []

    for dict_entry in group_details:
        for key, value in dict_entry.items():
            response = post_request(url=endpoint, data={key: value})
            logging.info(f"{response.status_code} | {response.text}")
            responses.append(response)

    return responses


def get_group_by_name(group_name) -> Response:
    endpoint = f"{load_config()['base_url']}/admin/getgroupbyname"
    response = post_request(url=endpoint, data=group_name)
    logging.info(f"{response.status_code} | {response.text}")

    return response


def get_group_id_using(group_name):
    response = get_group_by_name({'groupname': group_name})
    return converter.from_xml_response_to_dict(response)['groups']['group']['groupid']


def delete_group(group_id) -> Response:
    endpoint = f"{load_config()['base_url']}/admin/deletegroup"
    response = post_request(url=endpoint, data=group_id)
    logging.info(f"{response.status_code} | {response.text}")

    return response


def delete_group_using(group_name) -> Response:
    """
    Deletes a group by its name, which simplifies the process given the actual deletion requires a group id
    :param group_name: dict.
    :return: a Response object.
    """
    response = get_group_by_name(group_name)
    logging.info(f"Response in XML {response.text}")
    response_to_json = converter.from_xml_response_to_dict(response)
    return delete_group({'groupid': response_to_json['groups']['group']['groupid']})


def add_user_to_group(user_per_group) -> List[Response]:
    endpoint = f"{load_config()['base_url']}/admin/addmembertogroup"
    responses: List[Response] = []

    for entry in user_per_group:
        response = get_group_by_name(entry['groupname'])

        if "Group Does Not Exist" in response.text:
            create_group([{'groupname': entry['groupname']}])
            group_id = get_group_id_using(entry['groupname'])
            response = post_request(url=endpoint, data={'groupid': group_id,
                                                        'userid': entry['userid']})
            logging.info(f"{response.status_code} | {response.text}")
            responses.append(response)

        else:
            group_id = get_group_id_using(entry['groupname'])
            response = post_request(url=endpoint, data={'groupid': group_id,
                                                        'userid': entry['user_id']})
            logging.info(f"{response.status_code} | {response.text}")
            responses.append(response)

    return responses
