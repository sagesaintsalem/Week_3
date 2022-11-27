from models.book import Book

book1 = Book("Uzumaki", "Junji Ito", "horror", True)
book2 = Book("Neuromancer", "William Gibson", "cyberpunk", True)
book3 = Book("Gender Games", "Juno Dawson", "LGBTQ", False)

books = [book1, book2, book3]

def add_book(book):
    books.append(book)

def find_by_title(title):
    for i in books:
        if i.title == title:
            return i

def remove_book(title):
    book_to_remove = find_by_title(title)
    books.remove(book_to_remove)

