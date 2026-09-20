import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CalculatorPage:
    def __init__(self, driver):
        """
        Конструктор класса CalculatorPage.
        :param driver: WebDriver - объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Открытие страницы с калькулятором")
    def open(self, url):
        """Открывает страницу калькулятора"""
        self.driver.get(url)

    @allure.step("Установка задержки {delay_time} секунд")
    def set_delay(self, delay_time):
        """Устанавливает задержку по времени (в секундах)
           для выполнения операции на калькуляторе.
           :param delay_time: int - время задержки в секундах
        """
        delay_input = self.wait.until(
            ec.presence_of_element_located((By.ID, "delay")))
        with allure.step("Очищение поля ввода задержки от случайного текста"):
            delay_input.clear()
        with allure.step("Ввод значения времени задержки в элемент"):
            delay_input.send_keys(delay_time)

    @allure.step("Нажатие кнопок {value} калькулятора")
    def click_btn(self, value):
        """:param btn: str - текст на кнопке, которую надо нажать"""
        btn = self.wait.until(ec.element_to_be_clickable((
              By.XPATH, f"//span[text()='{value}']")))
        btn.click()

    @allure.step("Извлечение текста с элемента")
    def get_screen_text(self):
        screen_text = self.driver.find_element(By.CLASS_NAME, "screen")
        return screen_text.text.strip()

    @allure.step("Ожидание результата {result} с задержкой {timeout}")
    def result_element(self, result, timeout=46):
        """Ожидает появление результата на экране калькулятора
           c установленной задержкой {delay} + 1 сек для надежности
           timeout: int - время задержки в секундах"""
        return WebDriverWait(self.driver, timeout).until(
            ec.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), result))
