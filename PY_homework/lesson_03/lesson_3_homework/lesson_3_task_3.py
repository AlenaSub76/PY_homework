from address import Address
from mailing import Mailing

to_address = Address("152900", "г. Рыбинск", "пр. Ленина", 1, 5)
from_address = Address("150900", "г. Москва", "пр. Мира", 3, 77)
cost = 1200
track = "9RU6154N5"

my_mailing = Mailing(to_address, from_address, cost, track)

print(f"Отправление {my_mailing.track} из {my_mailing.from_address} в "
      f"{my_mailing.to_address}. Стоимость {my_mailing.cost} рублей.")
