class Library:

    def __init__(self, name):
        self.name = name
        self.books = []

    # В класа, който описва библиотека, добавете методи за добавяне на книга
    # към библиотеката, търсене на книга по предварително зададен автор, извеждане на
    # информация за дадена книга и изтриване на книга от библиотеката

    def add_book(self, book):
        self.books.append(book)

    def delete_books_by_author(self, author):
        self.books = [book for book in self.books if book.author != author]

    def search_book_by_author(self, author):
        for book in self.books:
            if book.author == author:
                return book

    def print_all_books_info(self):
        for book in self.books:
            self.print_book_info(book)

    def print_book_info(self, book):
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Publisher: {book.publisher}")
        print(f"Year: {book.year}")
        print(f"Pages: {book.pages}")
        print(f"ISBN: {book.isbn}")


class Books:

    def __init__(self, title, author, publisher, year, pages, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.isbn = isbn


class TestLibray:

    library_sofia = None

    @staticmethod
    def create_library():
        TestLibray.library_sofia = Library('Community Library Sofia')

    @staticmethod
    def run_tests():
        TestLibray.library_sofia.add_book(Books('Python', 'Vasil', 'Siela', 2020, 1000, 111111111))
        TestLibray.library_sofia.add_book(Books('C#', 'Nasko', 'Asenevci', 2021, 1100, 222222222))
        TestLibray.library_sofia.add_book(Books('Java', 'Pasko', 'Fiut', 2022, 1200, 333333333))

        # assert len(library_sofia.books) == 3, 'Expected 3 books!'

        # Add a book by Stephen King for testing
        TestLibray.library_sofia.add_book(Books('The Shining', 'Stephen King', 'Doubleday', 1977, 447, 9780385121675))

    @staticmethod
    def print_info():
        # Delete all books by Stephen King
        TestLibray.library_sofia.delete_books_by_author('Stephen King')

        # Print information for all remaining books
        TestLibray.library_sofia.print_all_books_info()


TestLibray.create_library()
TestLibray.run_tests()
TestLibray.print_info()
