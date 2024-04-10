from .locators import LoginPageLocators

class LoginPage():
    def should_be_login_form(self):
        '''Verifies login form is displayed'''
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is missing"
        assert True

    def should_be_login_url(self):
        '''Verifies correct login url is opened'''
        assert 'login' in self.browser.current_url, '"login" is missing in current url'
        assert True

    def should_user_login(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT).click()