employees = {
    "emp1 " : {"name" : "Ajit" , "hours worked" :100, "hourly wage" : 100  },
    "emp2 " : {"name" : "Pranay" , "hours worked" :80, "hourly wage" : 70  },
    "emp3 " : {"name" : "Riya" , "hours worked" :60, "hourly wage" : 50  }
    }

def add_emp():
        emp_count = 3
        new_emp = f"emp{emp_count+1}"
        name = input("Enter name : ")
        worked = int(input("Enter hours worked : "))
        wage = int(input("Enter wage per hour : "))
        
        employees[new_emp]={"name" : name , "hours worked" :worked, "hourly wage" : wage }
        emp_count +=1
        print(employees[new_emp].items())
         

def calculate(hours, wage):
    return hours*wage

    

def total_payroll():
    for x,y in employees.items():
        hrs =  y.get("hours worked")
        wages =  y.get("hourly wage") 
        payroll = calculate(hrs,wages)
        employees[x].update({"payroll" : payroll})
    print(employees.items())

def update_details():
        emp_name = input("Enter name : ")
        update_what = input("update hours or wage per hour ?")
        
        if update_what == "hours" :
            for x,y in employees.items() :
                name = y.get("name")
                if name == emp_name :
                    worked = int(input("Enter hours worked : "))  
                    employees[x].update({"hours worked" : worked})
                    print(employees[x].values())  
                
                   
        elif  update_what == "wage" :
            for x,y in employees.items() :
                name = y.get("name")
                if name == emp_name :
                    wage = int(input("Enter wage per hour : ")) 
                    employees[x].update({"hourly wage" : wage})
                    print(employees[x].values())    
          
                   
     

def display ():
    for x,y in employees.items():
       print(employees[x].values())
  
bonus = 10000
def check_overtime_give_bonus():
    for x,y in employees.items():
        working_hrs = y.get("hours worked")
        if working_hrs >40 : 
             overall_pay= working_hrs + bonus
             employees[x].update({"payroll": overall_pay, "bonus" : "applied bonus" })
        else :
            employees[x].update({"bonus" : "no bonus" })
    
      
print("Operations : \n 1. Add emp \n2. Update emp \n3.Display employees \n4. Calculate payment of an emp \n5. Check payroll of all emps \n6. Check overtime and give bonus ")

flag = 1 

while flag :
    
    op = int(input("enter operation : "))
    
    if op == 1:
        add_emp()
    elif op == 2:
        update_details()
    elif op == 3:
        display()
    elif op == 4:
        emp_name = input("enter the emp name : ")
        for x,y in employees.items():
            name = y.get("name")
            if name == emp_name :
                hr = y.get("hours worked")
                wg = y.get("hourly wage")
                pay = calculate(hr,wg)
        print(f"the total payment of the {emp_name} is ", pay)
    elif op == 5:
            total_payroll()
    elif op == 6:
            check_overtime_give_bonus()  
            display()
              
    cont =input("do you want to continue : ")
    if  cont == 'y' or cont=='Y' :
        flag = 1
    else :
        flag = 0