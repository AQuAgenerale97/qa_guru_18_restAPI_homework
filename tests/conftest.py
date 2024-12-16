import os

import allure
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium.webdriver.chrome.options import Options


DEMOWEBSHOP_URL = "https://demowebshop.tricentis.com"


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    browser.config.base_url = DEMOWEBSHOP_URL
    options = Options()
    options.add_argument("window-size=1920,1080")

    yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()

"""
@pytest.fixture(scope="function", autouse=False)
def simple_user_auth(request):
    with allure.step("Авторизация"):
        data = {
                "Email": os.getenv("DEMOWEBSHOP_LOGIN"),
                "Password": os.getenv("DEMOWEBSHOP_PASSWORD"),
                "RememberMe": False
        }
        response = post_request(DEMOWEBSHOP_URL + "/login", data=data, allow_redirects=False)
        authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        return authorization_cookie
"""
