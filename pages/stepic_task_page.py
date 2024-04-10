from .locators import LoginPageLocators
from .locators import StepikTaskPageLocators
from .base_page import BasePage

class MainPage(BasePage):

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        
    def should_be_login_button(self):
        '''Verifies login button is displayed'''
        assert self.is_element_present(*StepikTaskPageLocators.LOGIN_BUTTON), "Login button is missing"
        assert True

    def should_click_login_button(self):
        self.browser.find_element(*StepikTaskPageLocators.LOGIN_BUTTON).click()

    def should_user_login(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT).click()

    def should_not_be_login_form(self):
        '''Verifies login form is not displayed'''
        assert self.is_disappeared(*LoginPageLocators.LOGIN_FORM), "Login form is displayed"
        assert True

    def should_enter_the_answer(self, answer):
        self.browser.find_element(*StepikTaskPageLocators.ANSWER_FIELD).send_keys(answer)
        self.browser.find_element(*StepikTaskPageLocators.SUBMIT_BUTTON).click()

    def should_verification_text_be_displayed(self):
        text_element = self.browser.find_element(*StepikTaskPageLocators.CORRECT_TEXT)
        actual_text = text_element.text
        assert actual_text == "Correct!", f"The text is not 'Correct!', it is '{actual_text}'"