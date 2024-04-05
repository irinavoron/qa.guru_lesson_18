from selene import browser, command, have


def test_login():
    browser.open('/login')

    browser.element('#Email').type('j.doe@example.mail.com')
    browser.element('#Password').type('123456')
    browser.element('.login-button').click()

    browser.element('.account').should(have.text('j.doe@example.mail.com'))
