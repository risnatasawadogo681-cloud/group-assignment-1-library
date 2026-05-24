
# main.py
# Group 1 — Library Management System
# Burkina Institute of Technology — PRG1406
#
# Authors:
#   - Gadiere Houzeimatou Farida : Part 1 — User inputs, validation, summary
#   - Sawadogo Risnata           : Chef de projet — final testing

from classes import Book

def get_integer(prompt):
    """Ask the user for an integer. Re-prompt if input is invalid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Erreur ! Veuillez entrer un nombre entier valide.")

def get_float(prompt):
    """Ask the user for a float. Re-prompt if input is invalid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Erreur ! Veuillez entrer un nombre valide.")

print("=" * 50)
print("   SYSTEME DE GESTION DE BIBLIOTHEQUE")
print("   Burkina Institute of Technology")
print("=" * 50)

print("\n--- INFORMATIONS DE LA BIBLIOTHEQUE ---")

library_name = input("Nom de la bibliotheque : ")
library_city = input("Ville : ")
library_year_founded = get_integer("Annee de fondation : ")
library_capacity = get_integer("Capacite totale (nombre de livres) : ")
daily_fine = get_float("Amende par jour de retard (FCFA) : ")
weekend_input = input("Ouverte le weekend ? (oui/non) : ").strip().lower()
is_open_weekend = weekend_input == "oui"

print("\n--- INFORMATIONS DU LIVRE ---")

book_title = input("Titre du livre : ")
book_author = input("Auteur : ")
book_year = get_integer("Annee de publication : ")
book_isbn = input("ISBN : ")
book_genre = input("Genre (ex: Roman, Science, Histoire) : ")
book_copies = get_integer("Nombre d'exemplaires : ")
book_price = get_float("Prix par exemplaire (FCFA) : ")
available_input = input("Le livre est-il disponible ? (oui/non) : ").strip().lower()
book_available = available_input == "oui"

total_stock_value = book_copies * book_price
years_of_existence = 2026 - library_year_founded
weekly_fine = daily_fine * 7

book = Book(book_title, book_author, book_year, book_isbn, book_genre, book_copies)
book.is_available = book_available

print("\n")
print("=" * 50)
print("         RAPPORT FINAL — RECAPITULATIF")
print("=" * 50)

print(f"\n BIBLIOTHEQUE")
print(f"  Nom              : {library_name}")
print(f"  Ville            : {library_city}")
print(f"  Annee fondation  : {library_year_founded}")
print(f"  Annees existence : {years_of_existence} ans")
print(f"  Capacite totale  : {library_capacity} livres")
print(f"  Ouverte weekend  : {'Oui' if is_open_weekend else 'Non'}")
print(f"  Amende / jour    : {daily_fine:.2f} FCFA")
print(f"  Amende / semaine : {weekly_fine:.2f} FCFA")

print(f"\n LIVRE ENREGISTRE")
print(book)

print(f"\n CALCULS")
print(f"  Prix par exemplaire  : {book_price:.2f} FCFA")
print(f"  Nombre d'exemplaires : {book_copies}")
print(f"  Valeur totale stock  : {total_stock_value:.2f} FCFA")
print(f"  Nombre d'exemplaires : {len(book)}")

print(f"\n FICHE COMPLETE")
print(f"  {book.full_record}")

print(f"\n ETIQUETTE COLLECTION")
print(f"  {Book.library_collection_label()}")

print("\n" + "=" * 50)
print("   Fin du programme. Merci !")
print("=" * 50)
