from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Класс CalculatorPage представляет страницу калькулятора.

    Атрибуты:
        driver (WebDriver): Драйвер Selenium для взаимодействия с веб-страницей.
    """

    def __init__(self, driver):
        """
        Инициализация объекта CalculatorPage.

        :param driver: Драйвер Selenium для управления браузером.
        """
        self.driver = driver
        # Локаторы
        self.delay_input = (By.CSS_SELECTOR, '#delay')
        self.button7 = (By.XPATH, "//span[text()='7']")
        self.button8 = (By.XPATH, "//span[text()='8']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.result_output = (By.CSS_SELECTOR, '.screen')

    def set_delay(self, delay: str) -> None:
        """
        Ввод значения в поле задержки.

        :param delay: Значение задержки, которое будет введено в поле (строка).
        :return: None
        """
        delay_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.delay_input)
        )
        delay_element.clear()
        delay_element.send_keys(delay)

    def press_button7(self) -> None:
        """
        Нажать кнопку '7'.

        :return: None
        """
        button7_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button7)
        )
        button7_element.click()

    def press_button8(self) -> None:
        """
        Нажать кнопку '8'.

        :return: None
        """
        button8_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button8)
        )
        button8_element.click()

    def press_button_plus(self) -> None:
        """
        Нажать кнопку '+'.

        :return: None
        """
        button_plus_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_plus)
        )
        button_plus_element.click()

    def press_button_equals(self) -> None:
        """
        Нажать кнопку '='.

        :return: None
        """
        button_equals_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_equals)
        )
        button_equals_element.click()

    def get_result(self) -> str:
        """
        Получить результат вычисления.

        :return: Результат вычисления (строка).
        """
        result_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.result_output)
        )
        return result_element.text