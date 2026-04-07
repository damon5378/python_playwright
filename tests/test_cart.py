def test_cart_total(product_page, login_page, cart_page):
    product_page.open_home_page()
    product_page.click_login_link()
    login_page.login("abc@ya.ru", "12345Aq")
    product_page.move_to_product_page()
    product_page.add_first_product_to_cart()
    # product_page.add_search_product("Men Tshirt")
    product_page.continue_shopping()

    my_calc_total = cart_page.get_total_price_calculated()

    site_total = cart_page.get_final_total_from_site()

    assert my_calc_total == site_total, f"Сайт обсчитал! Мы насчитали {my_calc_total}, а сайт {site_total}"