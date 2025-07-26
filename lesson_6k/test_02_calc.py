import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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
    (driver.get
     ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"))

    # Ввод задержки
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()  # Очищаем поле перед вводом
    delay_input.send_keys("45")

    # Добавляем паузу после ввода задержки
    time.sleep(2)

    # Функция для клика по кнопкам с дополнительной проверкой
    def click_button(button_text):
        try:
            # Ждем появления кнопки
            button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable
                ((By.XPATH,
                  f"//span[contains(@class, 'btn') and text()='"
                  f"{button_text}']"))
            )

            # Проверяем, что кнопка активна и видима
            if button.is_enabled() and button.is_displayed():
                button.click()
                print(f"Нажата кнопка: {button_text}")
            else:
                raise (Exception
                       (f"Кнопка {button_text} не активна или не видна"))

        except Exception as e:
            print(f"Ошибка при клике на кнопку {button_text}: {str(e)}")
            raise

    try:
        # Нажимаем кнопки последовательно
        click_button('7')
        click_button('+')
        click_button('8')
        click_button('=')

        # Увеличенный пауза после нажатия "="
        time.sleep(20)  # Увеличено до 20 секунд

        # Используйте правильный XPath для поиска результата
        result = WebDriverWait(driver, 300).until(  # 5 минут ожидания
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='calculator']/div[1]/div")
            )
        )

        # Ждем, пока результат обновится до финального значения
        WebDriverWait(driver, 120).until(
            lambda d: d.find_element(By.XPATH,
                                     "//*[@id='calculator']"
                                     "/div[1]/div").text == "15"
        )

        # Получаем финальный результат
        final_result = result.text
        print(f"Полученный результат: {final_result}")

        # Проверяем полученный результат
        assert final_result == "15", f"Ожидалось 15, получено {final_result}"
        print("Тест пройден успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        raise


if __name__ == "__main__":
    pytest.main()
