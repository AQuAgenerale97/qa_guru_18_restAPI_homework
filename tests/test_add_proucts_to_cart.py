import os

import allure
import pytest

from allure_commons.types import Severity

from pages.cart_page import CartPage
from utils.logging_and_attachment_settings import post_with_logging

BASE_URL = "https://demowebshop.tricentis.com"


@pytest.fixture(scope='function', autouse=False)
def simple_user_auth():
    user_data = {
        'email': os.getenv('DEMOWEBSHOP_LOGIN'),
        'password': os.getenv('DEMOWEBSHOP_PASSWORD'),
        'RememberMe': False
    }
    with allure.step("Авторизация пользователя"):
        response = post_with_logging(BASE_URL + '/login',
                                     data=user_data,
                                     allow_redirects=False)
        auth_cookie = response.cookies.get('NOPCOMMERCE.AUTH')
        auth_data = (user_data, auth_cookie)

    yield auth_data


def test_add_to_cart_with_authorization(simple_user_auth):
    allure.dynamic.tag('web and api')
    allure.dynamic.title('Authorized user adds products to cart')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.label('owner', 'slinkov')
    allure.dynamic.feature('Я как авторизованный пользователь имею возможность добавить в корзину продукты и '
                           'найти этот продукт в корзине')
    allure.dynamic.story('Добавление продукта в корзину')
    allure.dynamic.link('https://demowebshop.tricentis.com', name='Testing')

    user_data, auth_cookie = simple_user_auth

    with allure.step("Добавить товар в корзину"):
        response = post_with_logging(BASE_URL + "/addproducttocart/catalog/13/1/1",
                                     cookies={"NOPCOMMERCE.AUTH": auth_cookie})
        assert response.status_code == 200, f"Failed to add product to cart: {response.text}"

    cart_page = CartPage(auth_cookie)
    cart_page.open()

    cart_page.product_should_be_added_to_cart("Computing and Internet")

    cart_page.remove_product_from_cart()
    cart_page.should_be_emtpy()


def test_add_to_cart_without_authorization():
    allure.dynamic.tag('web and api')
    allure.dynamic.title('Non-authorized user adds products to cart')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.label('owner', 'slinkov')
    allure.dynamic.feature('Я как неавторизованный пользователь имею возможность добавить в корзину продукты и '
                           'найти этот продукт в корзине')
    allure.dynamic.story('Добавление продукта в корзину')
    allure.dynamic.link('https://demowebshop.tricentis.com', name='Testing')

    with allure.step("Добавить товар в корзину"):
        response = post_with_logging(BASE_URL + "/addproducttocart/catalog/13/1/1")
        cookie = response.cookies.get('Nop.customer')

    cart_page = CartPage()
    cart_page.open_non_auth(cookie)

    cart_page.product_should_be_added_to_cart("Computing and Internet")

    cart_page.remove_product_from_cart()
    cart_page.should_be_emtpy()
