from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/")

    # Найдите ссылку HTML Form и кликните на нее
    link_form = driver.find_element(By.LINK_TEXT, "HTML Form")
    link_form.click()
    # Проверяем, что URL изменился на /forms/post
    assert driver.current_url == ("https://httpbin.qa-territory.online/"
                                  "forms/post")

    # Возвращаемся назад на главную страницу
    driver.back()
    # Проверяем, что вернулись на исходный URL
    assert driver.current_url == 'https://httpbin.qa-territory.online/'

    driver.quit()
