import sqlite3

# 
connection = sqlite3.connect("lecture_4/school.db")

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY,
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


students = [
    ("Alice Johnson", 2005),
    ("Brian Smith", 2004),
    ("Carla Reyes", 2006),
    ("Daniel Kim", 2005),
    ("Eva Thompson", 2003),
    ("Felix Nguyen", 2007),
    ("Grace Patel", 2005),
    ("Henry Lopez", 2004),
    ("Isabella Martinez", 2006)    
]

grades = [
    (1, "Math", 88),
    (1, "English", 92),
    (1, "Science", 85),
    (2, "Math", 75),
    (2, "History", 83),
    (2, "English", 79),
    (3, "Science", 95),
    (3, "Math", 91),
    (3, "Art", 89),
    (4, "Math", 84),
    (4, "Science", 88),
    (4, "Physical Education", 93),
    (5, "English", 90),
    (5, "History", 85),
    (5, "Math", 88),
    (6, "Science", 72),
    (6, "Math", 78),
    (6, "English", 81),
    (7, "Art", 91),
    (7, "Science", 87),
    (7, "Math", 90),
    (8, "History", 77),
    (8, "Math", 83),
    (8, "Science", 80),
    (9, "English", 96),
    (9, "Math", 89),
    (9, "Art", 92)
]

cursor.executemany("INSERT INTO students (full_name, birth_year) VALUES (?, ?)", students)
cursor.executemany("INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)", grades)

connection.commit()
connection.close()