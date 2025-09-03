import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Настройка Chrome драйвера
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Максимизация окна
    options.add_argument("--disable-gpu")  # Отключение GPU
    options.add_argument("--disable-dev-shm-usage")  # Для Linux
    options.add_argument("--no-sandbox")  # Для Linux
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_calculator(driver):
    # Открытие страницы калькулятора
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Ввод задержки
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()  # Очищаем поле перед вводом
    delay_input.send_keys("45")  # Задаем задержку в 45 секунд

    # Функция для клика по кнопкам
    def click_button(button_text):
        # Ждем появления кнопки и проверяем, что она кликабельна
        button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[contains(@class, 'btn') and text()='{button_text}']")
            )
        )
        button.click()  # Кликаем по кнопке

    # Нажимаем кнопки последовательно
    click_button('7')
    click_button('+')
    click_button('8')
    click_button('=')

    # Ожидаем, пока результат обновится до нужного значения
    result_element = WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, "//*[@id='calculator']/div[1]/div"), "15"
        )
    )

    # Проверка результата
    result_text = driver.find_element(By.XPATH, "//*[@id='calculator']/div[1]/div").text
    assert result_text == "15", f"Ожидалось 15, получено {result_text}"
