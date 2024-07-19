import json
import os
import uuid

booksdb = 'books.json'


class Book:
    def __init__(self, title, author, year, status="в наличии"):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.status = status


if not os.path.exists(booksdb):
    with open(booksdb, 'w') as f:
        json.dump([], f)


def load_books():
    with open(booksdb, 'r') as f:
        return json.load(f)


def save_books(books):
    with open(booksdb, 'w') as f:
        json.dump(books, f, indent=4)


def get_next_id(books):
    if not books:
        return 1
    return max(int(book['id']) for book in books) + 1


def add_book(title, author, year):
    books = load_books()
    new_book = Book(title, author, year)
    new_book.id = get_next_id(books)
    books.append(new_book.__dict__)
    save_books(books)
    print(f"Книга '{title}' добавлена в библиотеку с ID {new_book.id}.")


def remove_book(book_id):
    books = load_books()
    books = [book for book in books if book['id'] != book_id]
    save_books(books)
    print(f"Книга с ID '{book_id}' удалена из библиотеки.")


def search_books(keyword):
    books = load_books()
    results = [book for book in books if
               keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower()
               or keyword.lower() in book['year'].lower()]
    if results:
        for book in results:
            print(
                f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, "
                f"Год: {book['year']}, Статус: {book['status']}")
    else:
        print("По вашему запросу ничего не найдено.")


def display_books():
    books = load_books()
    if books:
        for book in books:
            print(
                f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, "
                f"Год: {book['year']}, Статус: {book['status']}")
    else:
        print("Библиотека пуста.")


def change_status(book_id, new_status):
    books = load_books()
    for book in books:
        if book['id'] == str(book_id):
            book['status'] = new_status
            save_books(books)
            print(f"Статус книги с ID '{book_id}' изменен на '{new_status}'.")
            return
    print(f"Книга с ID '{book_id}' не найдена.")


def main():
    while True:
        print("\nУправление библиотекой")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книги")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            add_book(title, author, year)
        elif choice == '2':
            book_id = input("Введите ID книги для удаления: ")
            remove_book(book_id)
        elif choice == '3':
            keyword = input("Введите ключевое слово для поиска: ")
            search_books(keyword)
        elif choice == '4':
            display_books()
        elif choice == '5':
            book_id = input("Введите ID книги для изменения статуса: ")
            new_status = input("Введите новый статус книги: ")
            change_status(book_id, new_status)
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == '__main__':
    main()
