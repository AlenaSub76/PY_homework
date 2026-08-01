class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name  # имя
        self.last_name = last_name    # фамилия

# три метода для печати данных
    def sayFname(self):
        print(f"Имя: {self.first_name}")
# print("Имя: ", self.first_name)

    def sayLname(self):
        print(f"Фамилия: {self.last_name}")
# print("Фамилия: ", self.last_name)

    def sayName(self):
        print(f"Имя, фамилия: {self.first_name} {self.last_name}")
# print("Имя, Фамилия: ", self.first_name, self.last_name)
