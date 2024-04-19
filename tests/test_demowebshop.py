import os
from allure_commons.types import AttachmentType
import requests
import allure
from selene import browser, have
from dotenv import load_dotenv


def test_login_ui():
    browser.open('/login')
    browser.element('#Email').type('j.doe@example.mail.com')
    browser.element('#Password').type('123456')
    browser.element('.login-button').click()

    browser.element('.account').should(have.exact_text('j.doe@example.mail.com'))


def test_login_api():
    load_dotenv()
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    with allure.step('Get cookie from api request'):
        response = requests.post(
            url='https://demowebshop.tricentis.com/login',
            data={'Email': email, 'Password': password},
            allow_redirects=False
        )
        cookies = response.cookies.get('NOPCOMMERCE.AUTH')

        allure.attach(response.text, 'Response', AttachmentType.TEXT, '.txt')
        allure.attach(str(response.cookies), 'Cookies', AttachmentType.TEXT, '.txt')

    with allure.step('Login with authorization cookie'):
        browser.open('/')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookies})
        browser.driver.refresh()

    with allure.step('Verify successful authorization'):
        browser.element('.account').should(have.exact_text(email))


