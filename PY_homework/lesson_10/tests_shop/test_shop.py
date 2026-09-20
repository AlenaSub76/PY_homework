import allure
from pages.shop_page_login import LoginPage
from pages.shop_page_inventory import InventoryPage
from pages.shop_page_cart import CartPage
from pages.shop_page_checkout import CheckoutPage

# Список товаров соответствует данным из исходного автотеста
ITEMS_TO_ADD: list[tuple[str, str]] = [
    ("sauce-labs-backpack", "remove-sauce-labs-backpack"),
    ("sauce-labs-bolt-t-shirt", "remove-sauce-labs-bolt-t-shirt"),
    ("sauce-labs-onesie", "remove-sauce-labs-onesie")
]

USER_DATA: dict[str, str] = {
    "first_name": "Алена",
    "last_name": "Субботина",
    "postal_code": "152900"
}

EXPECTED_TOTAL: str = "58.29"


@allure.parent_suite("Оформление покупки в интернет-магазине")
@allure.suite("Интернет-магазин")
@allure.sub_suite("Тестирование функциональности интернет-магазина")
@allure.description("""Тест проверяет выполнение следующих действий:
                        - авторизация в интернет-магазине,
                        - добавление товаров в корзину,
                        - оформление заказа,
                        - проверка итоговой суммы заказа""")
@allure.severity(allure.severity_level.CRITICAL)
class TestOnlineStore:
    @allure.title("Тестирование основных действий покупки товаров")
    @allure.feature("Онлайн покупки")
    def test_sauce_demo_store_with_pom(self, driver):
        with allure.step("Открыть интернет-магазин"):
            login_page = LoginPage(driver)
        with allure.step("Авторизоваться в системе"):
            login_page.login("standard_user", "secret_sauce")
        with allure.step("Добавить товары в корзину"):
            # Добавление товаров и переход в корзину
            inventory_page = InventoryPage(driver)
            inventory_page.add_items_to_cart(ITEMS_TO_ADD)
            inventory_page.go_to_cart()
        with allure.step("Перейти на страницу оформления заказа"):
            cart_page = CartPage(driver)
            cart_page.proceed_to_checkout()
        with allure.step("Заполнить личные данные покупателя"):
            checkout_page = CheckoutPage(driver)
            with allure.step("Заполнить форму"):
                checkout_page.fill_form_and_continue(
                    USER_DATA["first_name"],
                    USER_DATA["last_name"],
                    USER_DATA["postal_code"]
                )
        with allure.step("Проверить итоговую сумму заказа"):
            total_value = checkout_page.get_total_value()
            assert total_value == EXPECTED_TOTAL, (
                f"Ожидалась сумма ${EXPECTED_TOTAL}, "
                f"но получили ${total_value}")
