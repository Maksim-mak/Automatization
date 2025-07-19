from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Инициализация драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Открыть веб-страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Нажать на синюю кнопку
    button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    # Ожидание появления текста в зеленой плашке
    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".bg-success"),
            "Data loaded with AJAX get request.")
    )

    # Получить текст из зеленой плашки
    success_message = driver.find_element(By.CSS_SELECTOR, ".bg-success")
    print(success_message.text)

finally:
    # Закрыть драйвер
    driver.quit()
