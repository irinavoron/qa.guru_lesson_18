import os
import allure
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

    with allure.step('Account data should be displayed'):
        browser.element('.account').should(have.exact_text(email))


def test_login_api():
    response = requests.post(
        url='https://demowebshop.tricentis.com/login',
        data={'Email': email, 'Password': password},
        allow_redirects=False
    )

    print(response.status_code)

