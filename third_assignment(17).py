users = {
    "u1": {"id": 1, "balance": 5000},
    "u2": {"id": 2, "balance": 3000},
    "u3": {"id": 3, "balance": 6000}
}

continue_flag = True

print("Operations: 1. Show balance\n2. Deposit\n3. Withdraw")

while continue_flag:
    operation = int(input("Enter operation number: "))
    user_id = int(input("Enter user ID: "))

    user_found = None
    for user in users.values():
        if user["id"] == user_id:
            user_found = user
            break

    if user_found:
        if operation == 1:
            print("Balance:", user_found["balance"])
        
        elif operation == 2:
            amount = int(input("Enter amount to deposit: "))
            user_found["balance"] += amount
            print("Updated balance:", user_found["balance"])
        
        elif operation == 3:
            withdraw_amount = int(input("Enter amount to withdraw: "))
            if withdraw_amount <= user_found["balance"]:
                user_found["balance"] -= withdraw_amount
                print("Updated balance:", user_found["balance"])
            else:
                print("Insufficient balance")
    else:
        print("User not found")

    cont = input("Do you want to continue? (y/n): ")
    continue_flag = cont.lower() == 'y'
