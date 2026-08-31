from pages.shop_page_login import LoginPage
from pages.shop_page_inventory import InventoryPage
from pages.shop_page_cart import CartPage
from pages.shop_page_checkout import CheckoutPage

# Список товаров соответствует данным из исходного автотеста
ITEMS_TO_ADD = [
    ("sauce-labs-backpack", "remove-sauce-labs-backpack"),
    ("sauce-labs-bolt-t-shirt", "remove-sauce-labs-bolt-t-shirt"),
    ("sauce-labs-onesie", "remove-sauce-labs-onesie")
]

USER_DATA = {
    "first_name": "Алена",
    "last_name": "Субботина",
    "postal_code": "152900"
}

EXPECTED_TOTAL = "58.29"


def test_sauce_demo_store_with_pom(driver):
    # Авторизация
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    # Добавление товаров и переход в корзину
    inventory_page = InventoryPage(driver)
    inventory_page.add_items_to_cart(ITEMS_TO_ADD)
    inventory_page.go_to_cart()
    # Переход к оформлению заказа
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()
    # Заполнение данных и проверка суммы
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form_and_continue(
        USER_DATA["first_name"],
        USER_DATA["last_name"],
        USER_DATA["postal_code"]
    )

    total_value = checkout_page.get_total_value()
    assert total_value == EXPECTED_TOTAL, (
        f"Ожидалась сумма ${EXPECTED_TOTAL}, "
        f"но получили ${total_value}")
