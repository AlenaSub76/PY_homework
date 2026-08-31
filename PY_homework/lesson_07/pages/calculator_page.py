from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url):
        self.driver.get(url)

    def set_delay(self, delay_time):
        delay_input = self.wait.until(
            ec.presence_of_element_located((By.ID, "delay")))
        delay_input.clear()
        delay_input.send_keys(delay_time)

    def click_btn(self, value):
        btn = self.wait.until(ec.element_to_be_clickable((
              By.XPATH, f"//span[text()='{value}']")))
        btn.click()

    def get_screen_text(self):
        screen_text = self.driver.find_element(By.CLASS_NAME, "screen")
        return screen_text.text.strip()

    def result_element(self, result, timeout=46):
        return WebDriverWait(self.driver, timeout).until(
            ec.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), result))
