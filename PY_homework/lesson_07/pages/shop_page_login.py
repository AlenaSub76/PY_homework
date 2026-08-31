from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    # Локаторы
        self.username_in_locator = (By.ID, "user-name")
        self.password_in_locator = (By.ID, "password")
        self.login_btn_locator = (By.ID, "login-button")

    def login(self, username, password):
        username_in = self.wait.until(
            ec.element_to_be_clickable(self.username_in_locator))
        password_in = self.driver.find_element(*self.password_in_locator)
        login_btn = self.driver.find_element(*self.login_btn_locator)

        username_in.send_keys(username)
        password_in.send_keys(password)
        login_btn.click()
