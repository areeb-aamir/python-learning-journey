"""
Main Page Of Library Management System
"""
import json
from .book import Book
from .member import Member
from .transaction import Transaction
from datetime import date
from .member import Student, Faculty


class LibrarySystem:
    """Manages books, members, and transactions for the library."""
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []


    def add_book(self, book: Book):
        for existing_book in self.books:
            if existing_book.isbn == book.isbn:
                print("Error: A book with this ISBN already exists!")
                return
        self.books.append(book)
        print(f"Book added : {book.title}")

    def add_member(self, member: Member):
            for existing_member in self.members:
                if existing_member.id == member.id:
                    print("Error: A member with this ID already exists!")
                    return
            self.members.append(member)
            print(f"Member Added : {member.name}")

    def issue_book(self, book: Book, member: Member, due_date):
        if book in self.books and book.available_copies > 0:
            book_availability = True
        else:
           book_availability = False
        if len(member.borrowed_books) < member.max_limit:
            member_limit_allowance = True
        else:
            member_limit_allowance = False
        if book_availability and member_limit_allowance :
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

    def save_data(self, filepath: str):
        """Save Data In JSON File In Dict Form."""
        data = {
            "books": [book.to_dict() for book in self.books],
            "members": [member.to_dict() for member in self.members],
            "transactions" : [transaction.to_dict() for transaction in self.transactions]
        }
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self, filepath: str):
        """Load books, members, and transactions from a JSON file."""
        try:
            with open(filepath, "r") as f:
                data = json.load(f)

            for book_dict in data["books"]:
                new_book = Book(
                    book_dict["title"],
                    book_dict["author"],
                    book_dict["isbn"],
                    book_dict["genre"],
                    book_dict["publication_year"],
                    book_dict["total_copies"]
                )
                new_book.available_copies = book_dict["available_copies"]
                self.books.append(new_book)
            for member_dict in data["members"]:
                if member_dict["max_limit"] == 3:
                    new_member = Student(member_dict["name"], member_dict["id"])
                else:
                    new_member = Faculty(member_dict["name"], member_dict["id"])
                new_member.borrowed_books = member_dict["borrowed_books"]
                self.members.append(new_member)
            for txn_dict in data["transactions"]:
                found_book = self.find_book(txn_dict["book_title"])
                found_member = self.find_member(txn_dict["member_name"])
                if found_book and found_member:
                    new_txn = Transaction(found_book, found_member,
                                            txn_dict["issue_date"], txn_dict["due_date"],
                                            txn_dict["status"])
                    self.transactions.append(new_txn)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Starting New library system.")

    def find_book(self, title: str):
        """Find a book by exact title match."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_member(self, name: str):
        """Find a member by exact name match."""
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        return None
