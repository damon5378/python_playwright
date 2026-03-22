from pages.base_page import BasePage


class SignupPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.name_input = self.page.locator("input[data-qa='signup-name']")
        self.email_signup = self.page.locator("input[data-qa='signup-email']")
        self.signup_button = self.page.get_by_role("button", name="Signup")

        self.signup_form_header = self.page.locator(".signup-form h2")

    def signup(self, name, email):
        self.name_input.fill(name)
        self.email_signup.fill(email)
        self.signup_button.click()