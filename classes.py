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

# Safiatou code here — Magic methods + Decorators
