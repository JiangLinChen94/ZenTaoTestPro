import unittest
from selenium import webdriver
from page.login_page.zentao_login_page import ZenTaoLoginPage
from common.browser import Browser


class TestZenTaoLogin(unittest.TestCase):

    def setUp(self):
        driver = Browser().get_driver()
        self.login = ZenTaoLoginPage(driver)
        self.login.set_driver()

    def test_login_success(self):
        """
        禅道登录
        """
        self.login.input_username()
        self.login.input_password()
        self.login.click_login_button()
        self.login.screenshot_as_file()

    def test_login_username_error(self):
        """
        禅道账户名错误
        """
        self.login.input_username('admmm')
        self.login.input_password()
        self.login.click_login_button()
        self.login.screenshot_as_file()

    def test_login_password_error(self):
        """
        禅道账户名错误
        """
        self.login.input_username()
        self.login.input_password('654321')
        self.login.click_login_button()
        self.login.screenshot_as_file()

    def tearDown(self):
        self.login.quit_browser()


if __name__ == "__main__":
    unittest.main()
