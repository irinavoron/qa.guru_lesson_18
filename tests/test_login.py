import os
import allure
from allure_commons.types import AttachmentType
from selene import browser, have
from config import load_env
import requests


load_env()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')


def test_login_ui():
    with allure.step('Open login page'):
        browser.open('/login')

    with allure.step('Fill login data'):
        browser.element('#Email').type(email)
        browser.element('#Password').type(password)
        browser.element('.login-button').click()

    with allure.step('Verify successful authorization'):
        browser.element('.account').should(have.exact_text(email))


def test_login_api():
    with allure.step('Get coockie from api'):
        response = requests.post(
            url='https://demowebshop.tricentis.com/login',
            data={'Email': email, 'Password': password},
            allow_redirects=False
        )
        allure.attach(response.text, 'response', AttachmentType.TEXT, '.txt')
        auth_coockie = response.cookies.get('NOPCOMMERCE.AUTH')
        allure.attach(auth_coockie, 'Authorization coockie', AttachmentType.TEXT, '.txt')

    with allure.step('Login with api'):
        browser.open('/')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': auth_coockie})
        browser.open('/')

    with allure.step('Verify successful authorization'):
        browser.element('.account').should(have.exact_text(email))


