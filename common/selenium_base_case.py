import unittest
import warnings
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import local_config
from common.log_utils import logger


class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info('')
        logger.info('✈✈✈✈测试类开始执行✈✈✈✈!')
        warnings.simplefilter('ignore', ResourceWarning)
        cls.url = local_config.test_url

    def setUp(self) -> None:
        logger.info('♥❤♥❤测试方法开始执行♥❤♥❤!')
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_driver()

    def tearDown(self) -> None:
        errors = self._outcome.errors
        for test, exc_info in errors:
            if exc_info:
                self.base_page.wait(2)
                self.base_page.screenshot_as_file()
        logger.info('♥❤♥❤测试方法执行完毕♥❤♥❤!')
        self.base_page.quit_browser()

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('✈✈✈✈测试类执行完毕✈✈✈✈!')

