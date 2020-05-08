from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base_page import BasePage
mouse_name = {'element_name': 'TEST',
                'locator_type': 'css_selector',
                'locator_value': '#draggable',
                'timeout': 3}

mouse_name2 = {'element_name': 'TEST',
                'locator_type': 'css_selector',
                'locator_value': '#droppable',
                'timeout': 3}

mouse_name3 = {'element_name': 'TEST',
                'locator_type': 'xpath',
                'locator_value': '//*[@id="u1"]/a[9]',
                'timeout': 3}

driver = webdriver.Chrome()
bp = BasePage(driver)
# driver.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# driver.maximize_window()
bp.open_url('http://www.baidu.com')
bp.set_browser_max()

#
# # bp.mouse_operation(mouse_name, mouse_operate='move_to_element')
# driver.switch_to.frame('iframeResult')
# sleep(2)
# bp.drag_element(mouse_name, mouse_name2)
#
bp.move_to_element_by_mouse(mouse_name)
# e = driver.find_element(By.XPATH, '//*[@id="u1"]/a[9]')
# ActionChains(driver).move_to_element(e).perform()