import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    """
    фикстура для инициализации и завершения работы драйвера
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()
