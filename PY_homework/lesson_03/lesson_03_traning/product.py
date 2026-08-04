class Product:
    name = 'unknown'
    price = '10'

    def __init__(self, name, price):
        self.name = name
        self.price = price
# три метода

    def get_name(self):
        return self.name  # возвращает название продукта

    def get_price(self):
        return self.price  # возвращает цену продукта

    def get_product_info(self):
        return f"Продукт: {self.name}, Цена: {self.price}"
# возвращает строку, которая содержит название и цену продукта
