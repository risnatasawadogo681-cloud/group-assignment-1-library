# main.py
# PRG1406 — Advanced Programming (Python and C)
# Group Assignment 1 — Library Management System
# Burkina Institute of Technology | May 2026
#
# Responsibilities:
#   - Gadiere Houzeimatou Farida : Part 1 — Inputs, validation, summary
#   - Sawadogo Risnata           : Coordination, final testing

from classes import Book

# =============================================================================
# VALIDATION HELPERS
# Coded by: Gadiere Houzeimatou Farida
# =============================================================================

def get_integer(prompt: str) -> int:
    """Ask for an integer and re-prompt until the user enters a valid one."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("  Invalid input. Please enter a whole number.")

def get_float(prompt: str) -> float:
    """Ask for a float and re-prompt until the user enters a valid one."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("  Invalid input. Please enter a number (e.g. 12.5).")

def get_positive_integer(prompt: str) -> int:
    """Ask for a strictly positive integer."""
    while True:
        value = get_integer(prompt)
        if value > 0:
            return value
        print("  Value must be greater than zero.")

def get_positive_float(prompt: str) -> float:
    """Ask for a strictly positive float."""
    while True:
        value = get_float(prompt)
        if value > 0:
            return value
        print("  Value must be greater than zero.")


# =============================================================================
# MAIN PROGRAM
# Coded by: Gadiere Houzeimatou Farida
# =============================================================================

def main():
    print("=" * 55)
    print("   BURKINA INSTITUTE OF TECHNOLOGY")
    print("   Library Management System — PRG1406")
    print("=" * 55)

    # ------------------------------------------------------------------
    # SECTION 1 — Library General Information (inputs 1 to 5)
    # ------------------------------------------------------------------
    print("\n--- SECTION 1 : Library Information ---\n")

    # Input 1 — str
    library_name: str = input("Enter the library name: ").strip()

    # Input 2 — str
    librarian_name: str = input("Enter the librarian's full name: ").strip()

    # Input 3 — int
    year_founded: int = get_positive_integer("Enter the year the library was founded: ")

    # Input 4 — float
    annual_budget: float = get_positive_float("Enter the annual budget (in FCFA, e.g. 5000000.0): ")

    # Input 5 — bool (correct method: compare string, never bool(input(...)))
    is_open_weekend: bool = input("Is the library open on weekends? (yes/no): ").strip().lower() == "yes"

    # ------------------------------------------------------------------
    # SECTION 2 — Book Information (inputs 6 to 14)
    # ------------------------------------------------------------------
    print("\n--- SECTION 2 : Book Registration ---\n")

    # Input 6 — str
    title: str = input("Enter the book title: ").strip()

    # Input 7 — str
    author: str = input("Enter the author's full name: ").strip()

    # Input 8 — int
    publication_year: int = get_positive_integer("Enter the publication year: ")

    # Input 9 — str
    isbn: str = input("Enter the ISBN (e.g. 978-3-16-148410-0): ").strip()

    # Input 10 — str
    genre: str = input("Enter the genre (e.g. Science, Fiction, History): ").strip()

    # Input 11 — int
    copies: int = get_positive_integer("Enter the number of copies in stock: ")

    # Input 12 — float
    price_per_copy: float = get_positive_float("Enter the price per copy (in FCFA): ")

    # Input 13 — float
    late_fee_per_day: float = get_positive_float("Enter the late fee per day (in FCFA): ")

    # Input 14 — bool (correct method)
    is_available: bool = input("Is the book currently available? (yes/no): ").strip().lower() == "yes"

    # ------------------------------------------------------------------
    # ARITHMETIC EXPRESSIONS (3 required)
    # ------------------------------------------------------------------

    # Expression 1 — Total stock value
    total_stock_value: float = copies * price_per_copy

    # Expression 2 — Years of existence of the library
    current_year: int = 2026
    years_of_existence: int = current_year - year_founded

    # Expression 3 — Weekly late fee
    weekly_late_fee: float = late_fee_per_day * 7

    # ------------------------------------------------------------------
    # CREATE THE BOOK OBJECT (compatible with Zarani's Book class)
    # ------------------------------------------------------------------
    book = Book(
        title=title,
        author=author,
        year=publication_year,
        isbn=isbn,
        genre=genre,
        copies=copies
    )

    # Set availability manually after creation
    book.is_available = is_available

    # ------------------------------------------------------------------
    # USE THE BOOK OBJECT
    # ------------------------------------------------------------------
    print("\n--- BOOK RECORD ---")
    print(f"  {book.display_info()}")
    print(f"  {book.check_stock()}")

    # ------------------------------------------------------------------
    # SUMMARY SCREEN (f-strings only)
    # ------------------------------------------------------------------
    weekend_text = "Yes" if is_open_weekend else "No"
    avail_text   = "Yes" if is_available else "No"

    print("\n")
    print("=" * 55)
    print("   FINAL SUMMARY REPORT")
    print("=" * 55)

    print(f"\n  {'LIBRARY INFORMATION':^45}")
    print(f"  {'-'*45}")
    print(f"  Library Name      : {library_name}")
    print(f"  Librarian         : {librarian_name}")
    print(f"  Year Founded      : {year_founded}")
    print(f"  Years in Service  : {years_of_existence} year(s)")
    print(f"  Annual Budget     : {annual_budget:,.0f} FCFA")
    print(f"  Open on Weekends  : {weekend_text}")

    print(f"\n  {'BOOK DETAILS':^45}")
    print(f"  {'-'*45}")
    print(f"  Title             : {title}")
    print(f"  Author            : {author}")
    print(f"  Publication Year  : {publication_year}")
    print(f"  ISBN              : {isbn}")
    print(f"  Genre             : {genre}")
    print(f"  Copies in Stock   : {copies}")
    print(f"  Available Now     : {avail_text}")

    print(f"\n  {'FINANCIAL CALCULATIONS':^45}")
    print(f"  {'-'*45}")
    print(f"  Price per Copy    : {price_per_copy:,.0f} FCFA")
    print(f"  Total Stock Value : {total_stock_value:,.0f} FCFA")
    print(f"  Late Fee / Day    : {late_fee_per_day:,.0f} FCFA")
    print(f"  Late Fee / Week   : {weekly_late_fee:,.0f} FCFA")

    print("\n" + "=" * 55)
    print("   Program completed successfully.")
    print("   BIT — PRG1406 Group Assignment 1 | May 2026")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()
