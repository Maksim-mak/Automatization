from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Класс CheckoutPage представляет страницу оформления заказа.

    Атрибуты:
        driver (WebDriver): Драйвер Selenium для взаимодействия с веб-страницей.
    """

    def __init__(self, driver):
        """
        Инициализация объекта CheckoutPage.

        :param driver: Драйвер Selenium для управления браузером.
        """
        self.driver = driver
        self.first_name_input = (By.ID, 'first-name')
        self.last_name_input = (By.ID, 'last-name')
        self.zip_code_input = (By.ID, 'postal-code')
        self.continue_button = (By.CSS_SELECTOR, '.btn_primary.cart_button')
        self.total_price = (By.CSS_SELECTOR, '.summary_total_label')

    def fill_out_form(self, first_name: str, last_name: str, zip_code: str) -> None:
        """
        Заполнение формы оформления заказа.

        :param first_name: Имя покупателя (строка).
        :param last_name: Фамилия покупателя (строка).
        :param zip_code: Почтовый индекс покупателя (строка).
        :return: None
        """
        first_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input)
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name_input)
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        zip_code_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.zip_code_input)
        )
        zip_code_field.clear()
        zip_code_field.send_keys(zip_code)

    def click_continue(self) -> None:
        """
        Нажал на кнопку 'Продолжить'.

        :return: None
        """
        continue_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        )
        continue_btn.click()

    def get_total_price(self) -> str:
        """
        Получить общую стоимость заказа.

        :return: Общая стоимость заказа (строка).
        """
        total_label = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_price)
        )
        return total_label.text