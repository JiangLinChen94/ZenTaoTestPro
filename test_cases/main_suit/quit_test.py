import unittest
from common.browser import Browser
from common.base_page import BasePage
from Action.login_action import LoginAction
from Action.user_quit_action import UserQuitAction
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils


class QuitTest(SeleniumBaseCase):
    test_class_data = TestDataUtils('main_suit', 'QuitTest').convert_excel_data_to_test_data()

    @unittest.skipIf(test_class_data['test_user_quit']['isnot'], '')
    def test_user_quit(self):
        test_function_data = self.test_class_data['test_user_quit']
        self._testMethodDoc = test_function_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()
        quit_action = UserQuitAction(main_page.driver)
        login_page = quit_action.username_quit()
        actual_result = login_page.get_title()
        self.assertEqual(actual_result.__contains__(test_function_data['expected_result']), True, test_function_data['test_message'])


if __name__ == "__main__":
    unittest.main()