from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """
    Класс MainPage представляет главную страницу приложения.

    Атрибуты:
        driver (WebDriver): Драйвер Selenium для взаимодействия с веб-страницей.
    """

    def __init__(self, driver):
        """
        Инициализация объекта MainPage.

        :param driver: Драйвер Selenium для управления браузером.
        """
        self.driver = driver
        self.cart_button = (By.CSS_SELECTOR, '.shopping_cart_link')

    def add_item_to_cart(self, item_name: str) -> None:
        """
        Добавить товар в корзину по имени.

        :param item_name: Имя товара, который необходимо добавить в корзину (строка).
        :return: None
        """
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, f"[data-test='add-to-cart-{item_name}']")
            )
        )
        add_to_cart_button.click()  # Нажимаем на кнопку добавления в корзину

    def go_to_cart(self) -> None:
        """
        Перейти в корзину.

        :return: None
        """
        cart_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_button)
        )
        cart_icon.click()