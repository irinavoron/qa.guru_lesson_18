import pytest
from selene import browser
import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    base_url: str = 'https://demowebshop.tricentis.com'
    window_width: int = 1896
    window_height: int = 1080
    timeout: float = 4.5


config = Config()


@pytest.fixture(autouse=True, scope='function')
def browser_management():
    browser.config.base_url = config.base_url
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
    browser.config.timeout = config.timeout

    yield

    browser.quit()
