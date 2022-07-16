from selenium.webdriver.common.by import By


class LocatorsHome:
    # session locators
    HOME_LOGIN_BUTTON = (By.XPATH, '//div[@class="desk-notif-card__login-new-item-title" and text()="Войти"]')
    EMAIL_BUTTON = (By.XPATH, '//button[@data-type="login"]')
    USER_NAME_INPUT = (By.CSS_SELECTOR, '#passp-field-login')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#passp-field-passwd')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#passp\:sign-in')
    USER_MENU_BUTTON = (By.XPATH, '//a[@aria-label="Аккаунт"]/div')
    LOGOUT_BUTTON = (By.XPATH, '//span[contains(@class, "menu__text") and text()="Выйти"]')
    ACTION_BAR_CLOSE_BUTTON = (By.XPATH, '//button[@aria-label="Отменить выделение"]')
    # page locators
    DISK_BUTTON = (By.XPATH, '//a[@class="home-link home-link_black_yes" and text()="Диск"]')
    MAIL_BUTTON = (By.XPATH, '//div[@class="desk-notif-card__mail-title" and text()="Почта"]')
