import json
import xmltodict
from requests import Response


def from_xml_response_to_dict(response: Response) -> dict:
    """
    Takes a Response containing an XML body, decodes it and returns a JSON based dict.
    :param response
    :return: dict object
    """
    decoded_response = response.content.decode('utf-8')
    return json.loads(json.dumps(xmltodict.parse(decoded_response)))


def make_field_lower_case_in_users_per_group(data_array) -> []:
    """
    At the time to interact with the /admin/addmembertogroup endpoint
    we need all users names to be in lower case.
    :param data_array:
    :return: modified array
    """
    test_data = []
    for entry in data_array:
        test_data.append({'userid': entry['userid'].lower(), 'groupname': entry['groupname']})
    return test_data
