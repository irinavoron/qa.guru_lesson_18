import pytest
from selene import browser

from config import config


@pytest.fixture(autouse=True, scope='function')
def browser_management():
    browser.config.base_url = config.base_url
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
    browser.config.timeout = config.timeout

    yield

    browser.quit()
