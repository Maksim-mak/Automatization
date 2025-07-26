from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_shopping_cart():
    # Настраиваем драйвер Firefox
    driver = webdriver.Firefox()  # Убедитесь, что GeckoDriver добавлен в PATH
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    # Авторизуемся как стандартный пользователь
    wait.until(EC.visibility_of_element_located
               ((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # Добавляем товары в корзину
    try:
        (wait.until(EC.element_to_be_clickable
                    ((By.XPATH,
                      "//button"
                      "[@id='add-to-cart-sauce-labs-backpack']"))).click())
        wait.until(
            EC.element_to_be_clickable
            ((By.XPATH,
              "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
        wait.until(EC.element_to_be_clickable
                   ((By.XPATH,
                     "//button[@id='add-to-cart-sauce-labs-onesie']"))).click()
    except Exception as e:
        print("Ошибка при добавлении товара в корзину:", str(e))
        driver.quit()
        return

    # Переходим в корзину
    wait.until(EC.element_to_be_clickable
               ((By.CLASS_NAME, "shopping_cart_link"))).click()

    # Нажимаем Checkout
    wait.until(EC.element_to_be_clickable
               ((By.XPATH, "//button[text()='Checkout']"))).click()

    # Заполняем форму своими данными
    wait.until(EC.visibility_of_element_located
               ((By.ID, "first-name"))).send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Иванов")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    # Нажимаем кнопку Continue
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # Проверяем итоговую стоимость
    total_label = (wait.until
                   (EC.visibility_of_element_located
                    ((By.CSS_SELECTOR, ".summary_info .summary_total_label"))))
    total_text = total_label.text
    print("Итоговая стоимость:", total_text)

    # Проверяем, что итоговая сумма равна $58.29
    assert total_text == "Total: $58.29", \
        (f"Ожидалось, что итоговая сумма будет $58.29, но получено: "
         f"{total_text}")

    # Закрываем драйвер
    driver.quit()


if __name__ == "__main__":
    pytest.main()
