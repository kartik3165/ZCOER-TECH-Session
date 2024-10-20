cart = []
total_cost = 0
item_count = int(input("Enter number of items: "))

for _ in range(item_count):
    item_name = input("Enter item name: ")
    quantity = int(input("Enter item quantity: "))
    price = int(input("Enter item cost: "))
    cart.append((item_name, quantity, price))
    total_cost += price

print("\nCart contents:", cart)
print("Total cost:", total_cost)

item_to_remove = input("Enter item name to remove: ")
for item in cart:
    if item[0] == item_to_remove:
        cart.remove(item)
        total_cost -= item[2]
        print("Updated total cost:", total_cost)
        break

print("\nUpdated cart:", cart)

if total_cost > 100:
    discount = total_cost * 0.1
    total_cost -= discount
    print("Total after discount:", total_cost)
elif total_cost >= 50:
    discount = total_cost * 0.5
    total_cost -= discount
    print("Total after discount:", total_cost)
else:
    print("No discount applicable.")
