def write_grades_to_file(filename = "grades.txt"):
    with open(filename, "w") as file:
        print("Enter grades: type done when ready")
        while True:
            grade_input = input("> ")
            if grade_input.lower() == 'done':
                break

            grade = float(grade_input)
            file.write(str(grade) + "\n")

    print(f"Grades written in file {filename}")

write_grades_to_file()

def calculate_average_from_file(filename = "grades.txt"):
    grades = []
    with open(filename, "r") as file:
        for line in file:
            grade = float(line.strip())
            grades.append(grade)
                
    if grades:
        average = sum(grades) / len(grades)
        print(f"average grade: {average}")

    else:
        print("this file dont work")

calculate_average_from_file()