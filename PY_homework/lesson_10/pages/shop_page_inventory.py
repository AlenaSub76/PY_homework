import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@allure.step("Выбрать товары")
class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Базовые локаторы
        self.inventory_container_locator = (
            By.CLASS_NAME, "inventory_container")
        self.cart_icon_locator = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавить товары в корзину")
    def add_items_to_cart(self, items: list[tuple[str, str]]) -> None:
        """Ожидает загрузки страницы со списком товаров,
            добавляет указанные по ID-локатору товары и
            проверяет смену кнопки на «Remove».
            items (list[tuple[str, str]]): список пар вида (add_id, remove_id)
        """
        self.wait.until(
            ec.visibility_of_element_located(self.inventory_container_locator))

        for add_id, remove_id in items:
            with allure.step(f"Добавить выбранный товар в корзину "
                             f"по кнопке {add_id}"):
                # Находим кнопку "Add to cart" по динамическому ID и кликаем
                add_button = self.wait.until(ec.element_to_be_clickable((
                    By.ID, f"add-to-cart-{add_id}")))
                add_button.click()
            with allure.step("Дождаться, пока кнопка 'Add to cart' сменится "
                             "на 'Remove'"):
                self.wait.until(ec.text_to_be_present_in_element((
                    By.ID, remove_id), "Remove"))

    @allure.step("Перейти к корзине покупок")
    def go_to_cart(self):
        """Ожидает кликабельность иконки корзины и переходит в неё."""
        with allure.step("Нажать на значок корзины"):
            cart_icon = self.wait.until(
                ec.element_to_be_clickable(self.cart_icon_locator))
            cart_icon.click()
