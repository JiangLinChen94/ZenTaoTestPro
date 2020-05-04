from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.base_page import BasePage

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.implicitly_wait(10)
bp=BasePage(driver)
link = driver.find_element(By.LINK_TEXT, '设置').click()
driver.find_element(By.LINK_TEXT, '搜索设置').click()
sleep(2)

driver.find_element(By.CLASS_NAME, 'prefpanelgo').click()
# sleep(2)
# alert = driver.switch_to.alert
# sleep(2)
# alert_text = alert.text
# print(alert_text)
# sleep(2)
# alert.accept()
bp.get_alert()