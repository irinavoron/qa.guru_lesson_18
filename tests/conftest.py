import os

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv


@pytest.fixture(autouse=True)
def browser_management():
    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "122.0",
        "selenoid:options": {
            "enableVideo": True,
            "enableVNC": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    load_dotenv()
    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASSWORD')
    url = os.getenv('SELENOID_URL')
    base_url = os.getenv('BASE_URL')

    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@{url}/wd/hub',
        options=options)

    browser.config.driver = driver

    browser.config.base_url = base_url
    browser.config.window_width = 1896
    browser.config.window_height = 1096

    yield

    browser.quit()
