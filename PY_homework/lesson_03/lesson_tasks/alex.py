from lesson_03.lesson_tasks.user import User
from lesson_03.lesson_tasks.card import Card

user = User("Alex")

user.sayName()
user.setAge(27)
user.sayAge()

card = Card("5467 5678 9874 6321", "03/28", "Alex F")
user.addCard(card)
user.getCard().pay(3000)
