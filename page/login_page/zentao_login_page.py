from common.base_page import BasePage
from common.element_data_utils import ElementDataUtils
from common.element_yaml_utils import ElementYamlUtils


class ZenTaoLoginPage(BasePage):
    def __init__(self,  driver):
        super().__init__(driver)
        # self.username_input_box = {'element_name': '用户名输入框',
        #                            'locator_type': 'xpath',
        #                            'locator_value': '//input[@name="account"]',
        #                            'timeout': 3}
        #
        # self.password_input_box = {'element_name': '密码输入框',
        #                            'locator_type': 'xpath',
        #                            'locator_value': '//input[@name="password"]',
        #                            'timeout': 3}
        #
        # self.login_button = {'element_name': '登录按钮',
        #                      'locator_type': 'xpath',
        #                      'locator_value': '//button[@id="submit"]',
        #                      'timeout': 3}

        # elements = ElementDataUtils('login_page').get_element_info()
        # self.username_input_box = elements['username_input_box']
        # self.password_input_box = elements['password_input_box']
        # self.login_button = elements['login_button']

        yaml_element = ElementYamlUtils().get_ymal_info()
        self.username_input_box=yaml_element['username_input_box']
        self.password_input_box = yaml_element['password_input_box']
        self.login_button = yaml_element['login_button']

    def input_username(self, username='admin'):
        self.input(self.username_input_box, username)

    def input_password(self, password='alin19941226061X'):
        self.input(self.password_input_box, password)

    def click_login_button(self):
        self.click(self.login_button)



