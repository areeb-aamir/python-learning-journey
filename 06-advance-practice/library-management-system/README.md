# 📚 Library Management System

A command-line library management system built with Python, demonstrating Object-Oriented Programming, file persistence, and clean software design.

## Features

- **Book Management** — Add books with title, author, ISBN, genre, and copy tracking, with duplicate ISBN prevention
- **Member Management** — Register Students and Faculty with different borrowing limits (inheritance-based), with duplicate ID prevention
- **Issue & Return** — Full transaction lifecycle with availability and limit checks
- **Search** — Case-insensitive partial title search
- **Data Persistence** — Books, members, and transactions all saved to JSON and fully restored on restart
- **Activity Logging** — Custom decorator logs every transaction

## Tech Used

- Python 3.13
- Object-Oriented Programming (Inheritance, Encapsulation)
- Decorators
- JSON for data persistence
- Modular package structure

## Project Structure

library-management-system/
library/
book.py → Book class
member.py → Member, Student, Faculty classes
transaction.py → Transaction class + logging decorator
library_system.py → Core system logic
data/
library_data.json → Persisted data
main.py → CLI entry point

## How to Run

```bash
python main.py
```

## What This Project Demonstrates

- Inheritance (Student/Faculty extending Member, with different borrow limits)
- Decorators (transaction logging)
- JSON serialization/deserialization (to_dict methods, save/load)
- Data integrity checks (duplicate ISBN/ID prevention)
- Clean separation of concerns across modules
- Error handling for missing/corrupt data files

## Possible Future Improvements

- Update/delete books and members
- View all books/members/transactions
- Overdue tracking and fines
- Search by author, ISBN, or genre

---

_Part of my [Python Learning Journey](https://github.com/areeb-aamir/python-learning-journey)_
