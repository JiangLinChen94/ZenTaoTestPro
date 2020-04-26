import unittest
from selenium import webdriver
from common.login import common_login
from page.product_page.zentao_product_page import ZenTaoAddProductPage


class TestZenTaoAddProduct(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome()
        self.addpro = ZenTaoAddProductPage(driver)
        self.addpro.set_driver()
        common_login(driver)

    def test_add_product_success(self):
        """
        添加产品成功
        """
        self.addpro.go_product_page()
        self.addpro.go_add_product_page()
        self.addpro.input_product_name()
        self.addpro.input_product_code()
        self.addpro.target_locator()
        self.addpro.product_submit_button()

    def test_add_product_name_null_error(self):
        """
        产品名称为空添加失败
        """
        self.addpro.go_product_page()
        self.addpro.go_add_product_page()
        self.addpro.input_product_name('')
        self.addpro.input_product_code('test2')
        self.addpro.target_locator()
        self.addpro.product_submit_button()

    def test_add_product_code_null_error(self):
        """
        产品代号为空添加失败
        """
        self.addpro.go_product_page()
        self.addpro.go_add_product_page()
        self.addpro.input_product_name('alin2')
        self.addpro.input_product_code('')
        self.addpro.target_locator()
        self.addpro.product_submit_button()

    def tearDown(self):
        self.addpro.quit_browser()


if __name__ == "__main__":
    unittest.main()