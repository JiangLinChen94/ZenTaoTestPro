from page.login_page.zentao_login_page import ZenTaoLoginPage


def common_login(driver):
    login = ZenTaoLoginPage(driver)
    login.input_username()
    login.input_password()
    login.click_login_button()

