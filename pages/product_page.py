from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.product_page = self.page.locator("li", has_text="Products")
        self.all_products_text = self.page.locator(".productinfo p")
        self.all_products_price = self.page.locator(".productinfo h2")

        self.search_input = self.page.get_by_placeholder("Search Product")
        self.search_button = self.page.locator("#submit_search")

        self.add_to_cart_button = self.page.locator(".productinfo").get_by_text("Add to cart")
        self.continue_shopping_button = self.page.get_by_role("button", name="Continue Shopping")

        self.cart_button = self.page.locator("li", has_text="Cart")


    def move_to_product_page(self):
        self.product_page.click()

    def get_all_products(self):
        self.all_products_text.first.wait_for()
        locators_list = self.all_products_text.all()
        names = []
        for i in locators_list:
            names.append(i.inner_text())
        return names

    def add_search_product(self, product):
        self.search_input.click()
        self.search_input.fill(product)
        self.search_button.click()

    def get_all_prices(self):
        prices_list = self.all_products_price.all()
        prices = []
        for i in prices_list:
            text = i.inner_text()
            clean_number = float(text.replace("Rs.", ""))
            prices.append(clean_number)
        return prices

    def get_first_product_name(self):
        self.all_products_text.first.wait_for()
        return self.all_products_text.first.inner_text()


    def add_first_product_to_cart(self):
        self.add_to_cart_button.first.click()
        # self.add_to_cart_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()
        self.cart_button.click()


