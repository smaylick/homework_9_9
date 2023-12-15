import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
