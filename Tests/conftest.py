from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
from Pages.LoginPage import NopCommerceLoginPage

import pytest


@pytest.fixture()
def browser():
    with sync_playwright() as page:
        browser = page.chromium.launch(headless=False, slow_mo=1000, channel="chrome")
        yield browser
        browser.close()


@pytest.fixture()
def login_authenticate(browser):
    page = browser.new_page()
    context = browser.new_context()
    login_page = NopCommerceLoginPage(page)
    username = "admin@yourstore.com"
    password = "admin"
    login_page.do_login(username, password)
    yield context