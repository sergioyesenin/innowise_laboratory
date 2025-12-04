import sqlite3

# 
connection = sqlite3.connect("lecture_4/school.db")

cursor = connection.cursor()

# Create tables 'students' and 'grades' (This queries are also in 'queries.sql')
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY ,
full_name TEXT NOT NULL,
birth_year INTEGER)               
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
id INTEGER PRIMARY KEY,
student_id INTEGER,
subject TEXT NOT NULL,
grade INTEGER,
FOREIGN KEY (student_id) REFERENCES students(id)               
)               
''')

# Other queries in 'queres.sql'. You can run them in DB Browser for SQLite

connection.commit()

connection.close()