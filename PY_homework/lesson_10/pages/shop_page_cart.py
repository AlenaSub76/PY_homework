import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CartPage:
    def __init__(self, driver):
        """Конструктор класса CartPage:
           Находит и открывает корзину интернет-магазина
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Локаторы
        self.cart_item_locator = (By.CLASS_NAME, "cart_item")
        self.checkout_button_locator = (By.ID, "checkout")

    def proceed_to_checkout(self):
        """
        Ожидает загрузки страницы корзины и кликает по кнопке «Checkout».
        Шаги: 1. Ждём появления товаров в корзине (локатор: cart_item).
              2. Ждём, пока кнопка оформления станет кликабельной
                 (локатор: checkout).
              3. Нажимаем кнопку «Checkout», переходя на страницу Checkout.
        """
        self.wait.until(
            ec.visibility_of_element_located(self.cart_item_locator))
        with allure.step("Нажать на кнопку 'Checkout'"):
            checkout_btn = self.wait.until(
                ec.element_to_be_clickable(self.checkout_button_locator))
            checkout_btn.click()
