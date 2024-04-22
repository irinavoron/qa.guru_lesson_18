import logging
import os
import allure
import requests
from allure_commons.types import AttachmentType
from selene import browser
from dotenv import load_dotenv

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
        print("Response Text:", response.text)

        # Attach response text to Allure report
        allure.attach(response.text, 'response', AttachmentType.TEXT, '.txt')

        # Get 'NOPCOMMERCE.AUTH' cookie from response
        cookie = response.cookies.get('NOPCOMMERCE.AUTH')

        # Print cookie value for debugging
        print("Authorization Cookie:", cookie)

        # Attach authorization cookie to Allure report
        allure.attach(str(cookie), 'authorization_cookie', AttachmentType.TEXT, '.txt')

        # Log cookie value
        logging.info(cookie)

        return cookie


def login(authorization_cookie):
    #authorization_cookie = get_authorization_cookie()

    with allure.step('Login with authorization cookie'):
        browser.open('https://demowebshop.tricentis.com')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': authorization_cookie})
        browser.driver.refresh()


def add_product_to_cart(product_endpoint, **kwargs):
    with allure.step('Add product to cart with auth.cookie'):
        response = requests.post(BASE_URL + product_endpoint, **kwargs)

        return response
