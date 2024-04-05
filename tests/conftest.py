import pytest
from selene import browser
from config import config


@pytest.fixture(autouse=True, scope='function')
def browser_management():
    browser.config.base_url = config.BASE_URL
    browser.config.window_width = config.WINDOW_WIDTH
    browser.config.window_height = config.WINDOW_HEIGHT
    browser.config.timeout = config.TIMEOUT
    browser.config.driver_name = config.driver_name

    yield

    browser.quit()
