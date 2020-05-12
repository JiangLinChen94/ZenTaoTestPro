import unittest
from selenium import webdriver
from common.browser import Browser
from common.base_page import BasePage
from Action.login_action import LoginAction
from page.login_page.zentao_login_page import ZenTaoLoginPage
from page.main_page.zentao_main_page import ZenTaoMainPage
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils

class TestZenTaoLogin(SeleniumBaseCase):

    # def setUp(self) -> None:
    #     driver = Browser().get_driver()
    #     self.base_page = BasePage(driver)
    #     self.main_page = ZenTaoMainPage(driver)
    #     self.base_page.set_driver()
    test_class_data = TestDataUtils('login_suit', 'TestZenTaoLogin').convert_excel_data_to_test_data()

    def test_login_success(self):
        """
        禅道登录
        """
        test_function_data = self.test_class_data['test_login_success']
        self._testMethodDoc = test_function_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success(test_function_data['test_parameter'].get('username'), test_function_data['test_parameter'].get('password'))
        actual_result = main_page.get_username()
        self.assertEqual(actual_result, test_function_data['expected_result'], test_function_data['test_message'])

    def test_login_fail(self):
        test_function_data = self.test_class_data['test_login_fail']
        self._testMethodDoc = test_function_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        alert_value = login_action.login_fail(test_function_data['test_parameter'].get('username'), test_function_data['test_parameter'].get('password'))
        self.assertEqual(alert_value, test_function_data['expected_result'], test_function_data['test_message'])

    def tearDown(self) -> None:
        self.base_page.quit_browser()


if __name__ == "__main__":
    unittest.main()
