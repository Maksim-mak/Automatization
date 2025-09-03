# test_calculator.py
import pytest
from selenium import webdriver
from calculator_page import CalculatorPage
from time import sleep


@pytest.fixture()
def driver():
    """Фикстура для создания и закрытия драйвера."""
    driver = webdriver.Chrome()  # Убедитесь, что chromedriver находится в PATH
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calculator(driver):
    """Тест для проверки функциональности калькулятора."""
    page = CalculatorPage(driver)

    # Ввод значения 45 в поле задержки
    page.set_delay("45")

    # Выполнение операций: 7 + 8
    page.press_button7()
    page.press_button_plus()
    page.press_button8()
    page.press_button_equals()

    # Ожидание 45 секунд для получения результата
    sleep(45)  # Это время соответствует значению задержки в 45 секунд

    # Проверка результата
    result = page.get_result()
    assert result == "15", f"Ожидалось 15, но было {result}"