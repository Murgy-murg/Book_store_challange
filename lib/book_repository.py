from lib.book import Book
class BookRepository:

    def __init__(self, connection):
        self._connection = connection
    #select all records
    #No arguments
    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row["title"], row["author_name"],)
            books.append(item)
        return books

        # Executes the SQL query:
        # SELECT title, author_name, FROM books;

        # Returns an array of Student objects.

