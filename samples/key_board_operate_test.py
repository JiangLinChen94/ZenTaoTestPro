from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common.base_page import BasePage
frame_name1 = {'element_name': 'tanchuang',
                'locator_type': 'id',
                'locator_value': 'kw',
                'timeout': 3}
driver = webdriver.Chrome()
bp = BasePage(driver)
driver.get('http://www.baidu.com')
driver.maximize_window()
bp.find_element(frame_name1).send_keys('asdfasdf')
bp.key_enter(frame_name1)
bp.key_ctrl_a(frame_name1)
bp.key_ctrl_c(frame_name1)
sleep(2)
bp.key_ctrl_v(frame_name1)

sleep(2)

