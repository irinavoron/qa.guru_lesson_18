import os

import allure
from selene import browser
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL')


def open_cart():
    with allure.step('Open cart with ui'):
        browser.element('.header-links #topcartlink').click()


def clear_cart(items_qty):
    with allure.step('Clear cart with ui'):
        for item in range(items_qty):
            browser.element('.qty-input').clear()
            browser.element('.qty-input').type('0')
            browser.element('[name=updatecart]').click()


def remove_product_from_the_cart():
    with allure.step('Remove added product from the cart'):
        browser.element('[name=removefromcart]').click()
        browser.element('[name=updatecart]').click()
