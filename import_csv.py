import csv
import os

filename = "students.csv"

# Create file with header if it doesn't exist
if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll No", "Name", "Marks"])


# Add Student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student added successfully.")


# Search Student
def search_student():
    roll = input("Enter Roll Number to Search: ")

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)   # Skip header

        found = False
        for row in reader:
            if row[0] == roll:
                print("\nStudent Found")
                print("Roll No :", row[0])
                print("Name    :", row[1])
                print("Marks   :", row[2])
                found = True
                break

        if not found:
            print("Student not found.")


# Delete Student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    rows = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    found = False

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        for row in rows:
            if row[0] != roll:
                writer.writerow(row)
            else:
                found = True

    if found:
        print("Student deleted successfully.")
    else:
        print("Student not found.")


# Display All Students
def display_students():
    with open(filename, "r") as file:
        reader = csv.reader(file)

        print("\nStudent Records")
        print("---------------------------")

        for row in reader:
            print(row)


# Main Menu
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        display_students()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")