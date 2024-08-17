class Book:
    
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = 200
    
    # Methods
    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print("You just borrowed a book!")
        else:
            print("There are not enough available copies.")
    
    def return_book(self):
        self.available_copies += 1
    
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available Copies: {self.available_copies}")
    
class Member:
    
    def __init__(self, name, member_id, borrowed_books):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    # Methods
    def borrow_book(self, book):
        if self.available_copies > 0:
            self.borrowed_books.append(book)
            book.borrow()
        else:
            print("There are not enough available copies.")
    
    def return_book(self, book):
        self.borrowed_books.remove(book)
        book.return_book()
    
    def display_borrowed_books(self):
        for book in self.borrowed_books:
            print(f"Title: {book.title}, Author: {book.author}")

class Library:
    
    def __init__(self, books, members):
        self.books = []
        self.members = []
    
    # Methods
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        if self.available_copies == 200:
             self.books.remove(book)
             print(f"Book '{book.title}' by {book.author} removed from the library")
        else:
            print(f"Cannot remove '{book.title}'. Some copies are still borrowed.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered in the library.")
    
    def deregister_member(self, member):
        if len(member.borrowed_books) == 0:
            self.members.remove(member)
            print(f"Member '{member.name} deregistered from the library.'")
        else:
            print(f"Cannot deregister '{member.name}'. They still have borrowed books.")
    
    def list_available_books(self):
        for book in self.books:
            if book.available_copies > 0:
                print(f"Title: {book.title}, Author: {book.author}, Copies: {book.available_copies}")
    
    def list_members(self):
        print("Registered members in the library:")
        for member in self.members:
            print(f"Name: {member.name}, ID: {member.member_id}")