from selenium.webdriver.common.by import By


class LocatorsDisk:
    UPLOAD_INPUT = (By.XPATH, '//input[@title="Загрузить файлы"]')
    CREATE_BUTTON = (By.XPATH, '//span[text()="Создать"]/../..')
    FOLDER_BUTTON = (By.XPATH, '//button[@aria-label="Папку"]')
    FILE_BUTTON = (By.XPATH, '//button[@aria-label="Текстовый документ"]')
    NAME_INPUT = (By.XPATH, '//div[@class="Modal-Content"]//input')
    SUBMIT_BUTTON = (By.XPATH, '//div[@class="Modal-Content"]//button[contains(@class, "submit")]')
    FILES = (By.XPATH, '//div[@class="listing__items"]/div[@tabindex]//span')
    TEXT_FILE = (By.XPATH, '//p[@class="mg1"]')
    UPLOAD_FILE_CLOSE_BUTTON = (By.XPATH, '//button[@aria-label="Закрыть"]')