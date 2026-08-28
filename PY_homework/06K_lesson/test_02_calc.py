from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # Открываем страницу
    # https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Ввод значения задержки (45 с) в поле по локатору #delay
    delay_input = wait.until(ec.presence_of_element_located((By.ID, "delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажатие на кнопки калькулятора
    for value in ["7", "+", "8", "="]:
        btn = wait.until(ec.element_to_be_clickable((
              By.XPATH, f"//span[text()='{value}']")))
        btn.click()

    # Проверка результата через 45 секунд
    result_element = WebDriverWait(driver, 46).until(
        ec.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    screen_text = driver.find_element(By.CLASS_NAME, "screen")
    actual_text = screen_text.text.strip()
    # print(f"Полученный результат: '{actual_text}'")
    assert (
        actual_text == "15"
    ), f"Ожидался результат '15', но получено '{actual_text}'"

    driver.quit()
