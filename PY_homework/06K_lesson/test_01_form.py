from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def test_form():
    driver = webdriver.Edge()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # Открываем страницу https://bonigarcia.dev/selenium-webdriver-java/data-types.html
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # ждем видимости любого поля (что DOM загружен и готов к взаимодействию)
    wait.until(ec.visibility_of_element_located((By.NAME, "first-name")))

    # Заполняем форму согласно заданию
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # Поле Zip code намеренно оставляем пустым
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Находим и нажимаем на кнопку "Submit"
    submit_btn = wait.until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3")))
    submit_btn.click()

    # Находим поле Zip code
    zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    # Получаем значение CSS-свойства
    frame_color_zc = zip_code.value_of_css_property("background-color")
    #print(frame_color_zc)
    # Проверяем, что цвет красный
    assert frame_color_zc == 'rgba(248, 215, 218, 1)', "Поле 'Zip code' красного цвета"

    # создаём список всех остальных полей с зеленым цветом
    other_fields_ids = [
    "first-name", "last-name", "address", "e-mail",
    "phone", "city", "country", "job-position", "company"
    ]

    frame_colors = {}
    for field_id in other_fields_ids:
        element = driver.find_element(By.ID, field_id)
        # Получаем значение свойства
        frame_colors[field_id] = element.value_of_css_property("background-color")
    # print(frame_colors)
    # Проверяем, что цвет зелёный у каждого элемента
    for field_id in other_fields_ids:
        color_field = frame_colors[field_id]
        assert color_field == "rgba(209, 231, 221, 1)", f"Поле '{field_id}' должно быть зелёным"

    driver.quit()
