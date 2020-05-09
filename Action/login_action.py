from time import sleep
from page.login_page.zentao_login_page import ZenTaoLoginPage
from common.browser import Browser
from common.base_page import BasePage
from common.config_utils import local_config


class LoginAction:
    def __init__(self, driver):
        self.login_page = ZenTaoLoginPage(driver)

    def login_action(self, username, password):
        self.login_page.implicitly_wait()
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login_button()

    def login_success(self, username, password):
        self.login_action(username, password)
        self.login_page.screenshot_as_file()
        return ZenTaoLoginPage(self.login_page.driver)

    def default_login(self):
        return self.login_action('admin', 'alin19941226061X')

    def login_fail(self, username, password):
        self.login_action(username, password)
        return self.login_page.get_login_fail_alert_content()

    def login_by_cookie(self):
        pass


if __name__ == '__main__':
    driver = Browser().get_driver()
    login = LoginAction(driver)
    bp = BasePage(driver)
    bp.open_url(local_config.test_url)
    # login.login_success('admin', 'alin19941226061X')
    login.login_fail('test', 'test001')