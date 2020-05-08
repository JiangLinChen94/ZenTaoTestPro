from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.login import common_login

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
bp = BasePage(driver)

# search_windows = driver.current_window_handle
a = bp.switch_to_window_by_title(bp.get_title())
driver.find_element(By.XPATH, '//*[@id="lg"]/map/area').click()
# all_handles = driver.window_handles
# for handle in all_handles:
#     if handle != bp.all_handles():
#         driver.switch_to.window(handle)
#         print(driver.title)
# driver.switch_to.window(bp.get_current_handle())
sleep(2)
bp.go_beginning_handle(a)
