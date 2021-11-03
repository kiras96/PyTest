import time

from PageObjects.test_page import TestPage


class TestManager:

    @staticmethod
    def open_test_page(browser):
        test_page = TestPage(browser, TestPage.URL)
        test_page.open()
        test_page.wait_full_load(browser)
