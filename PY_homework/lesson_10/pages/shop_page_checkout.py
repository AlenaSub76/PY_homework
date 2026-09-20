import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@allure.step("Оформить заказ")
class CheckoutPage:
    def __init__(self, driver):
        """Конструктор класса CheckoutPage:
           Оформление заказа из корзины
           :param driver: WebDriver - объект драйвера Selenium
        """
        with allure.step("Открыть страницу с данными пользователя"):
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)
            # Локаторы формы
            self.first_name_locator = (By.ID, "first-name")
            self.last_name_locator = (By.ID, "last-name")
            self.postal_code_locator = (By.ID, "postal-code")
            self.continue_button_locator = (By.ID, "continue")
            # Локатор итоговой стоимости
            self.total_label_locator = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить личные данные")
    def fill_form_and_continue(self,
                               first_name: str,
                               last_name: str,
                               postal_code: str) -> None:
        """Заполняет форму на странице Checkout
           и переходит к следующему шагу.
           first_name (str): имя покупателя.
           last_name (str): фамилия покупателя.
           postal_code (str): почтовый индекс покупателя.
        """
        # Ждем пока загрузится форма
        self.wait.until(ec.presence_of_element_located(
            self.first_name_locator))
        with allure.step(f"Ввести имя покупателя: {first_name}"):
            element = self.driver.find_element(*self.first_name_locator)
            element.clear()
            element.send_keys(first_name)
        with allure.step(f"Ввести фамилию покупателя: {last_name}"):
            element = self.driver.find_element(*self.last_name_locator)
            element.clear()
            element.send_keys(last_name)
        with allure.step(f"Ввести почтовый индекс покупателя: {postal_code}"):
            element = self.driver.find_element(*self.postal_code_locator)
            element.clear()
            element.send_keys(postal_code)
        with allure.step("Нажать кнопку 'Continue'"):
            continue_btn = self.wait.until(
                ec.element_to_be_clickable(self.continue_button_locator))
            continue_btn.click()

    def get_total_value(self) -> str:
        """Возвращает итоговую стоимость заказа без префикса «Total: $».
        Returns: str: числовое значение итоговой стоимости (например, "58.29").
        """
        # Ждем загрузки итоговой страницы с итоговой стоимостью Total
        total_element = self.wait.until(
            ec.visibility_of_element_located(self.total_label_locator))
        with allure.step("Прочитать текст итоговой стоимости корзины"):
            total_text: str = total_element.text
        return total_text.replace("Total: $", "").strip()
