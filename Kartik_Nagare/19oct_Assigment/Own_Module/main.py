import tableGenerator

print("<==== Table Genrator ====>")

while True:
    num = int(input("Enter number you want to generate table : "))
    print(tableGenerator.table().number(num))