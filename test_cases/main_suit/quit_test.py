import unittest
from common.browser import Browser
from common.base_page import BasePage
from Action.login_action import LoginAction
from Action.user_quit_action import UserQuitAction
from common.selenium_base_case import SeleniumBaseCase


class QuitTest(SeleniumBaseCase):

    def test_user_quit(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()
        quit_action = UserQuitAction(main_page.driver)
        login_page = quit_action.username_quit()
        actual_result = login_page.get_title()
        self.assertEqual(actual_result.__contains__('用户登录'), True, 'test_user_quit登录失败')


if __name__ == "__main__":
    unittest.main()