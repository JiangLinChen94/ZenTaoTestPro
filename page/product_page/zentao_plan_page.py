from common.base_page import BasePage
from common.element_data_utils import ElementDataUtils
from common.element_yaml_utils import ElementYamlUtils

class ZenTaoAddPlanPage(BasePage):
    def __init__(self,  driver):
        super().__init__(driver)
        # self.product_page = {'element_name': '前往产品页面',
        #                      'locator_type': 'xpath',
        #                          'locator_value': "//li[@data-id='product']",
        #                      'timeout': 3}
        #
        # self.plan_page = {'element_name': '计划页面',
        #                    'locator_type': 'xpath',
        #                    'locator_value': "//*[@id='subNavbar']/ul/li[3]/a",
        #                    'timeout': 3}
        #
        # self.add_plan_page = {'element_name': '提计划页面',
        #                        'locator_type': 'xpath',
        #                        'locator_value': '//*[@id="mainMenu"]/div[2]/a/i',
        #                        'timeout': 3}
        #
        # self.plan_name = {'element_name': '计划名称',
        #                   'locator_type': 'xpath',
        #                   'locator_value': '//*[@id="title"]',
        #                   'timeout': 3}
        #
        # self.plan_submit = {'element_name': '保存计划按钮',
        #                      'locator_type': 'xpath',
        #                      'locator_value': '//*[@id="submit"]',
        #                      'timeout': 3}
        # elements = ElementDataUtils('product_page').get_element_info()
        # self.go_product_page = elements['go_product_page']
        # self.plan_page = elements['plan_page']
        # self.add_plan_page = elements['add_plan_page']
        # self.plan_name = elements['plan_name']
        # self.plan_submit = elements['plan_submit']

        yaml_element = ElementYamlUtils().get_ymal_info()
        self.go_product_page = yaml_element['go_product_page']
        self.plan_page = yaml_element['plan_page']
        self.add_plan_page = yaml_element['add_plan_page']
        self.plan_name = yaml_element['plan_name']
        self.plan_submit = yaml_element['plan_submit']

    def go_to_product_page(self):
        self.click(self.go_product_page)

    def go_plan_page(self):
        self.click(self.plan_page)

    def go_add_plan_page(self):
        self.click(self.add_plan_page)

    def input_plan_name(self, story_name='test2'):
        self.input(self.plan_name, story_name)

    def click_plan_submit(self):
        self.click(self.plan_submit)