import sqlite3

conn = sqlite3.connect('app.db')
cur = conn.cursor()

# --------------------------------------------------------------------------- #

cur.execute("SELECT * FROM departments")

rows = cur.fetchall()

print(" --- DEPARTMENTS --- ")
for row in rows:
    print(row)


# --------------------------------------------------------------------------- #


cur.execute("SELECT * FROM students")

rows = cur.fetchall()

print("\n --- STUDENTS --- ")
for row in rows:
    print(row)


