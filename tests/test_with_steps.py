import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_steps_github():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        browser.element(".header-search-button").click()
        browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
        browser.element("#query-builder-test").submit()

    with allure.step("Переходим по ссылке репозиторий"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 80"):
        browser.element(by.partial_text("#80")).should(be.visible)
