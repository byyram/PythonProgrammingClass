def analyze_grades_from_file(filename="grades.txt"):
    grades = []
    with open(filename, "r") as file:
        for line in file:
            grade = float(line.strip())
            grades.append(grade)

    if grades:
        print("grades:")
        for grade in grades:
            print(grade)

        total = sum(grades)
        count = len(grades)
        average = total / count

        print(f"\nTotal: {total}")
        print(f"count: {count}")
        print(f"average: {average}")
    else:
        print("this file dont work")

analyze_grades_from_file()