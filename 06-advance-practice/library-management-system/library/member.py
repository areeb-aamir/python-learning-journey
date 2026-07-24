"""
Member Module - represent members Data in library system
"""

class Member:
    """ Parent Class - Gives General Info """
    def __init__(self, name : str, id : int,):
        self.name = name
        self.id = id
        self.borrowed_books = []
        self.max_limit = 5

    def __str__(self) -> str:
        """Return a user-friendly string representation of the Member."""
        return f"""
        Name : {self.name}
        ID : {self.id}
        Borrowed Books : {self.borrowed_books}
        """


    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "id": self.id,
            "borrowed_books": self.borrowed_books,
            "max_limit": self.max_limit
        }


class Student(Member):
    """Inherited Class - Gives Extra Info rather than general"""
    def __init__(self, name : str, id : int):
        super().__init__(name, id,)
        self.max_limit = 3


class Faculty(Member):
    """Inherited Class - Gives Extra Info rather than general"""
    def __init__(self, name : str, id : int,):
        super().__init__(name, id,)
        self.max_limit = 10



