students = []

# create a list with students who has any grade
students_with_grades = []
while True:
    # menu text
    print("--- Students Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit program")

    # chouice input
    choice = input("Enter your choice: ")

    if choice == "1":
        # Input new student name
        name = input("Enter student name: ")

        # Check if student exists
        exists = any(student["name"] == name for student in students)

        if exists:
            print(f"Student '{name}' exists.")
        else:
            # Create a dict with keys "name" and "grades"
            new_student = {
                "name": name,
                "grades": [],
            }
            # Add student to list
            students.append(new_student)
            print(f"Student '{name}' added.")

    elif choice == "2":
        # Input new student name
        name = input("Enter student name: ")
        # Check if student exists
        student = next((s for s in students if s["name"] == name), None)
        if student:     
            while True:
                # input grades
                grade_str = input("Enter a grade (or 'done' to finish): ")

                if grade_str.lower() == "done":
                    break
                # Check if "grade_str is digit"
                if grade_str.isdigit():
                    grade = int(grade_str)
                    # Check if grade is not lower than 100
                    if grade <= 100:
                        student["grades"].append(int(grade_str))
                    else:
                        print("Error: you must enter a number between 0 and 100.")
                else:
                    print("Error: you must enter a number between 0 and 100.")
        else:
            print(f"Student '{name}' doesn't exist.")

    elif choice == "3":
        print("--- Student Report ---") 
        for student in students:
            try:
                # create new key to save average grade if it doesn't exist
                student["average"] = sum(student["grades"])/len(student["grades"])
                # add student who has any grades and his average grade
                students_with_grades.append(student)

                print(f"{student['name']}'s average grade is {student["average"]}")
                        
            except ZeroDivisionError:
                # the case when a student has no grades
                print(f"{student['name']}'s average grade is N/A")
        print("-------------------------")

        if students_with_grades:
            # count min, max and overall average grade if 'sudents_with_grades' is not empty
            max_average = max(students_with_grades, key=lambda s: s["average"])["average"]
            min_average = min(students_with_grades, key=lambda s: s["average"])["average"]
            overall_average = sum(s["average"] for s in students_with_grades) / len(students_with_grades)

            # output results
            print(f"Max average: {max_average}")
            print(f"Min average: {min_average}")
            print(f"Overall average: {overall_average}")
        else:
            if not students:
                # the case when 'sudents' is empty
                print("There are no students in the list. Enter students and their grades")
            else:
                # the case when 'sudents_with_grades' is empty
                print("There are no students with grades. Enter students' grades")

    elif choice == "4":
        if students_with_grades:
            # identify the student with the highest average grade and output information about him
            top_student = max(students_with_grades, key=lambda s: s["average"])
            print(f"The student with the highest average is {top_student["name"]} with grade of {top_student["average"]}")
        else:
            if not students:
                # the case when 'sudents' is empty
                print("There are no students in the list. Enter students and their grades")
            else:
                # the case when 'sudents_with_grades' is empty
                print("There are no students with grades. Enter students' grades")


    elif choice == "5":
        print("Exitting program")
        break
        