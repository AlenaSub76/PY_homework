import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    """
    фикстура для инициализации и завершения работы драйвера
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
      "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    yield driver
    driver.quit()
