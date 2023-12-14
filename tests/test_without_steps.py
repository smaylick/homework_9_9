from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
import allure


def test_simple_github():
    browser.open("https://github.com")

    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
    browser.element("#query-builder-test").submit()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#80")).should(be.visible)
