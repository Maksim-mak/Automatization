import pytest
import allure
from selenium import webdriver
from Lesson_07.calculator_page import CalculatorPage
from time import sleep


@pytest.fixture()
def driver() -> webdriver.Chrome:
    """
    Фикстура для создания и закрытия WebDriver.

    :return: Объект WebDriver для работы с браузером.
    """
    driver = webdriver.Chrome()  # Убедитесь, что chromedriver находится в PATH
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


@allure.title("Тест функциональности калькулятора")
@allure.description("Проверка функциональности калькулятора с задержкой.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver) -> None:
    """
    Тест для проверки функциональности калькулятора.

    :param driver: WebDriver объект, предоставляемый фикстурой.
    :return: None
    """
    page = CalculatorPage(driver)

    with allure.step("Ввод значения 45 в поле задержки"):
        page.set_delay("45")

    with allure.step("Выполнение операций: 7 + 8"):
        page.press_button7()
        page.press_button_plus()
        page.press_button8()
        page.press_button_equals()

    with allure.step("Ожидание 45 секунд для получения результата"):
        sleep(45)  # Это время соответствует значению задержки в 45 секунд

    with allure.step("Проверка результата"):
        result = page.get_result()
        assert result == "15", f"Ожидалось 15, но было {result}"