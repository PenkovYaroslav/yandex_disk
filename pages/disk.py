import os
import time
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from locators.disk import LocatorsDisk
from generator.generator import generated_file


class Disk():

    def __init__(self, app):
        self.app = app

    @allure.step('Создаем папку/документ')
    def create(self, type, name):
        """
        method for creating a file or folder
        :param type: folder or file
        :param name: name folder or file
        :return:
        """
        wd = self.app.wd
        type_dict = {'folder': LocatorsDisk.FOLDER_BUTTON,
                     'file': LocatorsDisk.FILE_BUTTON}
        self.app.element_is_visible(LocatorsDisk.CREATE_BUTTON).click()
        self.app.element_is_visible(type_dict[type]).click()
        time.sleep(1)
        self.app.element_is_visible(LocatorsDisk.NAME_INPUT).send_keys(Keys.BACK_SPACE)
        self.app.element_is_visible(LocatorsDisk.NAME_INPUT).send_keys(name)
        self.app.element_is_visible(LocatorsDisk.SUBMIT_BUTTON).click()
        if type == 'file':
            wd.switch_to.window(wd.window_handles[len(wd.window_handles) - 1])

    @allure.step('Открываем папку/файл')
    def open(self, type, name):
        wd = self.app.wd
        self.app.double_click(self.app.element_is_visible(locator=(By.XPATH, f'//div[@aria-label="{name}"]')))
        if type == 'file':
            wd.switch_to.window(wd.window_handles[len(wd.window_handles) - 1])

    @allure.step('Закрываем файл')
    def file_close(self):
        wd = self.app.wd
        wd.close()
        wd.switch_to.window(wd.window_handles[len(wd.window_handles) - 1])

    @allure.step('Получаем кол-во файлов в текущей папке')
    def get_count_files(self):
        try:
            files = self.app.elements_are_visible(LocatorsDisk.FILES)
            count_files = len(files)
            name_files = []
            for file in files:
                name_files.append(file.get_attribute('title').split('.')[0])
            return count_files, name_files
        except TimeoutException:
            return 0

    @allure.step('Загружаем файл')
    def upload_file(self):
        file_name, path, text = generated_file()
        self.app.element_is_present(LocatorsDisk.UPLOAD_INPUT).send_keys(path)
        self.app.element_is_visible(LocatorsDisk.UPLOAD_PROGRESS_TEXT, 10)
        self.app.element_is_visible(LocatorsDisk.UPLOAD_FILE_CLOSE_BUTTON).click()
        os.remove(path)
        return file_name.split('\\')[-1], text

    @allure.step('Получеем текст документа')
    def get_text_file_txt(self):
        element = self.app.element_is_visible(LocatorsDisk.TEXT_FILE)
        return element.text
