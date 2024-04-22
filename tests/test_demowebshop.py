import allure
from selene import browser, have

from demowebshop_test.data import products
from demowebshop_test.moduls import api_methods
from demowebshop_test.moduls.cart import Cart

cart = Cart()

cookie_name = 'NOPCOMMERCE.AUTH'


def test_product_added_to_cart():
    authorization_cookie = api_methods.get_authorization_cookie()
    api_methods.login(authorization_cookie)

    api_methods.add_product_to_cart(product_endpoint=products.notebook.add_to_cart_endpoint,
                                    cookies={cookie_name: authorization_cookie}
                                    )
    cart.open_cart()

    with allure.step('Only the added product should be displayed in the cart'):
        browser.element('.product-name').should(have.exact_text(products.notebook.name))
        browser.element('[name^=itemquantity]').should(
            have.attribute('value', '1')
        )
        browser.all('.cart-item-row').should(have.size(1))

    cart.clear_cart()


def test_added_product_can_be_deleted():
    authorization_cookie = api_methods.get_authorization_cookie()
    api_methods.login(authorization_cookie)

    api_methods.add_product_to_cart(product_endpoint=products.notebook.add_to_cart_endpoint,
                                    cookies={cookie_name: authorization_cookie}
                                    )
    cart.open_cart()
    cart.remove_product_from_the_cart()

    with allure.step('The added product should be removed from the cart'):
        browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))
