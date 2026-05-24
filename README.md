Library Management System - Group 23

Burkina Institute of Technology



A Python project modeling a library system using OOP.





CLASSES

=======



Document (by Ornella)

Parent class with: title, author, year, is\_available

Methods: display\_info(), borrow(), return\_document()



Book - child of Document (by Zarani)

Child class with: isbn, genre, copies

Methods: check\_stock(), add\_copies()



Magic Methods and Decorators (by Safiatou)

\- \_\_str\_\_()          : print(book)

\- \_\_eq\_\_()           : compare two books by ISBN

\- \_\_len\_\_()          : len(book) returns number of copies

\- summary            : book.summary returns a short description

\- is\_valid\_isbn()    : checks if an ISBN is valid





AUTHORS

=======

Ornella   : Classe Document

Zarani    : Classe Book

Safiatou  : Magic methods + Decorators + README

Farida    : main.py

Risnata   : Chef de projet - GitHub et Coordination





HOW TO RUN

==========

python main.py





COURSE

======

PRG1406 - Advanced Programming (Python and C)

Burkina Institute of Technology - May 2026

