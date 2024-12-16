from selene import browser, have, be


class LoginPage:
    def __init__(self):
        self.login_page_url = '/login'

    def open(self):
        browser.open(self.login_page_url)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        return self
