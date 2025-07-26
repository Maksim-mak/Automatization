import pytest
from selenium import webdriver
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import (TimeoutException,
                                        ElementNotInteractableException)


@pytest.fixture
def driver():
    service = SafariService()
    options = webdriver.SafariOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Safari(service=service, options=options)
    yield driver
    driver.quit()


def test_form_filling(driver):
    driver.get("https://bonigarcia.dev/"
               "selenium-webdriver-java/data-types.html")

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "first-name"))
    )

    # Заполнение формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Находим кнопку Submit и жмем ее
    submit_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

    # Пытаемся кликнуть по кнопке
    try:
        submit_button.click()
    except ElementNotInteractableException:
        driver.execute_script("arguments[0].click();", submit_button)

    time.sleep(3)

    # Функция для получения статуса поля
    def print_field_status(field_id):
        try:
            field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, field_id))
            )
            classes = field.get_attribute("class")  # Получаем классы поля
            print(f"Field '{field_id}' "
                  f"has classes: {classes}")  # Выводим классы в консоль
            return classes
        except TimeoutException:
            print(f"Field '{field_id}' is not visible.")
            return None

    # Проверяем результаты валидации каждого поля и выводим классы
    field_ids = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "zip-code"  # Предполагаем, что это поле должно быть с ошибкой
    ]

    for field_id in field_ids:
        print_field_status(field_id)  # Выводим статус каждого поля
