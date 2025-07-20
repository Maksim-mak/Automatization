from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Инициализация драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Открыть веб-страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Найти поле ввода по CSS-селектору
    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

    # Ввести текст "Sky"
    input_field.send_keys("Sky")

    # Очистить поле ввода
    input_field.clear()

    # Ввести текст "Pro"
    input_field.send_keys("Pro")

    # Настройка задержки, чтобы увидеть результат (по желанию)
    time.sleep(5)

finally:
    # Закрыть драйвер
    driver.quit()
