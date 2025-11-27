students = []

def get_students_with_grades(students):
    # create a list with students who has any grade
    return [s for s in students if s["grades"]]

def average(grades):
    # calculate average grade if grades exist
    return sum(grades) / len(grades) if grades else None

def add_student(students):
    # Input new student name
    name = input("Enter student name: ")
    # Check if student exists
    if any(s["name"] == name for s in students):
        print(f"Student '{name}' exists.")
    else:
        # Create a dict with keys "name" and "grades"
        students.append({"name": name, "grades": []})
        # Add student to list
        print(f"Student '{name}' added.")

def add_grades(students):
    # Input new student name
    name = input("Enter student name: ")
    # Check if student exists
    student = next((s for s in students if s["name"] == name), None)
    if not student:
        print(f"Student '{name}' doesn't exist.")
        return
    # input grades
    while True:
        grade_str = input("Enter a grade (or 'done' to finish): ")
        if grade_str.lower() == "done":
            break
        # try to convert str to int
        if grade_str.isdigit():
            grade = int(grade_str)
            if grade <=100:
                student["grades"].append(grade)
            else:
                print("Error: you must enter a number between 0 - 100.")
        else:
            print("Error: you must enter a number between 0 - 100.")

def generate_report(students):
    print("--- Student Report ---")
    students_with_grades = get_students_with_grades(students)
    for s in students:
        avg = average(s["grades"])
        # output average grade or N/A if no grades
        print(f"{s['name']}'s average grade is {avg if avg is not None else 'N/A'}")
    print("-------------------------")
    if students_with_grades:
        # count min, max and overall average grade if 'students_with_grades' is not empty
        max_avg = max(students_with_grades, key=lambda s: average(s["grades"]))
        min_avg = min(students_with_grades, key=lambda s: average(s["grades"]))
        overall_avg = sum(average(s["grades"]) for s in students_with_grades) / len(students_with_grades)
        # output results
        print(f"Max average: {average(max_avg['grades'])}")
        print(f"Min average: {average(min_avg['grades'])}")
        print(f"Overall average: {overall_avg}")
    else:
        # the case when 'students_with_grades' is empty
        print("No students with grades.")

def find_top_student(students):
    students_with_grades = get_students_with_grades(students)
    if students_with_grades:
        # identify the student with the highest average grade and output information about him
        top = max(students_with_grades, key=lambda s: average(s["grades"]))
        print(f"The student with the highest average is {top['name']} with grade of {average(top['grades'])}")
    else:
        # the case when 'students_with_grades' is empty
        print("No students with grades.")

def exit_program(students):
    # exit program
    print("Exiting program")
    exit()

# Меню как словарь
actions = {
    "1": add_student,
    "2": add_grades,
    "3": generate_report,
    "4": find_top_student,
    "5": exit_program
}

while True:
    # menu text
    print("--- Students Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit program")

    # choice input
    choice = input("Enter your choice: ")
    action = actions.get(choice)
    if action:
        action(students)
    else:
        print("Invalid choice")
