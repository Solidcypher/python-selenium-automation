from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class SignInPage(BasePage):
    SIGN_IN_TXT = (By.XPATH, "//span[contains(text(),'Sign into your Target account')]")
    EMAIL_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    SIGN_IN_BTN = (By.ID, 'login')
    TC_LINK = (By.CSS_SELECTOR, "a[aria-label='terms & conditions - opens in a new window']")
    SIGNIN_FAILURE_MSG = (By.CSS_SELECTOR, "[data-test='authAlertDisplay']")
    EMAIL = 'bllizardd@kimgmail.com'
    INCORRECT_EMAIL = 'Abllizardd@kimgmail.com'
    PASSWORD = '***********'

    def input_email(self):
        self.input_text(self.EMAIL, *self.EMAIL_FIELD)

    def input_incorrect_email(self):
        self.input_text(self.INCORRECT_EMAIL, *self.EMAIL_FIELD)

    def input_password(self):
        self.input_text(self.PASSWORD, *self.PASSWORD_FIELD)

    def click_sign_in(self):
        self.wait_and_click(*self.SIGN_IN_BTN)

    def click_tc_link(self):
        self.wait_and_click(*self.TC_LINK)

    def verify_user_logged_in(self):  # I am not sure if this is the best way to do this? What would be a better way?
        sleep(2)
        sign_in_txt = self.find_elements(*self.SIGN_IN_TXT)

        assert len(sign_in_txt) == 0, f'Expected length of 0 but got {len(sign_in_txt)} '

    def verify_sign_in_error_message(self):
        self.wait_and_click(*self.SIGNIN_FAILURE_MSG)

    def verify_sign_in_page_appears(self):
        expected_text = "Sign into your Target account"

        actual_text = self.find_element(*self.SIGN_IN_TXT).text

        assert expected_text in actual_text, f"Expected {expected_text} is not in actual text {actual_text}"

        print("Test case Passed")
