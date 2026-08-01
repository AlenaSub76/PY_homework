from smartphone import Smartphone

phone1 = Smartphone("Samsung", "Galaxy Z", "+79504562154")
phone2 = Smartphone("Apple", "iPhone 16", "+79154654218")
phone3 = Smartphone("Xiaomi", "Redmi 13C", "+79201564784")
phone4 = Smartphone("Honor", "Magic V5", "+79201568214")
phone5 = Smartphone("Huawei", "Mate X6", "+79801564624")

catalog = [phone1, phone2, phone3, phone4, phone5]

# печатаем каталог телефонов
for phone in catalog:
    print(f"{phone.phone_brand} - {phone.phone_model}. {phone.phone_number}")
