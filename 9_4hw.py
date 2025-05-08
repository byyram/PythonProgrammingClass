import csv

def displaygrades(filename="grades.csv"):
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        #print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(*header))

        for row in reader:
            print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(*row))

displaygrades()