def is_year_leap(year):
    return True if year % 4 == 0 else False


leap = int(input("Введите год: "))
result = is_year_leap(leap)
print(f"Год {leap}: {result}")
