from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page,):
        super().__init__(page)

        self.email_input = self.page.locator('input[data-qa="login-email"]')
        self.password_input = self.page.locator('input[data-qa="login-password"]')
        self.login_button = self.page.get_by_role("button", name="Login")

        self.signup_button = self.page.get_by_role("button", name="Signup")

        self.login_form_header = self.page.locator(".login-form h2")
        self.login_error_text = self.page.get_by_text("Your email or password is incorrect!")

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
        # self.signup_button.click()
        # self.password_input.press("Enter")

