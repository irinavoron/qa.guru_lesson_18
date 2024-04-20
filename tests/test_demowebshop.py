import logging
import os
from allure_commons.types import AttachmentType
import requests
import allure
from selene import browser, have
from dotenv import load_dotenv

load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')


def get_authorization_cookie():
    with allure.step('Get authorization cookie from response'):
        response = requests.post(
            url='https://demowebshop.tricentis.com/login',
            data={'Email': email, 'Password': password},
            allow_redirects=False
        )

        allure.attach(response.text, 'response', AttachmentType.TEXT, '.txt')

        authorization_cookie = response.cookies.get('NOPCOMMERCE.AUTH')

        allure.attach(response.cookies.get('NOPCOMMERCE.AUTH'), 'authorization_cookie', AttachmentType.TEXT, '.txt')

        logging.info(response.status_code)
        logging.info(response.text)

        return authorization_cookie


# def test_login_ui():
#     browser.open('/login')
#     browser.element('#Email').type('j.doe@example.mail.com')
#     browser.element('#Password').type('123456')
#     browser.element('.login-button').click()
#
#     browser.element('.account').should(have.exact_text('j.doe@example.mail.com'))


def test_login_api():
    authorization_cookie = get_authorization_cookie()

    with allure.step('Login with authorization cookie'):
        browser.open('/')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': authorization_cookie})
        browser.driver.refresh()

    with allure.step('Verify successful authorization'):
        browser.element('.account').should(have.exact_text(email))
