from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from pages.disk import Disk
from pages.home import Home


class Application:

    def __init__(self, browser, base_url):
        if browser == "chrome":
            wd_service = Service(ChromeDriverManager().install())
            self.wd = webdriver.Chrome(service=wd_service)
        else:
            raise ValueError("Unrecognized browser")
        self.base_url = base_url
        self.home = Home(self)
        self.disk = Disk(self)

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)
        wd.maximize_window()

    def destroy(self):
        wd = self.wd
        wd.quit()

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.wd, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.wd, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return Wait(self.wd, timeout).until(EC.presence_of_element_located(locator))

    def double_click(self, element):
        action = ActionChains(self.wd)
        action.double_click(element)
        action.perform()
