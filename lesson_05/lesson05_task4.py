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
    driver.get("http://the-internet.herokuapp.com/login")

    # Найти поле username и ввести значение
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    # Найти поле password и ввести значение
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Найти кнопку Login и нажать на неё
    login_button = driver.find_element(By.CSS_SELECTOR,
                                       "button[type='submit']")
    login_button.click()

    # Задержка на загрузку страницы после логина (по желанию)
    time.sleep(2)

    # Вывести текст с зеленой плашки в консоль
    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
    print(success_message.text)

    # Дополнительная задержка перед закрытием (по желанию)
    time.sleep(5)

finally:
    # Закрыть драйвер
    driver.quit()
