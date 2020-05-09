from time import sleep
from page.main_page.zentao_main_page import ZenTaoMainPage
from page.login_page.zentao_login_page import ZenTaoLoginPage
from common.browser import Browser
from common.base_page import BasePage
from common.config_utils import local_config
from Action.login_action import LoginAction


class UserQuitAction:
    def __init__(self, driver):
        self.main_page = ZenTaoMainPage(driver)

    def username_quit(self):
        self.main_page.click_username_button()
        self.main_page.click_user_quit_button()
        return ZenTaoLoginPage(self.main_page.driver)


if __name__ == '__main__':
    driver = Browser().get_driver()
    login = LoginAction(driver)
    main_page = UserQuitAction(driver)
    bp = BasePage(driver)
    bp.open_url(local_config.test_url)
    login.default_login()
    print(main_page.username_quit())
