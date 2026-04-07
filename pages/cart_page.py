from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.cart_product_name = self.page.locator("td.cart_description a")
        self.cart_product_price = self.page.locator("td.cart_price p")

        self.cart_quantity = self.page.locator("td.cart_quantity button")
        self.cart_total = self.page.locator("td.cart_total p")


    def get_total_price_calculated(self):
        price_locators = self.cart_product_price.all()
        quantity_locators = self.cart_quantity.all()

        total_price = 0

        for i in range(len(price_locators)):
            price_text = price_locators[i].inner_text()
            price_num = float(price_text.replace("Rs.", ""))

            qty_text = quantity_locators[i].inner_text()
            qty_num = int(qty_text)

            total_price += qty_num * price_num

        return total_price

    def get_final_total_from_site(self):
        text = self.cart_total.first.inner_text()
        return float(text.replace("Rs.", ""))




