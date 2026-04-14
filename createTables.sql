PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS category (
    categoryId      INTEGER PRIMARY KEY AUTOINCREMENT,
    categoryName    TEXT    NOT NULL UNIQUE,
    categoryImage   TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS book (
    bookId      INTEGER PRIMARY KEY AUTOINCREMENT,
    categoryId  INTEGER NOT NULL,
    title       TEXT    NOT NULL,
    author      TEXT    NOT NULL,
    isbn        TEXT    NOT NULL UNIQUE,
    price       REAL    NOT NULL CHECK(price >= 0),
    image       TEXT    NOT NULL,
    readNow     INTEGER NOT NULL DEFAULT 0 CHECK(readNow IN (0, 1)),
    FOREIGN KEY (categoryId) REFERENCES category(categoryId)
);
