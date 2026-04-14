"""
bookstore_cli.py
A command-line interface for managing a SQLite bookstore database.
"""

import sqlite3

DB_NAME = "bookstore.db"


def get_connection():
    """Open a connection to bookstore.db with foreign keys enabled."""
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn


# ── READ operations ────────────────────────────────────────────────────────────

def view_all_categories():
    with get_connection() as conn:
        rows = conn.execute("SELECT categoryId, categoryName FROM category ORDER BY categoryName").fetchall()
    if not rows:
        print("  No categories found.")
        return
    print(f"\n  {'ID':<5} {'Category'}")
    print("  " + "-" * 30)
    for row in rows:
        print(f"  {row['categoryId']:<5} {row['categoryName']}")


def view_all_books():
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT b.bookId, b.title, b.author, b.price, c.categoryName, b.readNow
            FROM book b
            JOIN category c ON b.categoryId = c.categoryId
            ORDER BY c.categoryName, b.title
        """).fetchall()
    if not rows:
        print("  No books found.")
        return
    print(f"\n  {'ID':<5} {'Title':<40} {'Author':<25} {'Price':>7}  {'Category':<15} {'ReadNow'}")
    print("  " + "-" * 105)
    for row in rows:
        read = "Yes" if row['readNow'] else "No"
        print(f"  {row['bookId']:<5} {row['title']:<40} {row['author']:<25} ${row['price']:>6.2f}  {row['categoryName']:<15} {read}")


def view_books_in_category():
    category_id = input("  Enter category ID: ").strip()
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT b.bookId, b.title, b.author, b.isbn, b.price, b.readNow
            FROM book b
            JOIN category c ON b.categoryId = c.categoryId
            WHERE b.categoryId = ?
            ORDER BY b.title
        """, (category_id,)).fetchall()
    if not rows:
        print("  No books found for that category.")
        return
    print(f"\n  {'ID':<5} {'Title':<40} {'Author':<25} {'ISBN':<15} {'Price':>7}  {'ReadNow'}")
    print("  " + "-" * 105)
    for row in rows:
        read = "Yes" if row['readNow'] else "No"
        print(f"  {row['bookId']:<5} {row['title']:<40} {row['author']:<25} {row['isbn']:<15} ${row['price']:>6.2f}  {read}")


def search_books_by_title():
    keyword = input("  Enter title keyword: ").strip()
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT b.bookId, b.title, b.author, b.price, c.categoryName
            FROM book b
            JOIN category c ON b.categoryId = c.categoryId
            WHERE b.title LIKE ?
            ORDER BY b.title
        """, (f"%{keyword}%",)).fetchall()
    if not rows:
        print("  No books matched your search.")
        return
    print(f"\n  {'ID':<5} {'Title':<40} {'Author':<25} {'Price':>7}  {'Category'}")
    print("  " + "-" * 95)
    for row in rows:
        print(f"  {row['bookId']:<5} {row['title']:<40} {row['author']:<25} ${row['price']:>6.2f}  {row['categoryName']}")


def search_books_by_author():
    """Bonus feature: search books by author name."""
    keyword = input("  Enter author keyword: ").strip()
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT b.bookId, b.title, b.author, b.price, c.categoryName
            FROM book b
            JOIN category c ON b.categoryId = c.categoryId
            WHERE b.author LIKE ?
            ORDER BY b.author, b.title
        """, (f"%{keyword}%",)).fetchall()
    if not rows:
        print("  No books matched that author.")
        return
    print(f"\n  {'ID':<5} {'Title':<40} {'Author':<25} {'Price':>7}  {'Category'}")
    print("  " + "-" * 95)
    for row in rows:
        print(f"  {row['bookId']:<5} {row['title']:<40} {row['author']:<25} ${row['price']:>6.2f}  {row['categoryName']}")


# ── CREATE operation ───────────────────────────────────────────────────────────

def add_new_book():
    print("\n  -- Add a New Book --")
    view_all_categories()

    category_id = input("\n  Category ID      : ").strip()
    title       = input("  Title            : ").strip()
    author      = input("  Author           : ").strip()
    isbn        = input("  ISBN             : ").strip()
    price_str   = input("  Price            : ").strip()
    image       = input("  Image filename   : ").strip()
    read_now    = input("  Available to read now? (1=Yes / 0=No): ").strip()

    # Basic validation
    try:
        price = float(price_str)
    except ValueError:
        print("  Invalid price. Book not added.")
        return
    if read_now not in ("0", "1"):
        print("  readNow must be 0 or 1. Book not added.")
        return

    try:
        with get_connection() as conn:
            conn.execute("""
                INSERT INTO book (categoryId, title, author, isbn, price, image, readNow)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (category_id, title, author, isbn, price, image, int(read_now)))
        print("  Book added successfully!")
    except sqlite3.IntegrityError as e:
        print(f"  Could not add book: {e}")


# ── UPDATE operation ───────────────────────────────────────────────────────────

def update_book_price():
    book_id   = input("  Enter book ID to update: ").strip()
    new_price = input("  Enter new price        : ").strip()

    try:
        price = float(new_price)
    except ValueError:
        print("  Invalid price. No changes made.")
        return

    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE book SET price = ? WHERE bookId = ?",
            (price, book_id)
        )
    if cursor.rowcount == 0:
        print("  No book found with that ID.")
    else:
        print("  Price updated successfully!")


# ── DELETE operation ───────────────────────────────────────────────────────────

def delete_book():
    book_id = input("  Enter book ID to delete: ").strip()
    confirm = input(f"  Are you sure you want to delete book {book_id}? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("  Delete cancelled.")
        return

    with get_connection() as conn:
        cursor = conn.execute("DELETE FROM book WHERE bookId = ?", (book_id,))
    if cursor.rowcount == 0:
        print("  No book found with that ID.")
    else:
        print("  Book deleted successfully!")


# ── Menu ───────────────────────────────────────────────────────────────────────

def print_menu():
    print("""
╔══════════════════════════════════════╗
║         📚  Bookstore CLI            ║
╠══════════════════════════════════════╣
║  1. View all categories              ║
║  2. View all books                   ║
║  3. View books in a category         ║
║  4. Search books by title            ║
║  5. Search books by author  [bonus]  ║
║  6. Add a new book                   ║
║  7. Update a book price              ║
║  8. Delete a book                    ║
║  9. Quit                             ║
╚══════════════════════════════════════╝""")


def main():
    actions = {
        "1": view_all_categories,
        "2": view_all_books,
        "3": view_books_in_category,
        "4": search_books_by_title,
        "5": search_books_by_author,
        "6": add_new_book,
        "7": update_book_price,
        "8": delete_book,
    }

    print("\nWelcome to the Bookstore CLI!")

    while True:
        print_menu()
        choice = input("  Choose an option (1-9): ").strip()

        if choice == "9":
            print("\n  Goodbye! Happy reading!")
            break
        elif choice in actions:
            print()
            actions[choice]()
        else:
            print("  Invalid option. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()
