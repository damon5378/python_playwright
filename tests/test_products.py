import pytest
from playwright.sync_api import Page, expect




def test_products_page(product_page, login_page):
    product_page.open_home_page()
    expect(product_page.page).to_have_url("https://automationexercise.com/")
    product_page.click_login_link()
    expect(product_page.page).to_have_url("https://automationexercise.com/login")
    login_page.login("abc@ya.ru", "12345Aq")
    product_page.move_to_product_page()

    all_names = product_page.get_all_products()
    print(f"\nНайдено товаров: {len(all_names)}")
    for name in all_names:
        print(f"Проверяю товар: {name}")
        assert len(name) > 0, "У товара пустое название"
        assert isinstance(name, str), f"Название {name} не является строкой"
        assert len(all_names) >= 10, f"Слишком мало товаров на странице: {len(all_names)}"

@pytest.mark.xfail
def test_products_search_and_filter(product_page, login_page):
    product_page.open_home_page()
    product_page.click_login_link()
    login_page.login("abc@ya.ru", "12345Aq")
    product_page.move_to_product_page()

    product_page.click_search_product("Dress")

    found_names = product_page.get_all_products()
    failed_products = []
    print(f"\nНайдено по запросу: {len(found_names)}")
    for name in found_names:
        if "dress" not in name.lower():
            failed_products.append(name)
    assert not failed_products, f"Эти товары не содержат слово Dress: {failed_products}"

def test_get_all_prices(product_page, login_page):
    product_page.open_home_page()
    product_page.click_login_link()
    login_page.login("abc@ya.ru", "12345Aq")
    product_page.move_to_product_page()

    prices = product_page.get_all_prices()
    for price in prices:
        assert price > 0, f"Цена {price} должна быть больше 0"

def test_add_product_to_cart_from_search(product_page, login_page, cart_page):
    search_query = "Blue Top"
    product_page.open_home_page()
    product_page.click_login_link()
    login_page.login("abc@ya.ru", "12345Aq")
    product_page.move_to_product_page()
    product_page.add_search_product(search_query)
    name_from_catalog = product_page.get_first_product_name()

    product_page.add_first_product_to_cart()
    product_page.continue_shopping()

    expect(cart_page.cart_product_name).to_have_text(name_from_catalog)