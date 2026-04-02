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
        self.select_form_last_name = self.page.locator("input[data-qa='last_name']")
        self.select_form_company_name = self.page.locator("input[data-qa='company']")
        self.select_form_address_name = self.page.locator("input[data-qa='address']")
        self.select_form_country_name = self.page.locator("select[data-qa='country']")
        self.select_form_state_name = self.page.locator("input[data-qa='state']")
        self.select_form_city_name = self.page.locator("input[data-qa='city']")
        self.select_form_zipcode = self.page.locator("input[data-qa='zipcode']")
        self.select_form_mobile_number = self.page.locator("input[data-qa='mobile_number']")

        self.select_create_account_button = self.page.get_by_role("button", name="Create Account")

        self.complete_signup = self.page.get_by_text("ACCOUNT CREATED!")

        self.continue_button = self.page.locator("a[data-qa='continue-button']")

        self.logged = self.page.locator("li", has_text="Logged in as")

        self.delete_button = self.page.locator("li", has_text="Delete Account")
        self.verify_delete = self.page.locator("h2", has_text="ACCOUNT DELETED!")


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

    def fill_user_info(self, first_name, last_name, company_name, address_name, country_name, state_name, city_name, zipcode, mobile_number):
        self.select_form_first_name.fill(first_name)
        self.select_form_last_name.fill(last_name)
        self.select_form_company_name.fill(company_name)
        self.select_form_address_name.fill(address_name)
        self.select_form_country_name.select_option(country_name)
        self.select_form_state_name.fill(state_name)
        self.select_form_city_name.fill(city_name)
        self.select_form_zipcode.fill(zipcode)
        self.select_form_mobile_number.fill(mobile_number)
        self.select_create_account_button.click()

    def click_continue(self):
        self.continue_button.click()

    def delete_flow(self):
        self.delete_button.click()



