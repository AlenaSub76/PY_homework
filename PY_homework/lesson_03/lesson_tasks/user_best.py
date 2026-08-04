class User:
    age = 0
    name = 'No name'
    email = 'mail@test.ru'

    def __init__(self, name, age, email):
        self.age = age
        self.name = name
        self.email = email

    def sayName(self):
        print("меня зовут ", self.name)

    def sayAge(self):
        print(self.age)

    def sayEmail(self):
        print(self.email)


newUser = User('Mark', 47, 'qwertyMark@mail.com')
newUser.sayName()
newUser.sayAge()
newUser.sayEmail()
