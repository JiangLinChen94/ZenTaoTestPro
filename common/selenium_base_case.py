import unittest
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import local_config


class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = local_config.test_url

    def setUp(self) -> None:
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_driver()

    def tearDown(self) -> None:
        self.base_page.quit_browser()

