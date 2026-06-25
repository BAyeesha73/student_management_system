import sqlite3

conn = sqlite3.connect("students1.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")
conn.commit()


def insert_student(name, age, course):
    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    conn.commit()


def fetch_students():
    conn = sqlite3.connect("students1.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows



def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()


def update_student(student_id, name, age, course):
    cursor.execute("""
        UPDATE students
        SET name=?, age=?, course=?
        WHERE id=?
    """, (name, age, course, student_id))
    conn.commit()


def search_student(keyword):
    cursor.execute("""
        SELECT * FROM students
        WHERE name LIKE ? OR id=?
    """, (f"%{keyword}%", keyword if keyword.isdigit() else -1))
    return cursor.fetchall()