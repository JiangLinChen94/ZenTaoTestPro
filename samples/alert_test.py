from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from page.login_page.zentao_login_page import ZenTaoLoginPage

driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')
driver.implicitly_wait(10)
bp=BasePage(driver)
bp.set_browser_max()
login = ZenTaoLoginPage(driver)
login.click_login_button()
# driver.find_element(By.XPATH, '//*[@id="s-usersetting-top"]').click()
# driver.find_element(By.LINK_TEXT, '搜索设置').click()
# sleep(2)
# driver.find_element(By.CLASS_NAME, 'prefpanelgo').click()
# sleep(2)
# alert = driver.switch_to.alert
# sleep(2)
# alert_text = alert.text
# print(alert_text)
# sleep(2)
# alert.accept()
bp.switch_to_alert()
bp.quit_browser()