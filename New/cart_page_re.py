from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Класс CartPage представляет страницу корзины покупок.

    Атрибуты:
        driver (WebDriver): Драйвер Selenium для взаимодействия с веб-страницей.
    """

    def __init__(self, driver):
        """
        Инициализация объекта CartPage.

        :param driver: Драйвер Selenium для управления браузером.
        """
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, '.btn_action.checkout_button')

    def get_cart_item_count(self) -> int:
        """
        Получить количество товаров в корзине.

        :return: Количество элементов (товаров) в корзине (целое число).
        """
        return len(self.driver.find_elements(By.CSS_SELECTOR, '.cart_item'))

    def click_checkout(self) -> None:
        """
        Нажать кнопку 'Checkout'.

        :return: None
        """
        checkout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        )
        checkout_btn.click()