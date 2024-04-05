import pytest
from selene import browser


@pytest.fixture(autouse=True, scope='function')
def browser_management():
    browser.config.base_url = 'https://demowebshop.tricentis.com'
    browser.config.window_width = 1896
    browser.config.window_height = 1080