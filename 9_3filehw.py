import csv
def store_student_grades(filename="grades.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["firstname", "lastname", "exam1grade", "exam2grade", "exam3grade"])  # Write header row

        while True:
            first_name = input("Enter student's first name (or 'done' to finish): ")
            if first_name.lower() == "done":
                break

            last_name = input("Enter student's last name: ")

            
            exam1 = int(input("Enter exam 1 grade: "))
            exam2 = int(input("Enter exam 2 grade: "))
            exam3 = int(input("Enter exam 3 grade: "))

            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print(f"Student grades stored in {filename}")

store_student_grades()

def read_student_grades(filename="grades.csv"):
    with open(filename, 'r', newline='') as file:
      reader = csv.reader(file)
      for row in reader:
        print(row)

read_student_grades()