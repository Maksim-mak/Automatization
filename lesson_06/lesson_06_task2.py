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
    driver.get("http://uitestingplayground.com/textinput")

    # Найти поле ввода и ввести текст "SkyPro"
    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    input_field.send_keys("SkyPro")

    # Найти кнопку и нажать на неё
    button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()

    # Подождать, чтобы нажатие кнопки завершилось (по желанию)
    time.sleep(2)

    # Получить текст кнопки и вывести в консоль
    button_text = button.text
    print(button_text)  # Ожидаемый вывод: "SkyPro"

finally:
    # Закрыть драйвер
    driver.quit()
