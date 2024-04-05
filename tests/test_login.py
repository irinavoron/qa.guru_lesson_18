import allure
from selene import browser, have


def test_login():
    with allure.step('Open login page'):
        browser.open('/login')

    with allure.step('Fill login data'):
        browser.element('#Email').type('j.doe@example.mail.com')
        browser.element('#Password').type('123456')
        browser.element('.login-button').click()

    with allure.step('Account data should be displayed'):
        browser.element('.account').should(have.text('j.doe@example.mail.com'))
