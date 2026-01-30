# Book Management System using Set and Dictionary

# set: stores unique book IDs
book_ids = set()

# dictionary: stores book details with book_id as key
# value will be another dictionary
book_details = {}

while True:
    print("\nWelcome to Book Management System")
    print("1. Add book")
    print("2. Delete book")
    print("3. Total books")
    print("4. All books")
    print("5. Borrow book")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add book
    if choice == 1:
        book_id = input("Enter book ID: ")

        if book_id in book_ids:
            print("Book ID already exists!")
        else:
            book_name = input("Enter book name: ")
            author = input("Enter book author: ")
            year = input("Enter year of publish: ")

            book_ids.add(book_id)
            book_details[book_id] = {
                "name": book_name,
                "author": author,
                "year": year,
                "status": "Available"
            }

            print("Book added successfully!")

    # 2. Delete book
    elif choice == 2:
        book_id = input("Enter book ID to delete: ")

        if book_id in book_ids:
            book_ids.remove(book_id)
            del book_details[book_id]
            print("Book deleted successfully!")
        else:
            print("Book ID not found!")

    # 3. Total books
    elif choice == 3:
        print("Total books:", len(book_ids))

    # 4. All books
    elif choice == 4:
        if not book_details:
            print("No books available.")
        else:
            for bid, details in book_details.items():
                print(f"\nBook ID: {bid}")
                print("Name:", details["name"])
                print("Author:", details["author"])
                print("Year:", details["year"])
                print("Status:", details["status"])

    # 5. Borrow book
    elif choice == 5:
        book_id = input("Enter book ID to borrow: ")

        if book_id in book_ids:
            if book_details[book_id]["status"] == "Available":
                book_details[book_id]["status"] = "Borrowed"
                print("Book borrowed successfully!")
            else:
                print("Book is already borrowed!")
        else:
            print("Book ID not found!")

    # 6. Exit
    elif choice == 6:
        print("Thank you for using Book Management System")
        print("Have a nice day 😊")
        break

    else:
        print("Invalid choice! Please try again.")
