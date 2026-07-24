from library.library_system import LibrarySystem
from library.book import Book
from library.member import Student, Faculty
from datetime import date, timedelta


def main():
    system = LibrarySystem()
    system.load_data("data/library_data.json")

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Exit")

        try:
            option = int(input("Choose Option: "))
        except ValueError:
            print("Enter a valid number!")
            continue

        if option == 1:
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            genre = input("Genre: ")
            year = int(input("Publication Year: "))
            copies = int(input("Total Copies: "))
            new_book = Book(title, author, isbn, genre, year, copies)
            system.add_book(new_book)

        elif option == 2:
            name = input("Name: ")
            id = int(input("Your ID: "))
            member_type = input("Type (student/faculty): ")
            if member_type.lower() == "student":
                new_member = Student(name, id)
            else:
                new_member = Faculty(name, id)
            system.add_member(new_member)

        elif option == 3:
            book_name = input("Book Name: ")
            name = input("Member Name: ")
            due = date.today() + timedelta(days=14)
            complete_book = system.find_book(book_name)
            complete_member = system.find_member(name)
            if complete_book and complete_member:
                system.issue_book(complete_book, complete_member, due)
            else:
                print("Book or Member not found!")

        elif option == 4:
            book_name = input("Book Name: ")
            name = input("Member Name: ")
            complete_book = system.find_book(book_name)
            complete_member = system.find_member(name)
            if complete_book and complete_member:
                system.return_book(complete_book, complete_member)
            else:
                print("Book or Member not found!")

        elif option == 5:
            title = input("Search: ")
            system.search_book(title)

        elif option == 6:
            system.save_data("data/library_data.json")
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
