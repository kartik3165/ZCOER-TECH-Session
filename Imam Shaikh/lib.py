
lib = {
    "rich dad poor dad": {"author": "Robert kiyosaki", "year": 2000, "status": "available"},
    "How to win an influence": {"author": "Dale Carnegie", "year": 2004, "status": "available"},
    "Elon Musk": {"author": "Walter Issacson", "year": 2002, "status": "available"},
    "Benjamin Franklen": {"author": "Walter Issacson", "year": 2003, "status": "available"},
}

# Update library
def update_book(b, c, d, e):
    lib.update({b: {"author": c, "year": d, "status": e}})
    return lib

def borrowed_book(b, c, d, e="not available"):
    lib.update({b: {"author": c, "year": d, "status": e}})
    return lib

def search_book(b):
    M=lib.get(b)
    return M    

print("---------------------------------------------------")
print("Enter the below information to update list:")
print("---------------------------------------------------")

while True:
    b = str(input("Enter the title of the book:"))
    c = str(input("Enter the name of the author:"))
    d = int(input("Enter the year of publication:"))
    e = str(input("Enter the status of the book (available/not available):"))
    g = int(input("Enter 1 to update and 2 to borrow and 3 for search:"))
    
    if g == 1:
        s=update_book(b, c, d, e)
        print("---------------------------------------------------")
        print(s)
    elif g == 2:
       t= borrowed_book(b, c, d)
       print("---------------------------------------------------")
       print(t)
    elif g == 3:
        z= search_book(b)
        print("---------------------------------------------------")
        print(z)
    else:
        print("Invalid option! Please enter 1 or 2 or 3.")



