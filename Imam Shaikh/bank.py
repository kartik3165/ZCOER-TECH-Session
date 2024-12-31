a=int(input("enter the amount to withdraw:"))
b=3000;
print("Show the balance amount:")
print(b)
if(a<b):
    b=b-a
    print("withdraw successfully")
else:
    print("insufficient Fund")
print("current balance in account:")
print(b)