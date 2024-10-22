# Problem 1: Student Management System
# Create a program to manage student information for a class. Implement the following features:
# Store student details like name, age, and marks in a dictionary where the key is the student’s name and the value is another dictionary with age and marks.
# Allow the user to add new students, update details of existing students, and display all student details.
# Use if-else conditions to evaluate the student's grade based on their marks and display it (e.g., A, B, C, D, or F).
# The program should continue to accept inputs until the user chooses to exit.

students = {}

def add_student(name , age , marks):
    students[name] = {
        "age" : age,
        "marks" : marks
    }
    print("Data added")

def update_student(name):
    if name in students:
        print(f"Current details for {name}: Age: {students[name]['age']}, Marks: {students[name]['marks']}")

        print("What would you like to update?")
        print("1. Age")
        print("2. Marks")
        
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            new_age = int(input("Enter new age: "))
            students[name]['age'] = new_age
            print(f"{name}'s age updated successfully.")

        elif choice == '2':
            new_marks = float(input("Enter new marks: "))
            students[name]['marks'] = new_marks
            print(f"{name}'s marks updated successfully.")

        else:
            print("Invalid choice.")
    else:
        print(f"Student {name} not found.")


def display_student():
    print("Name\t Age\t Marks\t")
    for name,details in students.items():
        print(f"{name}\t {details["age"]}\t {details["marks"]}")

while True:
    print("\n1. Add Student")
    print("2. Update Student")
    print("3. Display Student")
    print("4. Exit\n")

    ch = int(input("Enter your choice : "))

    if ch == 1:
        name = (input("Enter Name : "))
        age = int(input("Enter age : "))
        marks = int(input("Enter marks : "))
        add_student(name , age , marks)

    elif ch == 2:
        n = input("Enter name : ")
        update_student(n)

    elif ch == 3:
        display_student()

    elif ch == 4:
        break

    else:
        print("invalid")