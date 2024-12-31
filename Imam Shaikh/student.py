dic={"Gaurang":{"age":19,"marks":80},"Rushikesh":{"age":20,"marks":95},"Krishna":{"age":21,"marks":70}}
print("******Update the list of the student*****")
z=int(input("enter no. of student do you want to add:"))
for i in range(0,z):
     a=str(input("Enter the name:"))
     b=int(input("Enter the age:"))
     c=int(input("Enter the marks:"))
     dic.update({a:{"age":b,"marks":c}})

print(dic)
print("enter the below information to get the grades")
h=str(input("enter the name of student:"))
x=dic[h]["marks"]
if(x>=91 and x<=100):
    print("grade A")
elif(x>=81 and x<=90):
    print("grade B")
elif(x>=71 and x<=80):
    print("grade C")
elif(x>=35 and x<=70):
    print("grade D")
else:
     print("grade F")
    
