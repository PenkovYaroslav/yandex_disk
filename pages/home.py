import allure
from selenium.common.exceptions import TimeoutException
from locators.home import LocatorsHome


class Home():

    def __init__(self, app):
        self.app = app

    def login(self, login, password):
        self.app.element_is_visible(LocatorsHome.HOME_LOGIN_BUTTON).click()
        self.app.element_is_visible(LocatorsHome.EMAIL_BUTTON).click()
        self.app.element_is_visible(LocatorsHome.USER_NAME_INPUT).send_keys(login)
        self.app.element_is_visible(LocatorsHome.LOGIN_BUTTON).click()
        self.app.element_is_visible(LocatorsHome.PASSWORD_INPUT).send_keys(password)
        self.app.element_is_visible(LocatorsHome.LOGIN_BUTTON).click()

    def is_logged_in(self):
        try:
            self.app.element_is_visible(LocatorsHome.HOME_LOGIN_BUTTON)
            return False
        except:
            return True

    def ensure_login(self, login, password):
        wd = self.app.wd
        if len(wd.window_handles) > 1:
            while len(wd.window_handles) != 1:
                wd.switch_to.window(wd.window_handles[len(wd.window_handles) - 1])
                wd.close()
        wd.switch_to.window(wd.window_handles[0])
        self.app.open_home_page()
        if not self.is_logged_in():
            self.login(login, password)

    def logout(self):
        try:
            self.app.element_is_visible(LocatorsHome.ACTION_BAR_CLOSE_BUTTON).click()
        except TimeoutException:
            pass
        self.app.element_is_visible(LocatorsHome.USER_MENU_BUTTON).click()
        self.app.element_is_visible(LocatorsHome.LOGOUT_BUTTON).click()
        pass

    @allure.step('Открываем страницу')
    def open_page(self, page):
        wd = self.app.wd
        pages_dict = {'disk': LocatorsHome.DISK_BUTTON,
                      'email': LocatorsHome.EMAIL_BUTTON}
        self.app.element_is_visible(pages_dict[page]).click()
        wd.switch_to.window(wd.window_handles[len(wd.window_handles) - 1])
