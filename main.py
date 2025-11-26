students = []

while True:
    print("--- Students Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit program")

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
                "grades": []
            }
            # Add student to list
            students.append(new_student)
            print(f"Student '{name}' added.")

    elif choice == "2":
        # Input new student name
        name = input("Enter student name: ")

        # Check if student exists
        exists = any(student["name"] == name for student in students)

        if exists:
            
            grade_str = ""
            while grade_str.lower() != "done":
                grade_str = input("Enter a grade (or 'done' to finish): ")
                if grade_str.lower() == "done":
                    break
                try:
                    grade = int(grade_str)
                    for student in students:
                        if student["name"] == name:
                            student["grades"].append(grade)
                            break
                    else:
                        print(f"Error: student '{name}' not found.\n")
                except ValueError:
                    print("Error: you must enter a number.\n")     

        else:
            print(f"Student '{name}' doesn't exist.")

    elif choice == "3":
        print("--- Student Report ---") 
        for student in students:
            try:
                print(f"{student['name']}'s average grade is {(lambda s: sum(s)/len(s))(student['grades'])}")
            except ZeroDivisionError:
                print(f"{student['name']}'s average grade is N/A")
        print("-------------------------")
        max_student = max(list(filter(lambda s: s["grades"], students)), key=lambda s: sum(s['grades']) / len(s['grades']))
        min_student = min(list(filter(lambda s: s["grades"], students)), key=lambda s: sum(s['grades']) / len(s['grades']))

        print(f"Max average: {sum(max_student['grades']) / len(max_student['grades'])}")
        print(f"Min average: {sum(min_student['grades']) / len(min_student['grades'])}")
        print(f"Overall average: {(lambda lst: sum(
    map(lambda s: sum(s["grades"]) / len(s["grades"]), filter(lambda s: s["grades"], lst))
) / len(list(filter(lambda s: s["grades"], lst))))(students)}")

    elif choice == "4":
        top_student = ((max(list(filter(lambda s: s["grades"], students)), key=lambda s: sum(s["grades"]) / len(s["grades"]))))
        print(f"The student with the highest average is {top_student["name"]} with grade of {(lambda s: sum(s)/len(s))(top_student['grades'])}")

    elif choice == "5":
        print("Exitting program")
        break
        
#добавить условия на проверку если у всех студентов нет оценок
#
#
#
#
#