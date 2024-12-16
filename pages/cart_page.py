import allure

from selene import browser, have, be, by


class CartPage:
    def __init__(self, auth_cookie='Default'):
        self.cart_page_url = '/cart'
        self.auth_cookie = auth_cookie
        self.product_in_cart = browser.element("//a[@class='product-name']")
        self.remove_from_cart_button = browser.element(".remove-from-cart")
        self.update_shopping_cart = browser.element(by.xpath("//input[@name='updatecart']"))
        self.page_body = browser.element(".page-body")

    def open(self):
        with allure.step("Открыть корзину"):
            browser.open(self.cart_page_url)
            browser.driver.execute_script("$('#fixedban').remove()")
            browser.driver.execute_script("$('footer').remove()")

            browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': self.auth_cookie})
            browser.open(self.cart_page_url)
        return self

    def open_non_auth(self, cookie):
        with allure.step("Открыть корзину"):
            browser.open(self.cart_page_url)
            browser.driver.execute_script("$('#fixedban').remove()")
            browser.driver.execute_script("$('footer').remove()")

            browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
            browser.open(self.cart_page_url)
        return self

    def remove_product_from_cart(self):
        with allure.step("Очистить корзину"):
            self.remove_from_cart_button.click()
            self.update_shopping_cart.click()
        return self

    def should_be_emtpy(self):
        self.page_body.should(have.text("Your Shopping Cart is empty!"))

    def product_should_be_added_to_cart(self, product_name):
        with allure.step("Проверить, что товар добавлен"):
            self.product_in_cart.should(have.text(product_name))
        return self
