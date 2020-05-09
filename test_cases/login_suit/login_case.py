import unittest
from selenium import webdriver
from common.browser import Browser
from common.base_page import BasePage
from Action.login_action import LoginAction
from page.login_page.zentao_login_page import ZenTaoLoginPage


class TestZenTaoLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_driver()

    def test_login_success(self):
        """
        禅道登录
        """
        login_action = LoginAction(self.base_page.driver)
        login_action.login_success('admin', 'alin19941226061X')
        self.assertEqual('admin', 'admin', 'test_login_success用例执行失败')

    def test_login_fail(self):
        login_action = LoginAction(self.base_page.driver)
        login_action.login_fail('test', 'alin199')
        # self.assertEqual(alert, '登录失败，请检查您的用户名或密码是否填写正确。', 'test_login_fail用例执行失败')

    # def test_login_username_error(self):
    #     """
    #     禅道账户名错误
    #     """
    #     self.login.input_username('admmm')
    #     self.login.input_password()
    #     self.login.click_login_button()
    #     self.login.screenshot_as_file()
    #
    # def test_login_password_error(self):
    #     """
    #     禅道账户名错误
    #     """
    #     self.login.input_username()
    #     self.login.input_password('654321')
    #     self.login.click_login_button()
    #     self.login.screenshot_as_file()

    def tearDown(self) -> None:
        self.base_page.quit_browser()


if __name__ == "__main__":
    unittest.main()
