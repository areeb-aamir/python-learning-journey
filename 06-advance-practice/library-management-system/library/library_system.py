"""
Main Page Of Library Mangment System
"""
from .book import Book
from .member import Member
from .transaction import Transaction
from datetime import date


class LibrarySystem:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []


    def add_book(self, book : Book ):
        self.books.append(book)
        print(f"Book added : {book.title}")

    def add_member(self, member : Member):
        self.members.append(member)
        print(f"Member Added : {member.name}")

    def issue_book(self, book: Book, member: Member, due_date):
        if book in self.books and book.available_copies > 0:
            book_availability = True
        else:
           book_availability = False
        if len(member.borrowed_books) < member.max_limit:
            member_limit_allowence = True
        else:
            member_limit_allowence = False
        if book_availability and member_limit_allowence :
            book.available_copies -= 1
            member.borrowed_books.append(book.title)
            new_transaction = Transaction(book, member, date.today(), due_date)
            self.transactions.append(new_transaction)
            print("Transaction Done!")
        elif not book_availability:
            print("Book Is Not Available!")
        else:
            print("Error - You reached Your Max Limit.")


    def return_book(self, book : Book, member : Member):
        book.available_copies += 1
        member.borrowed_books.remove(book.title)
        for transaction in self.transactions:
            if transaction.book == book and transaction.member == member and transaction.status == "Issued":
                transaction.status = "returned"
                print("returned Sucessfull!")


    def search_book(self, title : str):
        matching_book = [book for book in self.books if title.lower()
                          in book.title.lower()]
        for book in matching_book:
            print(book)


























