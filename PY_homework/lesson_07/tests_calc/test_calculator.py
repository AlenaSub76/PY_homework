from pages.calculator_page import CalculatorPage


def test_calculator(driver):
    page = CalculatorPage(driver)

    page.set_delay("45")

    for value in ["7", "+", "8", "="]:
        page.click_btn(value)

    page.result_element("15", timeout=46)

    actual_text = page.get_screen_text()
    assert (actual_text == "15"), (f"Ожидался результат '15',"
                                   f"но получено '{actual_text}'")
