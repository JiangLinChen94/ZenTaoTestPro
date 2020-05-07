from common.base_page import BasePage
from common.element_data_utils import ElementDataUtils
from common.element_yaml_utils import ElementYamlUtils


class ZenTaoAddStoryPage(BasePage):
    def __init__(self,  driver):
        super().__init__(driver)
        # self.product_page = {'element_name': '前往产品页面',
        #                      'locator_type': 'xpath',
        #                      'locator_value': "//li[@data-id='product']",
        #                      'timeout': 3}
        #
        # self.story_page = {'element_name': '故事页面',
        #                    'locator_type': 'xpath',
        #                    'locator_value': "//*[@id='subNavbar']/ul/li[1]",
        #                    'timeout': 3}
        #
        # self.add_story_page = {'element_name': '提故事页面',
        #                        'locator_type': 'xpath',
        #                        'locator_value': '//*[@id="mainMenu"]/div[3]/a[3]/i',
        #                        'timeout': 3}
        #
        # self.story_name = {'element_name': '故事名称',
        #                          'locator_type': 'xpath',
        #                          'locator_value': '//*[@id="title"]',
        #                          'timeout': 3}
        #
        # self.story_submit = {'element_name': '保存故事按钮',
        #                      'locator_type': 'xpath',
        #                      'locator_value': '//*[@id="submit"]',
        #                      'timeout': 3}
        main_elements = ElementDataUtils('main', 'main_page').get_element_info()
        self.go_product_page = main_elements['product_page']
        story_elements = ElementDataUtils('product', 'story_page').get_element_info()
        self.story_page = story_elements['story_page']
        self.add_story_page = story_elements['add_story_page']
        self.story_name = story_elements['story_name']
        self.story_submit = story_elements['story_submit']
        # yaml_elements = ElementYamlUtils().get_ymal_info()
        # self.go_product_page = yaml_elements['go_product_page']
        # self.story_page = yaml_elements['story_page']
        # self.add_story_page = yaml_elements['add_story_page']
        # self.story_name = yaml_elements['story_name']
        # self.story_submit = yaml_elements['story_submit']

    def go_to_product_page(self):
        self.click(self.go_product_page)

    def go_story_page(self):
        self.click(self.story_page)

    def go_add_story_page(self):
        self.click(self.add_story_page)

    def input_story_name(self, story_name='test2'):
        self.input(self.story_name, story_name)

    def click_story_submit(self):
        self.click(self.story_submit)