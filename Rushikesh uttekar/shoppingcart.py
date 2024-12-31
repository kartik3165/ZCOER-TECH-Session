prod = [] 


cost = 0
m=int(input("enter no of items : "))

for i in range (m):
    n = input("enter item name: ")
    q = int(input("enter item quantity: "))
    c = int(input("enter item cost: "))
    p =(n , q, c)
    prod.append(p)
    
    cost +=c
    
print() 
print(prod)
print() 

print("total cost of cart ", cost)


print() 

item = input("enter item name to be deleted : ")
for i in prod :
    for j in i : 
        if j == item :
           prod.remove(i)
           price = i[2]
           cost-=price
           print("now cart price is ", cost)

print(prod)
 
print() 
if cost >100:
    dis = cost*0.1
    cost-=dis
    print("cost after discount",cost)
elif 50<= cost <=100:
    dis = cost*0.5
    cost-=dis
    print("cost after discount",cost)
elif cost<50:
    print("no discount")