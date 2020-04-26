import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        """
        浏览器操作封装
        """
        self.driver.get(url)
        logger.info('打开url地址%s' % url)

    def quit_browser(self):
        sleep(2)
        self.driver.quit()
        logger.info("关闭浏览器")

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info("设置浏览器最大化")

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info("设置浏览器最小化")

    def refresh(self):
        self.driver.refresh()
        logger.info("浏览器刷新操作")

    def get_title(self):
        value = self.driver.title
        logger.info("获取网页标题，标题是%s" % value)
        return value

    def set_driver(self):
        self.set_browser_max()
        self.open_url('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')

    def find_element(self, element_info):
        locator_element_name = element_info['element_name']
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'name':
            locator_type = By.NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        element = WebDriverWait(self.driver, int(locator_timeout))\
            .until(lambda x: x.find_element(locator_type, locator_value_info))
        logger.info("%s元素识别成功" % locator_element_name)
        # element = WebDriverWait(self.driver, locator_timeout)\
        #     .until(EC.presence_of_element_located(locator_type, locator_value_info))
        return element

    def click(self, element_info):
        self.find_element(element_info).click()
        logger.info('%s点击操作成功' % element_info['element_name'])

    def input(self, element_info, content):
        self.find_element(element_info).send_keys(content)
        logger.info("%s 输入内容【%s】" % (element_info['element_name'], content))

    def target_locator(self):
        sleep(2)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        logger.info("下拉至底部")

    def name_input(self, name):
        for i in range(100):
            name = i
        return 'test'+name