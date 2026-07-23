from library.library_system import LibrarySystem
from library.book import Book
from library.member import Student
from datetime import date, timedelta

# System banao
system = LibrarySystem()

# Book aur Member add karo
book1 = Book("Atomic Habits", "James Clear", "12345", "Self-help", 2018, 2)
system.add_book(book1)

student1 = Student("Areeb", 1)
system.add_member(student1)

# Book issue karo
due = date.today() + timedelta(days=14)
system.issue_book(book1, student1, due)

# Search test karo
system.search_book("atomic")

# Book return karo
system.return_book(book1, student1)
