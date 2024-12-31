emp = {
    "Karan": {"hour worked": 50, "hourly wage": 200},
    "Sumit": {"hour worked": 45, "hourly wage": 600},
    "Raj": {"hour worked": 56, "hourly wage": 300},
    "Benjamin Franklen": {"hour worked": 30, "hourly wage": 800},
}
def pay_roll(a,b):
    d= a*b
    return d

def update_employee(a,b,c):
    emp.update({a:{"hour worked": b, "hourly wage": c}})
    

def total_payroll():
    for x,y in emp.items():
        hrs =  y.get("hours worked")
        wages =  y.get("hourly wage") 
        payroll = pay_roll(hrs,wages)
        emp[x].update({"payroll" : payroll})
    print(emp.items()) 

def bonus_apply():
 for x,y in emp.items():
        
        if  y.get("hours worked")>40 : 
             overall_pay=  y.get("hours worked") + bonus
             emp[x].update({"payroll": overall_pay, "bonus" : "applied bonus" })
        else :
            emp[x].update({"bonus" : "no bonus" })

# display emp
print("---------------------------------------------------")
print("Enter the choice you want:")
print("1 for pay roll cal")
print("2 for upadate or add emplyees")
print("3 for total pay roll")
print("4 for bonus apply")
m= int(input("enter your choice:"))
print("---------------------------------------------------")
if(m==1):
    a= int(input("enter the hour he woks:"))
    b= int(input("enter the wage he have:"))
    x=pay_roll(a,b)
    print(x)
elif(m==2):
    d=str(input("enter the name you want to add or update:"))
    a= int(input("enter the hour he woks:"))
    b= int(input("enter the wage he have:"))
    h=update_employee(d,a,b)
    print("added or updated successfully")
    print(emp)
elif(m==3):
    total_payroll()

elif(m==4):
    bonus_apply()