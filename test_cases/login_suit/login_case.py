import unittest
from selenium import webdriver
from common.browser import Browser
from common.base_page import BasePage
from Action.login_action import LoginAction
from page.login_page.zentao_login_page import ZenTaoLoginPage
from page.main_page.zentao_main_page import ZenTaoMainPage
from common.selenium_base_case import SeleniumBaseCase


class TestZenTaoLogin(SeleniumBaseCase):

    # def setUp(self) -> None:
    #     driver = Browser().get_driver()
    #     self.base_page = BasePage(driver)
    #     self.main_page = ZenTaoMainPage(driver)
    #     self.base_page.set_driver()

    def test_login_success(self):
        """
        禅道登录
        """
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success('admin', 'alin19941226061X')
        actual_result = main_page.get_username()
        self.assertEqual(actual_result, 'admin', 'test_login_success用例执行失败')

    def test_login_fail(self):
        login_action = LoginAction(self.base_page.driver)
        alert_value = login_action.login_fail('test', 'alin199')
        self.assertEqual(alert_value, '登录失败，请检查您的用户名或密码是否填写正确。', 'test_login_fail用例执行失败')

    def tearDown(self) -> None:
        self.base_page.quit_browser()


if __name__ == "__main__":
    unittest.main()
