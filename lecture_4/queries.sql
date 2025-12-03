CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY,
full_name TEXT NOT NULL,
birth_year INTEGER)

CREATE TABLE IF NOT EXISTS grades (
id INTEGER PRIMARY KEY,
student_id INTEGER,
subject TEXT NOT NULL,
grade INTEGER
FOREIGN KEY (student_id) REFERENCES students(id)               
)