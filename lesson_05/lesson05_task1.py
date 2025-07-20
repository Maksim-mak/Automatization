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
    driver.get("http://uitestingplayground.com/classattr")

    # Настройка задержки для загрузки страницы (по желанию)
    time.sleep(2)  # Подождите, чтобы страница успела загрузиться

    # Найти и кликнуть на синюю кнопку по CSS-классу
    button = driver.find_element(By.CSS_SELECTOR,
                                 ".btn.btn-primary")
    # Измените селектор, если необходимо
    button.click()

    # Дополнительная задержка на случай, если нужно увидеть результат
    time.sleep(5)
finally:
    # Закрыть драйвер
    driver.quit()
