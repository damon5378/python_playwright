from playwright.sync_api import Page, expect
from pages.base_page import BasePage

def test_login_flow(login_page):
    login_page.open_home_page()
    expect(login_page.page).to_have_url("https://automationexercise.com/")
    login_page.click_login_link()
    expect(login_page.page).to_have_url("https://automationexercise.com/login")
    expect(login_page.login_form_header).to_have_text("Login to your account")
    # login_page.login("abc@ya.ru", "12345Aq")
    login_page.login("elly.barny@gmail.com", "213%fdsf")
    # login_page.page.pause()
    expect(login_page.login_error_text).to_be_visible()