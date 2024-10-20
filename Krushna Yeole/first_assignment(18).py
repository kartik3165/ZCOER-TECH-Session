library = {
    "book1": {"title": "Limitless", "author": "Jim Kwik", "year": 1960, "status": "available"},
    "book2": {"title": "Death on the Nile", "author": "Agatha Christie", "year": 1970, "status": "available"},
    "book3": {"title": "Murder on the Orient Express", "author": "Agatha Christie", "year": 1980, "status": "available"}
}

def add_book():
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    year = int(input("Enter Year: "))
    library[f"book{len(library) + 1}"] = {"title": title, "author": author, "year": year, "status": "available"}
    print("Book added!")

def borrow_book():
    title = input("Enter the book title: ")
    for book in library.values():
        if book["title"].lower() == title.lower() and book["status"] == "available":
            book["status"] = "not available"
            print("You borrowed:", book["title"])
            return
    print("Book not found or already borrowed.")

def return_book():
    title = input("Enter the book title: ")
    for book in library.values():
        if book["title"].lower() == title.lower():
            book["status"] = "available"
            print("You returned:", book["title"])
            return
    print("Book not found.")

def display_books():
    for book in library.values():
        print(book)

def search_book():
    search_term = input("Enter book title or author: ")
    for book in library.values():
        if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower():
            print(book)

while True:
    print("\nOptions: 1. Add Book  2. Borrow Book  3. Return Book  4. Display Books  5. Search Book")
    option = int(input("Choose an option: "))
    
    if option == 1:
        add_book()
    elif option == 2:
        borrow_book()
    elif option == 3:
        return_book()
    elif option == 4:
        display_books()
    elif option == 5:
        search_book()
    else:
        print("Invalid option.")

    if input("Continue? (y/n): ").lower() != 'y':
        break
