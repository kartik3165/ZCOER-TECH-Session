def generate_table(number, upto):
    for i in range(1, upto + 1):
        print(f"{number} x {i} = {number * i}")

while True:
    user_input = input("Enter a number to generate its multiplication table (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    
    try:
        number = int(user_input)
        print(f"\nMultiplication table for {number}:\n")
        generate_table(number, 10)
        
        print("\nMultiplication tables from 1 to 10:\n")
        for i in range(1, 11):
            generate_table(i, 10)
    
    except ValueError:
        print("Please enter a valid number.")
