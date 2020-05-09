from common.base_page import BasePage
from common.browser import Browser
from common.element_data_utils import ElementDataUtils
# from Action.login_action import LoginAction

class ZenTaoMainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        elements = ElementDataUtils('main', 'main_page').get_element_info()
        self.user_name = elements['user_name']
        self.user_quit_button = elements['user_quit_button']

    def get_username(self):
        return self.get_text(self.user_name)

    def click_username_button(self):
        self.click(self.user_name)

    def click_user_quit_button(self):
        self.click(self.user_quit_button)


# if __name__ == '__main__':
#     driver = Browser().get_driver()
#     bp = BasePage(driver)
#     login = LoginAction(driver)
#     main_page = ZenTaoMainPage(driver)
#     bp.set_driver()
#     login.default_login()
#     value = main_page.get_username()
#     print(value)



