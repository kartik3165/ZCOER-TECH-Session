employees = {
    "emp1": {"name": "Ajit", "hours worked": 100, "hourly wage": 100},
    "emp2": {"name": "Pranay", "hours worked": 80, "hourly wage": 70},
    "emp3": {"name": "Riya", "hours worked": 60, "hourly wage": 50},
}

def add_emp():
    name = input("Enter name: ")
    worked = int(input("Enter hours worked: "))
    wage = int(input("Enter wage per hour: "))
    new_emp = f"emp{len(employees) + 1}"
    employees[new_emp] = {"name": name, "hours worked": worked, "hourly wage": wage}
    print("Employee added!")

def calculate_payroll(emp):
    return emp["hours worked"] * emp["hourly wage"]

def total_payroll():
    for emp in employees.values():
        emp["payroll"] = calculate_payroll(emp)
    print("Total payroll calculated for all employees.")

def update_details():
    name = input("Enter employee name: ")
    for emp in employees.values():
        if emp["name"] == name:
            field = input("Update hours or wage? ")
            if field == "hours":
                emp["hours worked"] = int(input("Enter new hours worked: "))
            elif field == "wage":
                emp["hourly wage"] = int(input("Enter new wage: "))
            print("Employee details updated.")
            return
    print("Employee not found.")

def display_employees():
    for emp in employees.values():
        print(emp)

def check_overtime_and_bonus():
    bonus = 10000
    for emp in employees.values():
        if emp["hours worked"] > 40:
            emp["payroll"] += bonus
            emp["bonus"] = "Bonus applied"
        else:
            emp["bonus"] = "No bonus"

print("Operations:\n1. Add Employee\n2. Update Employee\n3. Display Employees\n4. Calculate Employee Payment\n5. Calculate Total Payroll\n6. Check Overtime and Bonus")

while True:
    operation = int(input("Enter operation number: "))
    
    if operation == 1:
        add_emp()
    elif operation == 2:
        update_details()
    elif operation == 3:
        display_employees()
    elif operation == 4:
        name = input("Enter employee name: ")
        for emp in employees.values():
            if emp["name"] == name:
                print(f"Total payment for {name}: {calculate_payroll(emp)}")
                break
    elif operation == 5:
        total_payroll()
    elif operation == 6:
        check_overtime_and_bonus()
        display_employees()
    
    if input("Do you want to continue? (y/n): ").lower() != 'y':
        break
