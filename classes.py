# classes.py
# Group 23 — Library Management System
# Burkina Institute of Technology 
#
# Authors:
#   - Koutiebou Salamata F. Ornella  : Part 2 — Parent class Document
#   - Zarani Mamadou Aboud Kader     : Part 2 — Child class Book
#   - Zongo Safiatou                 : Parts 3 & 4 — Magic methods + Decorators

# Ornella code here — Parent class Document


class Document:
    """
    Parent class representing a general library document.
    All document types in the library inherit from this class.
    """

    def __init__(self, title: str, author: str, year: int):
        self.title = title          
        self.author = author        
        self.year = year            
        self.is_available = True    

    def display_info(self) -> str:
        """Return a short string with basic document info."""
        return f"{self.title} by {self.author} ({self.year})"

    def borrow(self) -> str:
        """Mark the document as borrowed if available."""
        if self.is_available:
            self.is_available = False
            return f"SUCCESS: '{self.title}' has been borrowed."
        return f"UNAVAILABLE: '{self.title}' is currently not available."

    def return_document(self) -> str:
        """Mark the document as returned and available again."""
        self.is_available = True
        return f"SUCCESS: '{self.title}' has been returned to the library."





# Zarani code here — Child class Book
# =============================================================
#  PART 2 — TASK: Zarani Mamadou Aboud Kader
#  Child Class: Book (inherits from Document)
#  A Book IS a Document — extends it with library-specific data
# =============================================================

class Book(Document):
    """
    Child class representing a physical book in the library.
    Inherits all attributes and methods from Document,
    and adds book-specific attributes: ISBN, genre, copies.

    Relationship: A Book IS-A Document.
    """

    def __init__(self, title: str, author: str, year: int,
                 isbn: str, genre: str, copies: int):
        """
        Initialise a Book instance.

        Args:
            title  (str): Book title
            author (str): Author's full name
            year   (int): Publication year
            isbn   (str): International Standard Book Number
            genre  (str): Book genre (e.g. Science, History)
            copies (int): Number of physical copies in stock
        """
        # Call the parent constructor to set shared attributes
        super().__init__(title, author, year)

        # New attributes specific to Book (not in Document)
        self.isbn = isbn        # str — unique identifier
        self.genre = genre      # str — book category
        self.copies = copies    # int — number of copies available

    def check_stock(self) -> str:
        """Return a message indicating how many copies are in stock."""
        if self.copies > 0:
            return f"IN STOCK: {self.copies} copy/copies available."
        return "OUT OF STOCK: No copies currently available."

    def add_copies(self, number: int) -> str:
        """
        Add more copies of this book to the library collection.

        Args:
            number (int): Number of copies to add

        Returns:
            str: Updated stock message
        """
        self.copies += number
        return f"{number} copy/copies added. New total: {self.copies}"

# Safiatou code here — Magic methods + Decorators
# =============================================================
    #  PARTS 3 & 4 — TASK: Zongo Safiatou
    #  Magic methods : __str__, __eq__, __len__
    #  Decorators    : @property, @staticmethod
    # =============================================================

    def __str__(self) -> str:
        """Retourne une représentation lisible du livre."""
        status = "Available" if self.is_available else "Borrowed"
        return (
            f"[Book] '{self.title}' by {self.author} ({self.year}) | "
            f"Genre: {self.genre} | ISBN: {self.isbn} | "
            f"Copies: {self.copies} | Status: {status}"
        )

    def __eq__(self, other: object) -> bool:
        """Deux livres sont égaux s'ils ont le même ISBN."""
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn == other.isbn

    def __len__(self) -> int:
        """Retourne le nombre de copies avec len(book)."""
        return self.copies

    @property
    def summary(self) -> str:
        """Résumé court, accessible comme book.summary (sans parenthèses)."""
        return f"'{self.title}' ({self.year}) — {self.genre} | {self.copies} copies"

    @staticmethod
    def is_valid_isbn(isbn: str) -> bool:
        """Vérifie si un ISBN est valide (10 ou 13 chiffres)."""
        digits_only = isbn.replace("-", "").replace(" ", "")
        return len(digits_only) in (10, 13) and digits_only.isdigit()
