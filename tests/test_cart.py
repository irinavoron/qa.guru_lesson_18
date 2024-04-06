import os
import requests
from selene import browser

from config import load_env

load_env()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')


def get_auth_coockie():
    response = requests.post(
        url='https://demowebshop.tricentis.com/login',
        data={'Email': email, 'Password': password},
        allow_redirects=False
    )
    auth_coockie = response.cookies.get('NOPCOMMERCE.AUTH')

    return auth_coockie


def test_add_to_cart():
    browser.open('/')
    auth_coockie = get_auth_coockie()
    browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': auth_coockie})
    browser.open('/')
