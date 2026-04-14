PRAGMA foreign_keys = ON;

-- Categories
INSERT INTO category (categoryName, categoryImage) VALUES
    ('Fiction',          'fiction.jpg'),
    ('Science',          'science.jpg'),
    ('History',          'history.jpg'),
    ('Self-Help',        'selfhelp.jpg');

-- Fiction (categoryId = 1)
INSERT INTO book (categoryId, title, author, isbn, price, image, readNow) VALUES
    (1, 'The Great Gatsby',          'F. Scott Fitzgerald', '9780743273565', 12.99, 'gatsby.jpg',       1),
    (1, '1984',                      'George Orwell',       '9780451524935',  9.99, '1984.jpg',         1),
    (1, 'To Kill a Mockingbird',     'Harper Lee',          '9780061935466', 14.99, 'mockingbird.jpg',  0),
    (1, 'The Catcher in the Rye',    'J.D. Salinger',       '9780316769174', 11.99, 'catcher.jpg',      0);

-- Science (categoryId = 2)
INSERT INTO book (categoryId, title, author, isbn, price, image, readNow) VALUES
    (2, 'A Brief History of Time',   'Stephen Hawking',     '9780553380163', 15.99, 'briefhistory.jpg', 1),
    (2, 'The Selfish Gene',          'Richard Dawkins',     '9780198788607', 13.99, 'selfishgene.jpg',  0),
    (2, 'Cosmos',                    'Carl Sagan',          '9780345539434', 17.99, 'cosmos.jpg',       1);

-- History (categoryId = 3)
INSERT INTO book (categoryId, title, author, isbn, price, image, readNow) VALUES
    (3, 'Sapiens',                   'Yuval Noah Harari',   '9780062316097', 18.99, 'sapiens.jpg',      1),
    (3, 'The Guns of August',        'Barbara Tuchman',     '9780345476098', 16.99, 'guns.jpg',         0),
    (3, 'Team of Rivals',            'Doris Kearns Goodwin','9780743270755', 19.99, 'rivals.jpg',       0);

-- Self-Help (categoryId = 4)
INSERT INTO book (categoryId, title, author, isbn, price, image, readNow) VALUES
    (4, 'Atomic Habits',             'James Clear',         '9780735211292', 16.99, 'atomichabits.jpg', 1),
    (4, 'The 7 Habits of Highly Effective People', 'Stephen Covey', '9781982137274', 14.99, '7habits.jpg', 0),
    (4, 'Thinking, Fast and Slow',   'Daniel Kahneman',     '9780374533557', 17.99, 'thinking.jpg',     1);
