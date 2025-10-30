class Library:
  def __init__(self, name, address):
    self.name = name
    self.address = address
    self.books = []
    
  def add_book(self, book):
    self.books.append(book)
    print(f"Book '{book}' added to the library '{self.name}'.")

  def remove_book(self, book):
    if book in self.books:
      self.books.remove(book)
      print(f"Book '{book}' removed from the library '{self.name}'.")
      
  def list_books(self):
    for book in self.books:
      print(f"- {book.title} by {book.author} (ISBN: {book.isbn}), is {'available' if book.is_available else 'not available'}.\n")
      
  def borrow_book(self, book, user):
    if book in self.books and book.is_available:
      book.is_available = False
      book.responsible_user = user
      print(f"User '{user.name}' borrowed the book '{book.title}'.")
    else:
      print(f"Book '{book.title}' is not available for borrowing.")


class Book:
  def __init__(self, title, author, isbn, published_year, number_of_pages, is_available=True, responsible_user=None):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.published_year = published_year
    self.number_of_pages = number_of_pages
    self.is_available = is_available
    self.responsible_user = responsible_user
  
  def __str__(self):
    return f"{self.title} by {self.author} (ISBN: {self.isbn}), is {'available' if self.is_available else 'not available'} and responsible user is {self.responsible_user.name if self.responsible_user else 'not assigned'}."

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    
library = Library("Central Library", "123 Main St") 

book1 = Book("1984", "George Orwell", "1234567890", 1949, 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321", 1960, 281)

library.add_book(book1)
library.add_book(book2)
library.list_books()

user = User("Alice", "alice@example.com")
library.borrow_book(book1, user)
library.list_books()

print(book1)