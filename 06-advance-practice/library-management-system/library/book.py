"""
Book Module - represents a book in a library system.
"""



class Book:
    """Represents a single book with copy tracking."""
    def __init__(self, title: str, author: str, isbn: str, genre: str,
                  publication_year: int, total_copies: int):
        """Initialize a book with its details and set available copies."""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_year = publication_year
        self.total_copies = total_copies
        self.available_copies = total_copies



    def __str__(self) -> str:
        """Return a user-friendly string representation of the book."""
        return f"""
        Book Name : {self.title}
        Written By : {self.author}
        ISBN : {self.isbn}
        Genre : {self.genre}
        Publication Year : {self.publication_year}
        Total Copies : {self.total_copies}
        Available Copies : {self.available_copies}
        """



























































































