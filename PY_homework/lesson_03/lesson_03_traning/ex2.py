from book import Book

book1 = Book("Овод", "Э.Л. Войнич")
book2 = Book("Алиса в стране чудес", "Льюис Кэрролл")
book3 = Book("Золотой ключик", "А.Н. Толстой")

library = [book1, book2, book3]  # создали список книг

# печатаем список книг
for book in library:
    print(f"{book.title} - {book.author}")
