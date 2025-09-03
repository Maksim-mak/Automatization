import pytest
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture()
def driver() -> webdriver.Chrome:
    """
    Фикстура для создания и закрытия WebDriver.

    :return: Объект WebDriver для работы с браузером.
    """
    driver = webdriver.Chrome()  # Убедитесь, что chromedriver находится в PATH
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_purchase_flow(driver) -> None:
    """
    Тест для проверки потока покупки.

    Проверяет, что после входа в систему можно добавить товары в корзину,
    перейти к их проверке и оформить покупку.

    :param driver: WebDriver объект, предоставляемый фикстурой.
    :return: None
    """
    # Страница авторизации
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Главная страница
    main_page = MainPage(driver)
    main_page.add_item_to_cart("sauce-labs-backpack")  # Добавляем "Sauce Labs Backpack"
    main_page.add_item_to_cart("sauce-labs-bolt-t-shirt")  # Добавляем "Sauce Labs Bolt T-Shirt"
    main_page.add_item_to_cart("sauce-labs-onesie")  # Добавляем "Sauce Labs Onesie"
    main_page.go_to_cart()

    # Проверка товаров в корзине
    cart_page = CartPage(driver)
    cart_item_count = cart_page.get_cart_item_count()
    assert cart_item_count == 3, \
        (f"Количество товаров в корзине должно быть 3, "
         f"но было {cart_item_count}.")

    # Переход на страницу оформления заказа
    cart_page.click_checkout()

    # Страница оформления заказа
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_out_form("John", "Doe", "12345")  # Заполнение формы
    checkout_page.click_continue()

    # Проверка итоговой суммы
    total_price = checkout_page.get_total_price()
    assert total_price == "Total: $58.29", \
        f"Ожидалась цена $58.29, но была {total_price}."