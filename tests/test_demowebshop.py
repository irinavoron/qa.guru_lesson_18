import allure
from selene import browser, have

from demowebshop_test.data import products
from demowebshop_test.data.products import smartphone
from demowebshop_test.utils import api_methods, ui_methods

cookie_name = 'NOPCOMMERCE.AUTH'


def test_product_can_be_added_to_cart():
    items_qty = 1
    authorization_cookie = api_methods.get_authorization_cookie()
    api_methods.login(authorization_cookie)

    api_methods.add_product_to_cart(product_endpoint=products.notebook.add_to_cart_endpoint,
                                    cookies={cookie_name: authorization_cookie}
                                    )
    ui_methods.open_cart()

    with allure.step('Only the added product should be displayed in the cart'):
        browser.element('.product-name').should(have.exact_text(products.notebook.name))
        browser.all('.cart-item-row').should(have.size(items_qty))

    ui_methods.clear_cart(items_qty)


def test_added_product_can_be_deleted():
    authorization_cookie = api_methods.get_authorization_cookie()
    api_methods.login(authorization_cookie)

    api_methods.add_product_to_cart(product_endpoint=smartphone.add_to_cart_endpoint,
                                    cookies={cookie_name: authorization_cookie}
                                    )
    ui_methods.open_cart()
    ui_methods.remove_product_from_cart()

    with allure.step('The added product should be removed from the cart'):
        browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))
