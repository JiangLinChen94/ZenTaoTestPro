from common.base_page import BasePage


class ZenTaoAddProductPage(BasePage):
    def __init__(self,  driver):
        super().__init__(driver)
        self.product_page = {'element_name': '前往产品页面',
                             'locator_type': 'xpath',
                             'locator_value': "//li[@data-id='product']",
                             'timeout': 3}

        self.add_product_page = {'element_name': '添加产品按钮',
                                 'locator_type': 'xpath',
                                 'locator_value': '//*[@id="pageActions"]/div/a',
                                 'timeout': 3}

        self.product_input = {'element_name': '产品名称输入框',
                              'locator_type': 'xpath',
                              'locator_value': '//input[@id="name"]',
                              'timeout': 3}

        self.product_code_input = {'element_name': '产品代号输入框',
                                   'locator_type': 'xpath',
                                   'locator_value': '//input[@id="code"]',
                                   'timeout': 3}

        self.product_submit = {'element_name': '保存产品按钮',
                               'locator_type': 'xpath',
                               'locator_value': '//button[@id="submit"]',
                               'timeout': 3}

    def go_product_page(self):
        self.click(self.product_page)

    def go_add_product_page(self):
        self.click(self.add_product_page)

    def input_product_name(self, product_name='alin'):
        self.input(self.product_input, product_name)

    def input_product_code(self, product_code='test'):
        self.input(self.product_code_input, product_code)

    def product_submit_button(self):
        self.click(self.product_submit)


