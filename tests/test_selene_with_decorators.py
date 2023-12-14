import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "Sergey Gavrilenko")
@allure.feature("Decorators")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_github():
    open_main_page()
    search_for_repository("smaylick/homework_9_9")
    go_to_repository("smaylick/homework_9_9")
    open_issue_tab()
    should_see_issue_with_number()


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo} ")
def search_for_repository(repo):
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys(repo)
    browser.element("#query-builder-test").submit()


@allure.step("Переходим по ссылке репозиторий {repo} ")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером 1")
def should_see_issue_with_number():
    s(by.partial_text("#1")).should(be.visible)
