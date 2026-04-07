import os
import pytest
from dotenv import load_dotenv

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.signup_page import SignupPage


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def signup_page(page):
    return SignupPage(page)

@pytest.fixture
def product_page(page):
    return ProductPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture(autouse=True)
def cleanup_ads(page):
    # Блокируем запросы на уровне сети
    page.route("**/*googleads*", lambda route: route.abort())
    page.route("**/*doubleclick*", lambda route: route.abort())
    page.route("**/*pagead*", lambda route: route.abort())

    # Внедряем скрипт, который будет удалять мусор каждые 500мс
    page.add_init_script("""
        setInterval(() => {
            // Удаляем фреймы рекламы
            document.querySelectorAll('iframe[id^="aswift"], iframe[id^="google_ads"]').forEach(el => el.remove());
            // Удаляем всплывающее окно (vignette)
            document.querySelectorAll('.google-vignette-test, #google_ads_rf').forEach(el => el.remove());
            // Удаляем блоки с рекламой
            document.querySelectorAll('.adsbygoogle').forEach(el => el.remove());
        }, 500);
    """)

@pytest.fixture
def authenticated_page(login_page):
    login_page.open_home_page()
    login_page.click_login_link()
    login_page.login(os.getenv("LOGIN_EMAIL"), os.getenv("LOGIN_PASS"))

    return login_page


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }
