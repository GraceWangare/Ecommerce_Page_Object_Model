

from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
from Pages.LogOutPage import NopCommerceLogoutPage

import pytest


@pytest.fixture()
def browser():
    with sync_playwright() as page:
        browser = page.chromium.launch(headless=False, slow_mo=1000, channel="chrome")
        yield browser
        browser.close()


def test_logout(browser):
    page = browser.new_page()
    logout_page = NopCommerceLogoutPage(page)
    username = "admin@yourstore.com"
    password = "admin"
    logout_page.do_login(username, password)





    # assertion
    sign_message_locator = page.locator("//strong[normalize-space()='Welcome, please sign in!']")
    expect(sign_message_locator).to_contain_text("Welcome, please sign in!")


