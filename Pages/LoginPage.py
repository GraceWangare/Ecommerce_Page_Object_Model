

class NopCommerceLoginPage:
    def __init__(self, page):
        self.page = page

    def navigate_to_login_page(self):
        self.page.goto(" https://admin-demo.nopcommerce.com/")

    def enter_username(self, username):
        self.page.get_by_label("Email:").fill(username)

    def enter_password(self, password):
        self.page.get_by_label("Password:").fill(password)

    def click_login_button(self):
        self.page.get_by_role("button", name="Log in").click()

    def do_login(self, username, password):
        self.navigate_to_login_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()


