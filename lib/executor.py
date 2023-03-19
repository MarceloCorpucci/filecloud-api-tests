import requests
from lib.loader import load_config
from requests import Response
from requests.cookies import RequestsCookieJar


def authorization_data() -> RequestsCookieJar:
    login_payload = {'adminuser': load_config()['username'], 'adminpassword': load_config()['password']}
    response = requests.post(f"{load_config()['base_url']}/admin/adminlogin", login_payload)

    token = response.cookies["X-XSRF-TOKEN"]
    token_admin = response.cookies["X-XSRF-TOKEN-admin"]
    tonidocloudah = response.cookies["tonidocloud-ah"]
    tonidocloudas = response.cookies["tonidocloud-as"]

    jar = RequestsCookieJar()
    jar.set('X-XSRF-TOKEN-admin', token_admin)
    jar.set('X-XSRF-TOKEN', token)
    jar.set('tonidocloud-ah', tonidocloudah)
    jar.set('tonidocloud-as', tonidocloudas)
    jar.set('tonidocloud-au', 'admin')

    return jar


def post_request(url: str, data: []) -> Response:
    headers = {
        'X-XSRF-TOKEN-admin': authorization_data().get('token_admin'), 'X-XSRF-TOKEN': 'NONE',
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    return requests.post(url, cookies=authorization_data(), headers=headers, data=data)

