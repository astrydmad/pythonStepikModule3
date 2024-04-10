from selenium.webdriver.common.by import By

class StepikTaskPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#ember420")
    ANSWER_FIELD = (By.XPATH, "//*[contains(@class, 'string-quiz__textarea')]")
    SUBMIT_BUTTON = (By.XPATH, "//button[@class='submit-submission']")
    CORRECT_TEXT = (By.XPATH, "//p[@class='smart-hints__hint']")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#ember489')
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login_email")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login_password")
    LOGIN_SUBMIT = (By.XPATH, "//button[@class='sign-form__btn button_with-loader ']")