from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.login import common_login
driver = webdriver.Chrome()
bp = BasePage(driver)
frame_name1 = {'element_name': 'tanchuang',
                'locator_type': 'xpath',
                'locator_value': '//*[@id="iframe-triggerModal"]',
                'timeout': 3}


driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
common_login(driver)
sleep(2)
driver.find_element(By.XPATH, '//*[@id="subNavbar"]/ul/li[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="batchCreate"]/i').click()
# driver.switch_to.frame(frame_name)
bp.frame_switch(frame_name1)
sleep(2)
driver.find_element(By.XPATH, '//*[@id="switchDate0"]').click()
driver.find_element(By.XPATH, '//*[@id="submit"]').click()
bp.frame_default_content()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="batchCreate"]/i').click()


# driver.switch_to.default_content()
sleep(2)



sleep(2)


