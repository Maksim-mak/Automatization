from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Класс LoginPage представляет страницу для входа в систему.

    Атрибуты:
        driver (WebDriver): Драйвер Selenium для взаимодействия с веб-страницей.
    """

    def __init__(self, driver):
        """
        Инициализация объекта LoginPage.

        :param driver: Драйвер Selenium для управления браузером.
        """
        self.driver = driver
        self.username_input = (By.ID, 'user-name')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.CSS_SELECTOR, '.btn_action')

    def enter_username(self, username: str) -> None:
        """
        Ввод имени пользователя в поле ввода.

        :param username: Имя пользователя (строка).
        :return: None
        """
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        )
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Ввод пароля в поле ввода.

        :param password: Пароль пользователя (строка).
        :return: None
        """
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self) -> None:
        """
        Нажать на кнопку 'Вход'.

        :return: None
        """
        login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_btn.click()