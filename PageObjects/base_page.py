import logging
import time

from telnetlib import EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support.wait import WebDriverWait
from Extention.WebDriverEx import WebDriverEx


# Базовая страница
class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Открытие ссылки
    def open(self):
        self.browser.get(self.url)

    # Открытие ссылки в новой вкладке
    def open_in_new_tab(self, url):
        WebDriverEx.open_in_new_tab(self.browser, url)

    # Переключение на вкладку со страницей
    # def switch_to(self):
    #     self.browser

    # Ожидание полной прогрузки страницы
    @staticmethod
    def wait_full_load(browser):
        js = 'return document.readyState;'
        wait = WebDriverWait(driver=browser, timeout=3)
        try:
            page_state = browser.execute_script(js)
            wait.until(lambda x: (page_state == "complete"), "страница не загрузилась за 3 сек.")
        except Exception as e:
            raise e

    def refresh_page(self):
        self.browser.refresh()
        self.wait_full_load(self.browser)

    # def wait_control(self):
    #
    # def wait_block(self):

    # Вынести в расширения
    # def is_element_present(self, how, what):
    #     try:
    #         self.browser.find_element(how, what)
    #     except NoSuchElementException:
    #         return False
    #     return True

    def wait(self, delay, locator):
        WebDriverWait(self.browser, delay).until(EC.presence_of_element_located(locator))

    def scroll_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView({block: \"center\"});", element)
        time.sleep(0.5)
