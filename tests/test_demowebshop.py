import logging
import os
from allure_commons.types import AttachmentType
import requests
import allure
from selene import browser, have, be, command
from dotenv import load_dotenv

load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

base_url = 'https://demowebshop.tricentis.com'


def get_authorization_cookie():
    with allure.step('Get authorization cookie from response'):
        response = requests.post(
            url=base_url + '/login',
            data={'Email': email, 'Password': password},
            allow_redirects=False
        )

        allure.attach(response.text, 'response', AttachmentType.TEXT, '.txt')

        authorization_cookie = response.cookies.get('NOPCOMMERCE.AUTH')

        allure.attach(response.cookies.get('NOPCOMMERCE.AUTH'), 'authorization_cookie', AttachmentType.TEXT, '.txt')

        # logging.info(response.status_code)
        # logging.info(response.text)

        return authorization_cookie


def login_with_authorization_cookie():
    authorization_cookie = get_authorization_cookie()

    with allure.step('Login with authorization cookie'):
        browser.open('/')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': authorization_cookie})
        browser.driver.refresh()


def add_product_to_cart(product_endpoint, **kwargs):
    with allure.step('Add product to cart'):
        response = requests.post(base_url + product_endpoint, **kwargs)

        return response


def open_cart_with_ui():
    with allure.step('Open cart with ui'):
        browser.element('.header-links #topcartlink').click()


def clear_cart_with_ui():
    with allure.step('Clear cart with UI'):
        browser.element('.qty-input').clear()
        browser.element('.qty-input').type('0')
        browser.element('[name=updatecart]').click()


def test_product_added_to_cart():
    authorization_cookie = get_authorization_cookie()
    login_with_authorization_cookie()

    add_product_to_cart(
        product_endpoint='/addproducttocart/catalog/31/1/1',
        cookies={'NOPCOMMERCE.AUTH': authorization_cookie}
    )

    open_cart_with_ui()

    with allure.step('The added product should be displayed in the cart'):
        browser.element('.product-name').should(have.exact_text('14.1-inch Laptop'))
        browser.element('[name^=itemquantity]').should(
            have.attribute('value', '1')
        )
        browser.all('.cart-item-row').should(have.size(1))

    clear_cart_with_ui()


def test_added_product_can_be_deleted():
    authorization_cookie = get_authorization_cookie()
    login_with_authorization_cookie()

    add_product_to_cart(
        '/addproducttocart/catalog/31/1/1',
        cookies={'NOPCOMMERCE.AUTH': authorization_cookie}
    )

    open_cart_with_ui()

    with allure.step('Delete added product from the cart'):
        browser.element('[name=removefromcart]').click()
        browser.element('[name=updatecart]').click()

    with allure.step('The added product should be removed from the cart'):
        browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def test_qty_can_be_updated_in_the_cart():
    authorization_cookie = get_authorization_cookie()
    login_with_authorization_cookie()

    add_product_to_cart(
        '/addproducttocart/catalog/31/1/1',
        cookies={'NOPCOMMERCE.AUTH': authorization_cookie}
    )

    open_cart_with_ui()

    with allure.step('Update the qty in the cart'):
        qty = 1
        # total = browser.element('.product-subtotal')

        browser.element('.qty-input').clear()
        browser.element('.qty-input').type(qty + 1)
        browser.element('[name=updatecart]').click()

    with allure.step('Updated qty should be displayed in the cart'):
        pass

    clear_cart_with_ui()
