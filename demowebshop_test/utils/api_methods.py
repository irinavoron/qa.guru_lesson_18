import os
import allure
import requests
from allure_commons.types import AttachmentType
from selene import browser
from dotenv import load_dotenv

from demowebshop_test.utils.logging_attaching_methods import response_logging, response_attaching

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
BASE_URL = os.getenv('BASE_URL')


def get_authorization_cookie():
    with allure.step('Get authorization cookie from response'):
        response = requests.post(
            url=BASE_URL + '/login',
            data={'Email': EMAIL, 'Password': PASSWORD},
            allow_redirects=False
        )

        cookie = response.cookies.get('NOPCOMMERCE.AUTH')

        allure.attach(str(cookie), 'authorization_cookie', AttachmentType.TEXT, '.txt')

        response_logging(response)
        response_attaching(response)

        return cookie


def login(authorization_cookie):
    with allure.step('Login with authorization cookie'):
        browser.open('https://demowebshop.tricentis.com')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': authorization_cookie})
        browser.driver.refresh()


def add_product_to_cart(product_endpoint, **kwargs):
    with allure.step('Add product to cart with auth.cookie'):
        response = requests.post(BASE_URL + product_endpoint, **kwargs)

        response_logging(response)
        response_attaching(response)

        return response
