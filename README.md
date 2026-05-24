# Library Management System — Group 1

## Description
This program simulates a university library management system.
It allows a librarian to register a book, view its details,
and get a complete summary report at the end of the session.

## Group Members
| Name | Role |
|---|---|
| Sawadogo Risnata | Chef de Projet — GitHub & Coordination |
| Gadiere Houzeimatou Farida | Part 1 — User inputs & Validation |
| Koutiebou Salamata F. Ornella | Part 2 — Parent class Document |
| Zarani Mamadou Aboud Kader | Part 2 — Child class Book |
| Zongo Safiatou | Parts 3 & 4 — Magic methods & Decorators |

## Classes
- Document (parent class) — title, author, year, is_available
- Book (child class) — inherits from Document, adds isbn, genre, copies

## OOP Concepts Used
- Inheritance : Book IS-A Document
- Magic methods : __str__, __eq__, __len__
- Decorators : @property and @staticmethod

## How to Run
python main.py

## Course
PRG1406 — Advanced Programming (Python and C)
Burkina Institute of Technology — May 2026
