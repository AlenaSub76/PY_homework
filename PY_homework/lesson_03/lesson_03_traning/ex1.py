from lesson_03.lesson_03_traning.product import Product

# создаем экземпляр класса Product
my_product = Product("Авокадо", 150)

# Вызываем методы и выводим строку с информацией о продукте
print(my_product.get_name())  # ОР: "Авокадо"
print(my_product.get_price())  # ОР: 150
print(my_product.get_product_info())  # ОР: Продукт Авокадоб цена 150
