from playwright.sync_api import Page
from page_object.Login.login_page_variables import LoginPageVariables


class LoginPage(LoginPageVariables):

    def __init__(self, page: Page):
        super().__init__()
        self.page = page

    def login(self, login, password):
        self.page.locator("#id_username").fill(login)
        self.page.locator("#id_password").fill(password)
        self.page.locator("text=Login").click()

    def type_login(self, login):
        self.page.locator("#id_username").fill(login)

    def type_password(self, password):
        self.page.locator("#id_password").fill(password)

    def click_login_button(self):
        self.page.locator("text=Login").click()

    def go_to_login_page(self):
        self.page.goto(self.login_path)

    def get_error_text(self):
        return self.page.locator('.loginError')

    def get_greeting(self):
        return self.page.locator('.account h2')

    def go_to_register_page(self):
        button = self.page.get_by_text(self.registration_button_text)
        button.click()
