from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Базовые локаторы
        self.inventory_container_locator = (
            By.CLASS_NAME, "inventory_container")
        self.cart_icon_locator = (By.CLASS_NAME, "shopping_cart_link")

    def add_items_to_cart(self, items):
        # Ждем загрузки страницы со списком товаров
        self.wait.until(
            ec.visibility_of_element_located(self.inventory_container_locator))

        for add_id, remove_id in items:
            # Находим кнопку "Add to cart" по динамическому ID и кликаем
            add_button = self.wait.until(ec.element_to_be_clickable((
                By.ID, f"add-to-cart-{add_id}")))
            add_button.click()
            # Ждем, пока кнопка сменится на "Remove"
            self.wait.until(ec.text_to_be_present_in_element((
                By.ID, remove_id), "Remove"))

    def go_to_cart(self):
        cart_icon = self.wait.until(
            ec.element_to_be_clickable(self.cart_icon_locator))
        cart_icon.click()
