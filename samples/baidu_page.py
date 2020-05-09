from selenium.webdriver.common.by import By


class BaiduPage:
    def __init__(self, driver):
        self.driver = driver

    def search_input(self, search_key):
        self.driver.find_element(By.ID, 'kw').send_keys(search_key)

    def search_button(self):
        self.driver.find_element(By.ID, 'su').click()

