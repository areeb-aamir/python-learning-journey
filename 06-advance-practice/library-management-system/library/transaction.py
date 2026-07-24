"""
Transaction module - represents a book issue/return record.
"""
from datetime import date
from .book import Book
from .member import Member


def log_transaction(func):
    def wrapper(*args, **kwargs):
        print("Transaction Starts")
        result = func(*args, **kwargs)
        print("Transaction End!")
        return result
    return wrapper

class Transaction:
    """represents Transaction record of Library."""
    @log_transaction
    def __init__(self, book: Book, member: Member, issue_date: date,
                 due_date: date, status: str = "Issued"):
        self.book = book
        self.member = member
        self.issue_date = issue_date
        self.due_date = due_date
        self.status = status


    def __str__(self) -> str:
        """Return a user-friendly string representation."""
        return f"""
        Book Name : {self.book.title}
        Member : {self.member.name}
        Issue Date : {self.issue_date}
        Due Date : {self.due_date}
        Status : {self.status}
        """

    def to_dict(self) -> dict:
        """Convert transaction to a dictionary for JSON storage."""
        return {
            "book_title": self.book.title,
            "member_name": self.member.name,
            "issue_date": str(self.issue_date),
            "due_date": str(self.due_date),
            "status": self.status
        }
