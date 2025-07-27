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

    # Ждем, пока не появится новое сообщение или подтверждение после отправки формы
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
