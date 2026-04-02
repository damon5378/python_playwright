import time

import pytest
from playwright.sync_api import Page, expect

from generators import nickname_random, unique_email, pass_random, first_name_random, last_name_random


@pytest.mark.parametrize(
    "gender, day, month, year, company, address, country, state, city, zipcode, mobile_number",
    [
        ("Mr.", "15", "January", "2000", "Apple", "Trump avenue", "United States", "New York", "New York", "50101", "+1898995564"),
        ("Mrs.", "5", "December", "1982", "NCIS", "Pacific Rd", "Australia", "Sydney", "Palm Beach", "2108", "+6155505857")
    ])
def test_signup_flow(signup_page, gender, day, month, year, company, address, country, state, city, zipcode, mobile_number):
    user_nickname = nickname_random()
    user_password = pass_random()
    user_first_name = first_name_random(gender)
    user_last_name = last_name_random(gender)
    user_email = unique_email(gender)
    signup_page.open_home_page()
    expect(signup_page.page).to_have_url("https://automationexercise.com/")
    signup_page.click_login_link()
    expect(signup_page.page).to_have_url("https://automationexercise.com/login")
    expect(signup_page.signup_form_header).to_have_text("New User Signup!")
    signup_page.signup("John", user_email)
    expect(signup_page.page).to_have_url("https://automationexercise.com/signup")
    expect(signup_page.signup_form_title).to_be_visible()
    # signup_page.signup_form()
    signup_page.select_gender(gender)
    signup_page.fill_signup_form(user_nickname, user_password)
    signup_page.fill_select_dob(day, month, year)
    signup_page.select_checkbox()
    signup_page.fill_user_info(
        user_first_name,
        user_last_name,
        company,
        address,
        country,
        state,
        city,
        zipcode,
        mobile_number)
    expect(signup_page.complete_signup).to_be_visible()
    signup_page.click_continue()
    expect(signup_page.logged).to_contain_text(f"Logged in as {user_nickname}")
    signup_page.delete_flow()
    expect(signup_page.verify_delete).to_contain_text("Account Deleted!")
    signup_page.click_continue()


