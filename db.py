import sqlite3

def create_database():
    # Connect to SQLite database
    conn = sqlite3.connect("studentdb.db")
    cursor = conn.cursor()

    # Create 'student' table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        major TEXT NOT NULL,
        gpa REAL NOT NULL,
        graduation_year INTEGER NOT NULL
    )
    ''')

    # Insert sample records
    students = [
        (1, "Alice", 20, "Computer Science", 3.8, 2025),
        (2, "Bob", 22, "Mathematics", 3.5, 2024),
        (3, "Charlie", 21, "Physics", 3.9, 2025),
        (4, "Diana", 23, "Biology", 3.7, 2023),
        (5, "Eve", 20, "Chemistry", 3.6, 2025),
        (6, "Frank", 24, "Economics", 3.4, 2023),
        (7, "Grace", 22, "Engineering", 3.9, 2024),
        (8, "Hank", 21, "History", 3.2, 2025),
        (9, "Ivy", 23, "Philosophy", 3.5, 2023),
        (10, "Jack", 22, "Literature", 3.6, 2024)
    ]

    cursor.executemany('''INSERT OR REPLACE INTO student VALUES (?, ?, ?, ?, ?, ?)''', students)

    conn.commit()
    conn.close()
    print("Database and table 'student' created with sample records.")

if __name__ == "__main__":
    create_database()
