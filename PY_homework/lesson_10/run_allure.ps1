param(
    # По умолчанию — обе папки с тестами
    [string[]]$TestPath = @("tests_calc", "tests_shop")
)
# Папка для сырых результатов тестов (JSON, XML файлы от pytest + allure)
$results = ".\allure-results"
# Папка с историей предыдущих отчетов Allure (для графиков трендов)
$rep_history = ".\final-report\history"
# Папка для финального HTML отчета Allure
$report = ".\final-report"
# Удаляем папку с предыдущими результатами тестов
# -Recurse удаляет содержимое, -Force игнорирует ошибки прав, -ErrorAction SilentlyContinue подавляет вывод ошибок
Remove-Item -Path $results -Recurse -Force -ErrorAction SilentlyContinue
# Запускаем тесты и сохраняем результаты в папку $results
# --alluredir указывает куда сохранять сырые данные для Allure
pytest $TestPath --alluredir=$results

# Переносим историю из старого отчета в новые результаты
# Это нужно для построения графиков трендов в Allure
# -ErrorAction SilentlyContinue означает: "если команда завершится ошибкой, продолжаем выполнение"
# Ошибка будет если папки $rep_history не существует (первый запуск)
Move-Item -Path $rep_history -Destination $results -Force -ErrorAction SilentlyContinue
# Удаляем предыдущий сгенерированный HTML отчет
Remove-Item -Path $report -Recurse -Force -ErrorAction SilentlyContinue
# Преобразуем сырые данные в красивый HTML отчет
# -o указывает выходную папку для отчета
allure generate $results -o $report
# Автоматически открываем сгенерированный отчет в браузере по умолчанию
allure open $report
