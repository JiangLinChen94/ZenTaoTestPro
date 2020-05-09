import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from samples.baidu_page import BaiduPage

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'http://www.baidu.com'

    def test_baidu_search_case1(self):
        self.driver.get(self.base_url)
        bd = BaiduPage(self.driver)
        bd.search_input('selenium')
        bd.search_button()


    def test_baidu_search_case2(self):
        self.driver.get(self.base_url)
        bd = BaiduPage(self.driver)
        bd.search_input('unittest')
        bd.search_button()

    def test_baidu_search_case3(self):
        self.driver.get(self.base_url)
        bd = BaiduPage(self.driver)
        bd.search_input('page object')
        bd.search_button()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
