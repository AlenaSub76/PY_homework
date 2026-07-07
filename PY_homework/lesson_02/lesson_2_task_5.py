def month_to_season(month):
    if 1 <= month <= 2 or month == 12:
        return "Зима"
    if 3 <= month <= 5:
        return "Весна"
    if 6 <= month <= 8:
        return "Лето"
    if 9 <= month <= 11:
        return "Осень"
    return "Неверный номер месяца"


month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month))

# или ещё вариант:
month_to_season = int(input("Введите номер месяца (1-12): "))
month = (month_to_season)
season = ' '
if 1 <= month <= 2 or month == 12:
    season = "Зима"
if 3 <= month <= 5:
    season = "Весна"
if 6 <= month <= 8:
    season = "Лето"
if 9 <= month <= 11:
    season = "Осень"
print(season)
