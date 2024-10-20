class Book:
    def __init__(self, title, author, year, read=False):
        self.title = title
        self.author = author
        self.year = year
        self.read = read

    def mark_as_read(self):
        self.read = True

    def mark_as_unread(self):
        self.read = False

    def __str__(self):
        status = "Прочитана" if self.read else "Непрочитана"
        return f"{self.title} by {self.author} ({self.year}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

    def find_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books

    def find_by_author(self, author):
        found_books = [book for book in self.books if author.lower() in book.author.lower()]
        return found_books

    def mark_book_as_read(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.mark_as_read()
                print(f"Книга '{title}' отмечена как прочитанная.")
                return
        print(f"Книга '{title}' не найдена.")

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title.lower() != title.lower()]
        print(f"Книга '{title}' удалена.")

    def filter_books(self, read_status):
        return [book for book in self.books if book.read == read_status]

    def sort_books_by_year(self):
        self.books.sort(key=lambda book: book.year)


def main():
    library = Library()

    while True:
        print("\nКомандное меню:")
        print("1. Добавить книгу")
        print("2. Просмотреть книги")
        print("3. Найти книгу по названию")
        print("4. Найти книги по автору")
        print("5. Отметить книгу как прочитанную")
        print("6. Удалить книгу")
        print("7. Просмотреть прочитанные книги")
        print("8. Просмотреть непрочитанные книги")
        print("9. Сортировать книги по году публикации")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год публикации: ")
            library.add_book(Book(title, author, year))
            print(f"Книга '{title}' добавлена в библиотеку.")

        elif choice == '2':
            print("\nСписок книг в библиотеке:")
            library.list_books()

        elif choice == '3':
            title = input("Введите название книги для поиска: ")
            found_books = library.find_by_title(title)
            print("\nНайденные книги:")
            for book in found_books:
                print(book)

        elif choice == '4':
            author = input("Введите автора для поиска: ")
            found_books = library.find_by_author(author)
            print("\nНайденные книги:")
            for book in found_books:
                print(book)

        elif choice == '5':
            title = input("Введите название книги, которую хотите отметить как прочитанную: ")
            library.mark_book_as_read(title)

        elif choice == '6':
            title = input("Введите название книги для удаления: ")
            library.remove_book(title)

        elif choice == '7':
            print("\nПрочитанные книги:")
            read_books = library.filter_books(read_status=True)
            for book in read_books:
                print(book)

        elif choice == '8':
            print("\nНепрочитанные книги:")
            unread_books = library.filter_books(read_status=False)
            for book in unread_books:
                print(book)

        elif choice == '9':
            library.sort_books_by_year()
            print("Книги отсортированы по году публикации.")

        elif choice == '0':
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    main()
