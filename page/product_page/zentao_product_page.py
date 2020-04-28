from common.base_page import BasePage
from common.element_data_utils import ElementDataUtils
from common.element_yaml_utils import ElementYamlUtils

class ZenTaoAddProductPage(BasePage):
    def __init__(self,  driver):
        super().__init__(driver)
        # self.go_product_page = {'element_name': '前往产品页面',
        #                      'locator_type': 'xpath',
        #                      'locator_value': "//li[@data-id='product']",
        #                      'timeout': 3}
        #
        # self.add_product_page = {'element_name': '添加产品按钮',
        #                          'locator_type': 'xpath',
        #                          'locator_value': '//*[@id="pageActions"]/div/a',
        #                          'timeout': 3}
        #
        # self.product_input = {'element_name': '产品名称输入框',
        #                       'locator_type': 'xpath',
        #                       'locator_value': '//input[@id="name"]',
        #                       'timeout': 3}
        #
        # self.product_code_input = {'element_name': '产品代号输入框',
        #                            'locator_type': 'xpath',
        #                            'locator_value': '//input[@id="code"]',
        #                            'timeout': 3}
        #
        # self.product_submit = {'element_name': '保存产品按钮',
        #                        'locator_type': 'xpath',
        #                        'locator_value': '//button[@id="submit"]',
        #                        'timeout': 3}
        # elements = ElementDataUtils('product_page').get_element_info()
        # self.go_product_page = elements['go_product_page']
        # self.add_product_page = elements['add_product_page']
        # self.product_input = elements['product_input']
        # self.product_code_input = elements['product_code_input']
        # self.product_submit = elements['product_submit']

        yaml_elements = ElementYamlUtils().get_ymal_info()
        self.go_product_page = yaml_elements['go_product_page']
        self.add_product_page = yaml_elements['add_product_page']
        self.product_input = yaml_elements['product_input']
        self.product_code_input = yaml_elements['product_code_input']
        self.product_submit = yaml_elements['product_submit']

    def go_to_product_page(self):
        self.click(self.go_product_page)

    def go_add_product_page(self):
        self.click(self.add_product_page)

    def input_product_name(self, product_name='alin'):
        self.input(self.product_input, product_name)

    def input_product_code(self, product_code='test'):
        self.input(self.product_code_input, product_code)

    def product_submit_button(self):
        self.click(self.product_submit)


