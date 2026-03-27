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
        self.select_form_password = self.page.locator("input[data-qa='password']")

        self.select_day = self.page.locator("#days")
        self.select_month = self.page.locator("#months")
        self.select_year = self.page.locator("#years")

        self.select_checkbox_news = self.page.locator("#newsletter")
        self.select_checkbox_offer = self.page.locator("#optin")

        self.select_form_first_name = self.page.locator("input[data-qa='first_name']")


    def signup(self, name, email):
        self.name_input.fill(name)
        self.email_signup.fill(email)
        self.signup_button.click()

    def select_gender(self, gender_name):
        return self.page.get_by_label(gender_name).check()

    def fill_signup_form(self, name, email):
        self.select_form_name.fill(name)
        self.select_form_password.fill(email)

    def fill_select_dob(self, day, month, year):
        self.select_day.select_option(day)
        self.select_month.select_option(month)
        self.select_year.select_option(year)

    def select_checkbox(self):
        self.select_checkbox_news.check()
        self.select_checkbox_offer.check()

    def fill_user_info(self, first_name):
        self.select_form_first_name.fill(first_name)



