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
    (driver.get
     ("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"))

    # Ожидание, пока загрузится 4-е изображение или текст "Done!"
    print("Ожидание загрузки 4-го изображения или текста 'Done!'...")

    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '(//img)[4]'))
        # Ожидание конкретного элемента (4-е изображение)
    )

    # Теперь у нас есть уверенность, что 4-е изображение загружено
    fourth_image = driver.find_element(By.XPATH, '(//img)[4]')
    # Находим 4-е изображение

    # Получаем значение атрибута src у 4-й картинки
    fourth_image_src = fourth_image.get_attribute("src")
    print(f"URL четвертого изображения: {fourth_image_src}")

    # Вам также нужно убедиться, что текст "Done!" присутствует
    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
        # Ождание текста "Done!"
    )
    print("Загрузка завершена (текст 'Done!' найден).")

finally:
    # Закрыть драйвер
    driver.quit()
