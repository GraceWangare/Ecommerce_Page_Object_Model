from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
from Pages.LoginPage import NopCommerceLoginPage

import pytest


# @pytest.fixture()
# def browser():
#     with sync_playwright() as page:
#         browser = page.chromium.launch(headless=False, slow_mo=1000, channel="chrome")
#         context = browser.new_context()
#         yield browser
#         browser.close()


def test_valid_login(browser):
    page = browser.new_page()
    login_page = NopCommerceLoginPage(page)
    username = "admin@yourstore.com"
    password = "admin"
    login_page.do_login(username, password)

    # assertion
    dashboard_locator = page.locator("//h1[normalize-space()='Dashboard']")
    assert dashboard_locator.is_visible()


def test_invalid_login(browser):
    page = browser.new_page()
    login_page = NopCommerceLoginPage(page)
    username = "admin@yourstore.com"
    password = "invalid"
    login_page.do_login(username, password)

    # assertion
    # error_message_locator = page.locator(".message-error.validation-summary-errors")
    # assert error_message_locator.is_visible()

    wrong_password_error_message = page.locator(".message-error.validation-summary-errors")
    expect(wrong_password_error_message).to_contain_text("Login was unsuccessful")

