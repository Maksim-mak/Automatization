import pytest
from selenium import webdriver
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchElementException

@pytest.fixture
def driver():
    service = SafariService()
    options = webdriver.SafariOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Safari(service=service, options=options)
    yield driver
    driver.quit()

def test_form_filling(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Ждем, пока поля формы загрузятся
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "first-name")))

    # Заполнение полей формы
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in fields.items():
        driver.find_element(By.NAME, field_name).send_keys(value)

    # Отправка формы
    submit_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

    try:
        submit_button.click()
    except ElementNotInteractableException:
        driver.execute_script("arguments[0].click();", submit_button)

    # Ждем появления результатов валидации
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))

    # Функция для проверки статуса поля
    def check_field_status(field_id, expected_class):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, field_id))
            )
            actual_class = element.get_attribute("class")
            if expected_class in actual_class:
                print(f"✅ Поле {field_id} имеет ожидаемый статус: {expected_class}")
                return True
            else:
                print(f"❌ Ошибка: поле {field_id} имеет неожиданный статус. Ожидалось: {expected_class}, фактически: {actual_class}")
                return False
        except Exception as e:
            print(f"Ошибка при проверке поля {field_id}: {str(e)}")
            return False

    # Список полей, которые должны быть зелеными
    green_fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]

    # Проверяем зеленые поля
    for field in green_fields:
        assert check_field_status(field, "alert-success"), f"Поле {field} не прошло валидацию"

    # Проверяем, что zip-code красное
    assert check_field_status("zip-code", "alert-danger"), "Поле zip-code не отмечено как невалидное"
