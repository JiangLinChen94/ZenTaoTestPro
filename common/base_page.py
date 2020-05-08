import os
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from common.log_utils import logger
from common.config_utils import local_config
from selenium.webdriver.support.wait import WebDriverWait

current_path = os.path.abspath(os.path.dirname(__file__))

class BasePage:

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    def open_url(self, url=None):
        """
        浏览器操作封装
        """
        if url is None:
            print('Please enter the url')
            logger.info('没有输入网址')
        else:
            self.driver.get(url)
            logger.info('打开url地址%s' % url)

    def quit_browser(self):
        """
        关闭浏览器
        """
        sleep(2)
        self.driver.quit()
        logger.info("关闭浏览器")

    def set_browser_max(self):
        """
        浏览器最大化
        """
        self.driver.maximize_window()
        logger.info("设置浏览器最大化")

    def set_browser_min(self):
        """
        浏览器最小化
        """
        self.driver.minimize_window()
        logger.info("设置浏览器最小化")

    def refresh(self):
        """
        刷新浏览器
        """
        self.driver.refresh()
        logger.info("浏览器刷新操作")

    def wait(self, seconds=local_config.time_out):
        """
        显示等待
        """
        sleep(seconds)

    def implicitly_wait(self, seconds=local_config.time_out):
        """
        隐式等待
        """
        self.driver.implicitly_wait(seconds)

    def get_title(self):
        """
        获取网页标题
        """
        value = self.driver.title
        logger.info("获取网页标题，标题是%s" % value)
        return value

    def set_driver(self):
        self.set_browser_max()
        self.open_url(local_config.test_url)

    def find_element(self, element_info):
        """
        元素定位方法
        """
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
        elif locator_type_name =='link_text':
            locator_type = By.LINK_TEXT
        elif locator_type_name == 'css_selector':
            locator_type = By.CSS_SELECTOR
        # element = WebDriverWait(self.driver, int(locator_timeout))\
        #     .until(lambda x: x.find_element(locator_type, locator_value_info))
        # logger.info("%s元素识别成功" % locator_element_name)
        element = WebDriverWait(self.driver, float(locator_timeout))\
            .until(EC.presence_of_element_located((locator_type_name, locator_value_info)))
        logger.info("%s元素识别成功" % locator_element_name)
        return element

    def click(self, element_info):
        """
        元素点击操作
        """
        self.find_element(element_info).click()
        logger.info('%s点击操作成功' % element_info['element_name'])

    def input(self, element_info, content):
        """
        元素输入操作
        """
        self.find_element(element_info).send_keys(content)
        logger.info("%s 输入内容【%s】" % (element_info['element_name'], content))

    # selenium 执行 js
    def target_locator(self):
        """
        下拉至底部
        """
        sleep(2)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        logger.info("下拉至底部")

    def execute_script(self, js_str, element_info=None):
        if element_info:
            self.driver.execute_script(js_str)
        else:
            self.driver.execute_script(js_str, None)

    def delete_element_attribute(self, element_info, attribute_name):
        element = self.find_element(element_info)
        self.execute_script('argument[0].removeAttribute("%s");' % attribute_name, element)

    def update_element_attribute(self, element_info, attribute_name, attribute_value):
        element = self.find_element(element_info)
        self.execute_script('argument[0].removeAttribute("%s","%s");' % (attribute_name, attribute_value), element)

    # 表单切换
    def frame_switch(self, frame_name=None):
        """
        表单切换
        """
        self.implicitly_wait()
        if frame_name is None:
            print("Please enter the form element to jump to")
            logger.info("没有输入页面元素")
        else:
            frame_name = self.find_element(frame_name)
            self.driver.switch_to.frame(frame_name)
            self.wait(2)
            logger.info("跳转至%s表单" % frame_name['element_name'])

    def frame_default_content(self):
        """
        切回初始表单
        """
        self.driver.switch_to.default_content()
        sleep(2)

    # 句柄切换
    def get_windows_handle(self):
        return self.driver.current_window_handle

    def switch_to_window_by_handle(self, window_handle):
        self.driver.switch_to.window(window_handle)

    # 根据title切换句柄
    def switch_to_window_by_title(self, title):
        window_handles = self.driver.current_window_handle
        for window_handle in window_handles:
            if WebDriverWait(self.driver, local_config.time_out).until(EC.title_contains(title)):
                self.driver.switch_to.window(window_handle)
                break

    # 根据url切换句柄
    def switch_to_window_by_url(self, url):
        window_handles = self.driver.current_window_handle
        for window_handle in window_handles:
            if WebDriverWait(self.driver, local_config.time_out).until(EC.url_contains(url)):
                self.driver.switch_to.window(window_handle)
                break



    def go_beginning_handle(self, current_handle):
        """
        返回初始表单
        """
        self.driver.switch_to.window(current_handle)
        title = self.driver.title
        logger.info('返回%s' % title)

    # 警告框
    def switch_to_alert(self, action='accept', time_out=local_config.time_out):
        WebDriverWait(self.driver, time_out).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        if action == 'accept':
            alert.accept()
        elif action == 'dismiss':
            alert.dismiss()
        return alert_text

    # 鼠标操作
    def move_to_element_by_mouse(self, element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).move_to_element(element).perform()

    def long_press_element(self, element_info, senconds = local_config.time_out):
        element = self.find_element(element_info)
        ActionChains(self.driver).click_and_hold(element).pause(senconds).release(element_info)

    def double_click_element(self, element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).double_click(element).perform()

    def drag_element(self, element_info, element_info2):
        """
        鼠标拖动操作
        """
        drag = self.find_element(element_info)
        drop = self.find_element(element_info2)
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()
        logger.info("正在将%s拖动至%s" % (element_info['element_name'], element_info2['element_name']))

    # 键盘操作
    def key_enter(self, element_info):
        """
        回车
        """
        self.find_element(element_info).send_keys(Keys.ENTER)
        logger.info("对%s进行回车" % element_info['element_name'])

    def key_ctrl_a(self, element_info):
        """
        全选
        """
        self.find_element(element_info).send_keys(Keys.CONTROL, 'a')
        logger.info("对%s全选" % element_info['element_name'])

    def key_ctrl_c(self, element_info):
        """
        复制
        """
        self.find_element(element_info).send_keys(Keys.CONTROL, 'c')
        logger.info("对%s复制" % element_info['element_name'])

    def key_ctrl_v(self, element_info):
        """
        粘贴
        """
        self.find_element(element_info).send_keys(Keys.CONTROL, 'v')
        logger.info("对%s粘贴" % element_info['element_name'])

    def key_ctrl_x(self, element_info):
        """
        剪切
        """
        self.find_element(element_info).send_keys(Keys.CONTROL, 'x')
        logger.info("对%s剪切" % element_info['element_name'])

    # 截图
    def screenshot_as_file(self, *screenshot_path):
        if len(screenshot_path) == 0:
            screenshot_filepath = local_config.screenshot_path
        else:
            screenshot_filepath = screenshot_path[0]
        now = time.strftime('%Y_%m_%d_%H_%M_%S_')
        print(now)
        screenshot_filepath = os.path.join(current_path, screenshot_filepath, 'UITest%s.png' % now)
        self.driver.get_screenshot_as_file(screenshot_filepath)

