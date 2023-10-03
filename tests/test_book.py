from lib.book import Book

#Book contructs with a title and author name

def test_book_constructs():
    book = Book('test title', 'test author')
    assert book.title == 'test title'
    assert book.author_name == 'test author'

#We can format books to nice strings

def test_books_format_nicely():
    book = Book('test title', 'test author')
    assert str(book) == 'Book(test title, test author)'

#we can check that two identical books are equal

def test_books_are_equal():
    book1 = Book('test title', 'test author')
    book2 = Book('test title', 'test author')
    assert book1 == book2