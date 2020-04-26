from common.base_page import BasePage


class ZenTaoLoginPage(BasePage):
    def __init__(self,  driver):
        super().__init__(driver)
        self.username_input_box = {'element_name': '用户名输入框',
                                   'locator_type': 'xpath',
                                   'locator_value': '//input[@name="account"]',
                                   'timeout': 3}

        self.password_input_box = {'element_name': '密码输入框',
                                   'locator_type': 'xpath',
                                   'locator_value': '//input[@name="password"]',
                                   'timeout': 3}

        self.login_button = {'element_name': '登录按钮',
                             'locator_type': 'xpath',
                             'locator_value': '//button[@id="submit"]',
                             'timeout': 3}

    def input_username(self, username='admin'):
        self.input(self.username_input_box, username)

    def input_password(self, password='alin19941226061X'):
        self.input(self.password_input_box, password)

    def click_login_button(self):
        self.click(self.login_button)



