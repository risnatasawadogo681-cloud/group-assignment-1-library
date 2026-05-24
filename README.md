\# Library Management System — Group 23

\*\*Burkina Institute of Technology\*\*



A Python project modeling a library system using OOP.



\## Classes



\### `Document` (by Ornella)

Parent class with: `title`, `author`, `year`, `is\_available`

Methods: `display\_info()`, `borrow()`, `return\_document()`



\### `Book(Document)` (by Zarani)

Child class with: `isbn`, `genre`, `copies`

Methods: `check\_stock()`, `add\_copies()`



\### Magic Methods \& Decorators (by Safiatou)

\- `\_\_str\_\_()` → print(book)

\- `\_\_eq\_\_()` → book1 == book2 (par ISBN)

\- `\_\_len\_\_()` → len(book)

\- `@property summary` → book.summary

\- `@staticmethod is\_valid\_isbn()` → Book.is\_valid\_isbn("...")



\## Authors

| Nom | Partie |

|-----|--------|

| Ornella | Classe Document |

| Zarani | Classe Book |

| Safiatou | Magic methods + Decorators + README |

| Farida | main.py |

