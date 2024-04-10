import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from pages.stepic_task_page import MainPage
from pages.login_page import LoginPage
from pages.base_page import BasePage


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage():
    # @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
    #                               "https://stepik.org/lesson/236896/step/1"])
    #                             #   "https://stepik.org/lesson/236897/step/1",
    #                             #   "https://stepik.org/lesson/236898/step/1",
    #                             #   "https://stepik.org/lesson/236899/step/1",
    #                             #   "https://stepik.org/lesson/236903/step/1",
    #                             #   "https://stepik.org/lesson/236904/step/1",
    #                             #   "https://stepik.org/lesson/236905/step/1"])
    def test_guest_should_be_able_to_login(self, browser):
        link = "https://stepik.org/lesson/236895/step/1"
        page = MainPage(browser, link)
        page.open()
        time.sleep(7)
        '''Verify Login button is displayed'''
        page.should_be_login_button()
        page.should_click_login_button()
        email = 'domnina.mariia@gmail.com'
        password = '1q2w3e4r!'
        page.should_user_login(email, password)
        time.sleep(5)
        page.should_not_be_login_form()
        answer = math.log(int(time.time()))
        page.should_enter_the_answer(answer)
        time.sleep(3)
        page.should_verification_text_be_displayed
        time.sleep(5)
        


