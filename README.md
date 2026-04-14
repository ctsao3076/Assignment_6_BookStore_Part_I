# 📚 Bookstore CLI

Author: Christine Tsao

## Description

A command-line bookstore application backed by SQLite. The store carries books across four
categories — Fiction, Science, History, and Self-Help — and lets you browse, search, add,
update, and delete books entirely from the terminal.

---

## Files

| File | Purpose |
|------|---------|
| `createTables.sql` | Creates the `category` and `book` tables |
| `insertRows.sql` | Populates the database with sample data |
| `bookstore.db` | The SQLite database file |
| `bookstore_cli.py` | The interactive Python CLI |
| `README.md` | This file |

---

## Setup Process
### 1. Create the database and tables
```bash
sqlite3 bookstore.db < createTables.sql
```

### 2. Insert sample data
```bash
sqlite3 bookstore.db < insertRows.sql
```

### 3. Run the CLI
```bash
python3 bookstore_cli.py
```

---

## CLI Features

| Option | Feature |
|--------|---------|
| 1 | View all categories |
| 2 | View all books |
| 3 | View books in a chosen category |
| 4 | Search books by title keyword |
| 5 | **Search books by author keyword** *(bonus feature)* |
| 6 | Add a new book |
| 7 | Update a book's price |
| 8 | Delete a book |
| 9 | Quit |

---

## Database Schema

### `category`
| Column | Type | Constraints |
|--------|------|-------------|
| categoryId | INTEGER | PRIMARY KEY AUTOINCREMENT |
| categoryName | TEXT | NOT NULL, UNIQUE |
| categoryImage | TEXT | NOT NULL |

### `book`
| Column | Type | Constraints |
|--------|------|-------------|
| bookId | INTEGER | PRIMARY KEY AUTOINCREMENT |
| categoryId | INTEGER | NOT NULL, FOREIGN KEY → category |
| title | TEXT | NOT NULL |
| author | TEXT | NOT NULL |
| isbn | TEXT | NOT NULL, UNIQUE |
| price | REAL | NOT NULL, CHECK ≥ 0 |
| image | TEXT | NOT NULL |
| readNow | INTEGER | NOT NULL DEFAULT 0, CHECK IN (0,1) |

---

## Notes

- All user input is handled with parameterized queries (`?` placeholders) to prevent SQL injection.
- Foreign key enforcement is enabled with `PRAGMA foreign_keys = ON;`.
- The bonus feature (option 5) allows searching by author name using a `LIKE` pattern match.
