from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # 1.Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2.Найдите и нажмите на кнопку "Start"
    start_btn = driver.find_element(By.XPATH, "//div[@id='start']/button")
    start_btn.click()

    # 3.Дождитесь появления текста "Hello World!"
    hello_element = wait.until(
        ec.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']"))
    )

    # 4.Сделайте скриншот страницы
    driver.save_screenshot("screenshots/page_screen.png")

    # 5.Проверьте, что появившийся текст равен "Hello World!"
    assert hello_element.is_displayed(), "Элемент с текстом 'Hello World!' не отображается"
    assert hello_element.text == "Hello World!", f"Текст элемента не 'Hello World!', а '{hello_element.text}'"

    driver.quit()