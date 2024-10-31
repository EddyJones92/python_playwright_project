from pytest import fixture
from playwright.sync_api import sync_playwright

from page_object.Base.base_methods import BaseMethods
from page_object.Login.login_page_methods import LoginPage


@fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@fixture(scope="session")
def context(browser):
    context = browser.new_context(base_url='http://127.0.0.1:8000')
    yield context
    context.close()


@fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


@fixture()
def login(page):
    yield LoginPage(page)


@fixture()
def base(page):
    yield BaseMethods(page)

