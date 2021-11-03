from TestManagers.TestManager import TestManager


def test_main(browser):
    TestManager.open_test_page(browser)

