import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    def __init__(self, driver):
        """Конструктор класса LoginPage:
           авторизация в онлайн-магазине https://www.saucedemo.com/
           (инициализация прописана в фикстуре conftest.py)
           :param driver: WebDriver - объект драйвера Selenium
        """
        with allure.step("Дожидаться загрузки страницы с формой авторизации"):
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)
            # Локаторы
            self.username_in_locator = (By.ID, "user-name")
            self.password_in_locator = (By.ID, "password")
            self.login_btn_locator = (By.ID, "login-button")

    @allure.step("Заполнить форму авторизации и войти в систему")
    def login(self, username: str, password: str) -> None:
        """Авторизует пользователя на saucedemo.com.
           :param username: логин пользователя
           :param password: пароль пользователя
        """
        with allure.step(f"Ввести логин '{username}'"):
            username_in = self.wait.until(
                ec.element_to_be_clickable(self.username_in_locator))
            username_in.send_keys(username)
        with allure.step(f"Ввести пароль '{password}'"):
            password_in = self.driver.find_element(*self.password_in_locator)
            password_in.send_keys(password)
        with allure.step("Нажать кнопку 'Login'"):
            login_btn = self.driver.find_element(*self.login_btn_locator)
            login_btn.click()
