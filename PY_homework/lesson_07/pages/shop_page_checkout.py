from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Локаторы формы
        self.first_name_locator = (By.ID, "first-name")
        self.last_name_locator = (By.ID, "last-name")
        self.postal_code_locator = (By.ID, "postal-code")
        self.continue_button_locator = (By.ID, "continue")
        # Локатор итоговой стоимости
        self.total_label_locator = (By.CLASS_NAME, "summary_total_label")

    def fill_form_and_continue(self, first_name, last_name, postal_code):
        # Ждем пока загрузится форма
        self.wait.until(ec.presence_of_element_located(
            self.first_name_locator))
        self.driver.find_element(
            *self.first_name_locator).send_keys(first_name)
        self.driver.find_element(
            *self.last_name_locator).send_keys(last_name)
        self.driver.find_element(
            *self.postal_code_locator).send_keys(postal_code)
        continue_btn = self.driver.find_element(*self.continue_button_locator)
        continue_btn.click()

    def get_total_value(self):
        # Ждем загрузки итоговой страницы с итоговой стоимостью Total
        total_element = self.wait.until(
            ec.visibility_of_element_located(self.total_label_locator))
        # Прочитать итоговую стоимость
        total_text = total_element.text
        return total_text.replace("Total: $", "")
