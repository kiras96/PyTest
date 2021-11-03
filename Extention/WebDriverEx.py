from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.keys import Keys


class WebDriverEx:



    def open_in_new_tab(self, link):
        # Open new tab
        self.browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        # Load a page
        self.browser.get(link)
