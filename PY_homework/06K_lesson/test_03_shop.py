from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_sauce_demo_store():
    driver = webdriver.Firefox()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # Открыть сайт магазина в Firefox
    driver.get("https://www.saucedemo.com/")

    # ждём появления полей
    username_in = wait.until(ec.element_to_be_clickable((By.ID, "user-name")))
    password_in = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")
    # Авторизация как standard_user
    username_in.send_keys("standard_user")
    password_in.send_keys("secret_sauce")
    login_btn.click()

    # Ждем загрузки страницы со списком товаров
    wait.until(ec.visibility_of_element_located((
        By.CLASS_NAME, "inventory_container")))
    # Добавить товары в корзину
    items = [("sauce-labs-backpack", "remove-sauce-labs-backpack"),
             ("sauce-labs-bolt-t-shirt", "remove-sauce-labs-bolt-t-shirt"),
             ("sauce-labs-onesie", "remove-sauce-labs-onesie")]
    for add_id, remove_id in items:
        #  Находим кнопку "Add to cart" по динамическому ID и кликаем
        add_button = wait.until(ec.element_to_be_clickable((
            By.ID, f"add-to-cart-{add_id}")))
        add_button.click()
        # Ждем, пока кнопка сменится на "Remove"
        wait.until(ec.text_to_be_present_in_element((
            By.ID, remove_id), "Remove"))

    # Шаг 4: Перейти в корзину
    cart_icon = wait.until(ec.element_to_be_clickable((
        By.CLASS_NAME, "shopping_cart_link")))
    cart_icon.click()

    # Ждем пока загрузится страница корзины
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "cart_item")))

    # Нажимаем Checkout
    checkout_btn = wait.until(ec.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()

    # Заполнияем форму данными
    # Ждем пока загрузится форма
    wait.until(ec.presence_of_element_located((By.ID, "first-name")))

    driver.find_element(By.ID, "first-name").send_keys("Алена")
    driver.find_element(By.ID, "last-name").send_keys("Субботина")
    driver.find_element(By.ID, "postal-code").send_keys("152900")
    continue_btn = driver.find_element(By.ID, "continue")
    continue_btn.click()

    # Ждем загрузки итоговой страницы с итоговой стоимостью Total
    total_element = wait.until(ec.visibility_of_element_located((
        By.CLASS_NAME, "summary_total_label")))
    # Прочитать итоговую стоимость
    total_text = total_element.text
    total_value = total_text.replace("Total: $", "")

    # print(f"Итоговая стоимость: {total_text}")

    # Проверить, что сумма равна $58.29
    expected_total = "58.29"
    assert total_value == expected_total, (
        f"Ожидалась сумма ${expected_total}, "
        f"но получили ${total_value}"
    )

    driver.quit()
