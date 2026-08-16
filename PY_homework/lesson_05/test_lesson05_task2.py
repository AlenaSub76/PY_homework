from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    in_url = driver.current_url  # запонминаем текущий URL
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Алена Субботина")

    # Найдите кнопку отправки и кликните на нее
    submit_btn = driver.find_element(By.XPATH,
                                     "//button[text()='Submit order']")
    submit_btn.click()
    # получаем новый URL
    new_url = driver.current_url
    # Проверяем, что после нажатия URL изменился
    assert new_url != in_url

    driver.quit()
