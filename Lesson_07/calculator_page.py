# calculator_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        # Локаторы
        self.delay_input = (By.CSS_SELECTOR, '#delay')  # Если поле для задержки есть на странице
        self.button7 = (By.XPATH, "//span[text()='7']")
        self.button8 = (By.XPATH, "//span[text()='8']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.result_output = (By.CSS_SELECTOR, '.screen')  # Локатор для поля вывода результата

    def set_delay(self, delay):
        """Ввод значения в поле задержки."""
        delay_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.delay_input)
        )
        delay_element.clear()
        delay_element.send_keys(delay)

    def press_button7(self):
        """Нажать кнопку '7'."""
        button7_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button7)
        )
        button7_element.click()

    def press_button8(self):
        """Нажать кнопку '8'."""
        button8_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button8)
        )
        button8_element.click()

    def press_button_plus(self):
        """Нажать кнопку '+'."""
        button_plus_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_plus)
        )
        button_plus_element.click()

    def press_button_equals(self):
        """Нажать кнопку '='."""
        button_equals_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_equals)
        )
        button_equals_element.click()

    def get_result(self):
        """Получить результат вычисления."""
        result_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.result_output)
        )
        return result_element.text