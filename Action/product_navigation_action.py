#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/5/11 20:51
from common.browser import Browser
from common.base_page import BasePage
from common.config_utils import local_config
from Action.login_action import LoginAction
from page.main_page.zentao_main_page import ZenTaoMainPage
from page.product_page.zentao_product_page import ZenTaoProductPage
from page.product_page.zentao_plan_page import ZenTaoPlanPage
from page.product_page.zentao_story_page import ZenTaoStoryPage


class ProductNavigationAction:
    def __init__(self, driver):
        self.main_page = ZenTaoMainPage(driver)
        self.product_page = ZenTaoProductPage(driver)
        self.plan_page = ZenTaoPlanPage(driver)
        self.story_page = ZenTaoStoryPage(driver)

    def go_product_page(self):
        self.main_page.go_product_page()
        return ZenTaoProductPage(self.product_page.driver)

    def go_plan_page(self):
        self.product_page.go_plan_page()
        return ZenTaoPlanPage(self.plan_page.driver)

    def go_story_page(self):
        self.product_page.go_story_page()
        return ZenTaoStoryPage(self.story_page.driver)


if __name__ == '__main__':
    driver = Browser().get_driver()
    login = LoginAction(driver)
    bp = BasePage(driver)
    bp.open_url(local_config.test_url)
    login.default_login()
    pna = ProductNavigationAction(driver)
    pna.go_product_page()
    bp.wait()
    pna.go_plan_page()
    bp.wait()
    pna.go_story_page()





