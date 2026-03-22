from playwright.sync_api import Page, expect

def test_signup_flow(signup_page):
    signup_page.open_home_page()
    expect(signup_page.page).to_have_url("https://automationexercise.com/")
    signup_page.click_login_link()
    expect(signup_page.page).to_have_url("https://automationexercise.com/login")
    expect(signup_page.signup_form_header).to_have_text("New User Signup!")
    signup_page.signup("John", "yoyo55@gmail.com")