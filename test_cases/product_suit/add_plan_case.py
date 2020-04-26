import unittest
from selenium import webdriver
from common.login import common_login
from page.product_page.zentao_plan_page import ZenTaoAddPlanPage


class TestZenTaoAddProduct(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome()
        self.addplan = ZenTaoAddPlanPage(driver)
        self.addplan.set_driver()
        common_login(driver)

    def test_add_story_success(self):
        """
        添加故事成功
        """
        self.addplan.go_to_product_page()
        self.addplan.go_plan_page()
        self.addplan.go_add_plan_page()
        self.addplan.input_plan_name()
        self.addplan.target_locator()
        self.addplan.click_plan_submit()

    def test_add_story_name_null_error(self):
        """
        故事名称为空添加失败
        """
        self.addplan.go_to_product_page()
        self.addplan.go_plan_page()
        self.addplan.go_add_plan_page()
        self.addplan.input_plan_name('')
        self.addplan.target_locator()
        self.addplan.click_plan_submit()

    def tearDown(self):
        self.addplan.quit_browser()


if __name__ == "__main__":
    unittest.main()