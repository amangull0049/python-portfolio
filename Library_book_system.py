class Book:
    def __init__(self, title, author,):
        self.title = title
        self.author = author
        self.available = True
    
    
    def display_info(self,):
        print("Book Title: ", self.title, "Author: ", self.author)
        
        
        
class Library:
    def __init__(self, books):
        self.books = []
        
        
    def add_book(self, book):
        self.books.append(book)
        
    def view_books(self,):
        for book in self.books:
            status = "Availble" if self.available else "Not Available"
            
        print("Title: ", book.title, " - ", status)
        
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Book borrowd.")
                return
        print("Book not available")
        
    def return_book(self, title):
        for  book in self.books:
            if book.title == title:
                book.available = True
                print("Book returned.")
                return


book1 = Book("python basics", "John Doe")
book2 = Book("Machine Learning", "Jane Smith")

lib = Library()

lib.add_book(book1)
lib.add_book(book2)

lib.view_books()

lib.borrow_book("Python basics")

lib.view_books()