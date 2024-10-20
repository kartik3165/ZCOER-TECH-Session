students = {
    "ABC": {"age": 20, "marks": 85},
    "PQR": {"age": 21, "marks": 75},
    "XYZ": {"age": 22, "marks": 90}
}

while True:
    print("Student Management System")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Display Students")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        marks = float(input("Enter student's marks: "))
        students[name] = {'age': age, 'marks': marks}
        print(f"Student {name} added successfully.")

    elif choice == '2':
        name = input("Enter the name of the student to update: ")
        if name in students:
            age = int(input("Enter new age: "))
            marks = float(input("Enter new marks: "))
            students[name] = {'age': age, 'marks': marks}
        else:
            print("Student not found.")

    elif choice == '3':
        if not students:
            print("No student records found.")
        else:
            for name, details in students.items():
                marks = details['marks']
                if marks >= 90:
                    grade = 'A'
                elif marks >= 80:
                    grade = 'B'
                elif marks >= 70:
                    grade = 'C'
                elif marks >= 60:
                    grade = 'D'
                else:
                    grade = 'F'
                
                print(f"Name: {name}, Age: {details['age']}, Marks: {marks}, Grade: {grade}")

    elif choice == '4':
        print("Exiting....")
        break

    else:
        print("Invalid choice. Please try again.")
