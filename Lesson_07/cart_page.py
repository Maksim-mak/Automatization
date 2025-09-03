from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, '.btn_action.checkout_button')

    def get_cart_item_count(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, '.cart_item'))

    def click_checkout(self):
        checkout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        )
        checkout_btn.click()