from selenium import webdriver

def test_session_storage_auth():
    driver = webdriver.Chrome()

    # 1. Откройте страницу https://gitflic.ru/
    driver.get("https://gitflic.ru/")
    driver.maximize_window()

    # 2.Установите cookie пользователя 1
    driver.add_cookie({
        "name": "Alena76",
        "value": "ZDM3ZDhmYzAtZWI2MS00ZTliLTg3NjUtYWI1MmRjYWQ1YmUx",
        "domain": "gitflic.ru"
    })
    # добавляем куки для закрытия окна подтверждения работы с куки
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    # 3.Обновите страницу
    driver.refresh()

    # 4.Перейдите на страницу пользователя 1 по URL
    driver.get("https://gitflic.ru/user/alena76")

    # 5.Сохраните текущий URL
    url_first_user = driver.current_url

    # 6.Разлогиньтесь (очистите куки)
    driver.delete_all_cookies()
    driver.refresh()

    # 7.Установите cookie пользователя 2
    driver.add_cookie({
        "name": "alenenok",
        "value": "Y2ZmZDMyNGEtYjBjMi00ZjViLWEzYjctOTc5NGU0YWQzMzNj",
        "domain": "gitflic.ru"
    })

    # 8.Обновите страницу
    driver.refresh()

    # 9.Перейдите на страницу пользователя 2 по URL
    driver.get("https://gitflic.ru/user/alenenok")

    # 10.Сохраните текущий URL
    url_second_user = driver.current_url

    # 11.Проверьте, что URL для пользователя 1 и пользователя 2 различаются
    assert url_first_user != url_second_user, "URLs должны отличаться"

    driver.quit()