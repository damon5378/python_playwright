from pages.base_page import BasePage


class SignupPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.name_input = self.page.locator("input[data-qa='signup-name']")
        self.email_signup = self.page.locator("input[data-qa='signup-email']")
        self.signup_button = self.page.get_by_role("button", name="Signup")

        self.signup_form_header = self.page.locator(".signup-form h2")
        self.signup_form_title = self.page.get_by_text("Enter Account Information")

        self.select_form_name = self.page.locator("input[data-qa='name']")
        self.select_form_email = self.page.locator("input[data-qa='password']")

        # self.title_gender = self.page.locator("#id_gender1")

    def signup(self, name, email):
        self.name_input.fill(name)
        self.email_signup.fill(email)
        self.signup_button.click()
        # self.select_gender(gender)

    def select_gender(self, gender_name):
        return self.page.get_by_label(gender_name).check()

    def fill_signup_form(self, name, email):
        self.select_form_name.fill(name)
        self.select_form_email.fill(email)


