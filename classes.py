# classes.py
# Group 1 — Library Management System
# Burkina Institute of Technology — PRG1406
#
# Authors:
#   - Koutiebou Salamata F. Ornella  : Part 2 — Parent class Document
#   - Zarani Mamadou Aboud Kader     : Part 2 — Child class Book
#   - Zongo Safiatou                 : Parts 3 & 4 — Magic methods + Decorators

class Document:
    """Parent class representing a general document in the library."""

    def __init__(self, title, author, year):
        """Initialize a Document with title, author, year, and availability."""
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def display_info(self):
        """Display the basic information of the document."""
        status = "Available" if self.is_available else "Borrowed"
        print(f"Title     : {self.title}")
        print(f"Author    : {self.author}")
        print(f"Year      : {self.year}")
        print(f"Status    : {status}")

    def borrow(self):
        """Mark the document as borrowed."""
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' has been borrowed successfully.")
        else:
            print(f"'{self.title}' is not available — already borrowed.")

    def return_document(self):
        """Mark the document as returned and available again."""
        if not self.is_available:
            self.is_available = True
            print(f"'{self.title}' has been returned successfully.")
        else:
            print(f"'{self.title}' was not borrowed.")


class Book(Document):
    """Child class representing a book. A Book IS-A Document."""

    def __init__(self, title, author, year, isbn, genre, copies):
        """Initialize a Book — calls parent constructor and adds new attributes."""
        super().__init__(title, author, year)
        self.isbn = isbn
        self.genre = genre
        self.copies = copies

    def check_stock(self):
        """Check if copies are available in stock."""
        if self.copies > 0:
            print(f"'{self.title}' has {self.copies} copy/copies in stock.")
        else:
            print(f"'{self.title}' is out of stock.")

    def add_copies(self, number):
        """Add new copies to the stock."""
        self.copies += number
        print(f"{number} copy/copies added. Total copies: {self.copies}")

    def __str__(self):
        """Return a readable string representation of the Book object."""
        status = "Available" if self.is_available else "Borrowed"
        return (
            f"\n{'=' * 45}\n"
            f"  BOOK RECORD\n"
            f"{'=' * 45}\n"
            f"  Title   : {self.title}\n"
            f"  Author  : {self.author}\n"
            f"  Year    : {self.year}\n"
            f"  ISBN    : {self.isbn}\n"
            f"  Genre   : {self.genre}\n"
            f"  Copies  : {self.copies}\n"
            f"  Status  : {status}\n"
            f"{'=' * 45}"
        )

    def __eq__(self, other):
        """Compare two books by their ISBN. Returns True if ISBN is the same."""
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False

    def __len__(self):
        """Return the number of copies of the book."""
        return self.copies

    @property
    def full_record(self):
        """Return a complete record of the book as a formatted string."""
        status = "Available" if self.is_available else "Borrowed"
        return (
            f"Title: {self.title} | Author: {self.author} | "
            f"Year: {self.year} | ISBN: {self.isbn} | "
            f"Genre: {self.genre} | Copies: {self.copies} | Status: {status}"
        )

    @staticmethod
    def library_collection_label():
        """Return a standard label for the library collection."""
        return "BIT University Library — Official Book Collection — 2026"
