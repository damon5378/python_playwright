import pytest

from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    return LoginPage(page)


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