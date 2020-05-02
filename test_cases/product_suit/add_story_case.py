import unittest
from selenium import webdriver
from common.login import common_login
from common.browser import Browser
from page.product_page.zentao_story_page import ZenTaoAddStoryPage


class TestZenTaoAddProduct(unittest.TestCase):

    def setUp(self):
        driver = Browser().get_driver()
        self.addstory = ZenTaoAddStoryPage(driver)
        self.addstory.set_driver()
        common_login(driver)

    def test_add_story_success(self):
        """
        添加故事成功
        """
        self.addstory.go_to_product_page()
        self.addstory.go_story_page()
        self.addstory.go_add_story_page()
        self.addstory.input_story_name()
        self.addstory.target_locator()
        self.addstory.click_story_submit()

    def test_add_story_name_null_error(self):
        """
        故事名称为空添加失败
        """
        self.addstory.go_to_product_page()
        self.addstory.go_story_page()
        self.addstory.go_add_story_page()
        self.addstory.input_story_name('')
        self.addstory.target_locator()
        self.addstory.click_story_submit()

    def tearDown(self):
        self.addstory.quit_browser()


if __name__ == "__main__":
    unittest.main()