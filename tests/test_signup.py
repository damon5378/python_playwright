import time

import pytest
from playwright.sync_api import Page, expect

from generators import name_random, unique_email, pass_random


@pytest.mark.parametrize("gender", ["Mr.", "Mrs."])
def test_signup_flow(signup_page, gender):
    signup_page.open_home_page()
    expect(signup_page.page).to_have_url("https://automationexercise.com/")
    signup_page.click_login_link()
    expect(signup_page.page).to_have_url("https://automationexercise.com/login")
    expect(signup_page.signup_form_header).to_have_text("New User Signup!")
    signup_page.signup("John", unique_email(gender))
    expect(signup_page.page).to_have_url("https://automationexercise.com/signup")
    expect(signup_page.signup_form_title).to_be_visible()
    # signup_page.signup_form()
    signup_page.select_gender(gender)
    signup_page.fill_signup_form(name_random(), pass_random())