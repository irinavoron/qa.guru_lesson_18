from selene import browser
import pytest


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.base_url = 'https://demowebshop.tricentis.com'
    browser.config.window_width = 1896
    browser.config.window_height = 1080

    yield

    browser.quit()
