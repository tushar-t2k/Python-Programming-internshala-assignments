import sqlite3

# Connect to the database (or create it)
db = sqlite3.connect("m5assignment.db")
cur = db.cursor()

# Create the table
cur.execute("""
CREATE TABLE books (
    BookID INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT,
    price REAL
);
""")

# Insert 5 records
for x in range(5):
    ttl = input("Enter book's title: ")
    aut = input("Enter name of author: ")
    pr = float(input("Enter price: "))
    
    sql = "INSERT INTO books (title, author, price) VALUES (?, ?, ?)"
    
    try:
        cur.execute(sql, (ttl, aut, pr))
        db.commit()
        print("One record added successfully")
    except Exception as e:
        print("Error in operation:", e)
        db.rollback()

db.close()
