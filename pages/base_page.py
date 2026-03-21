from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://automationexercise.com/"

        self.consent = self.page.get_by_role("button", name="Consent")

        self.login_link = self.page.get_by_role("link", name="Signup / Login")
        self.cart_link = self.page.get_by_role("link", name="Cart")
        self.products_link = self.page.get_by_role("link", name="Products")

    def open_home_page(self):
        self.page.goto(self.url)
        # self.consent.click()

    def click_login_link(self):
        self.login_link.click()