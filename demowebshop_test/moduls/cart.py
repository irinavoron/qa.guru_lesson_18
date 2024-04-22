import os

import allure
from selene import browser
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL')


class Cart:

    def open_cart(self):
        with allure.step('Open cart with ui'):
            browser.element('.header-links #topcartlink').click()

    def clear_cart(self):
        with allure.step('Clear cart with UI'):
            browser.element('.qty-input').clear()
            browser.element('.qty-input').type('0')
            browser.element('[name=updatecart]').click()

    def remove_product_from_the_cart(self):
        with allure.step('Remove added product from the cart'):
            browser.element('[name=removefromcart]').click()
            browser.element('[name=updatecart]').click()
