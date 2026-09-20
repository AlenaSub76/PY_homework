import allure
from pages.calculator_page import CalculatorPage


@allure.parent_suite("Выполнение простых арифметических операций")
@allure.suite("Калькулятор")
@allure.sub_suite("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работы калькулятора "
                    "с возможностю установления времени задержки для "
                    "вывода результата операции")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    @allure.title("Тестирование операции СЛОЖЕНИЕ чисел")
    @allure.feature("Калькулятор")
    def test_calculator(self, driver):
        with allure.step("Открыть страницу с калькулятором"):
            page = CalculatorPage(driver)
        with allure.step("Установить время задержки в секундах"):
            page.set_delay("5")
        with allure.step("Нажать кнопки выполнения арифметического действия"):
            for value in ["7", "+", "8", "="]:
                page.click_btn(value)
        with allure.step("Ожидание результата выполнения"):
            page.result_element("15", timeout=6)
        with allure.step("Проверить результат"):
            with allure.step("Найти текст с результатом вычисления"):
                actual_text = page.get_screen_text()
            with allure.step("Выполнить сравнение"):
                assert (actual_text == "15"), (f"Ожидался результат '15',"
                                               f"но получено '{actual_text}'")
