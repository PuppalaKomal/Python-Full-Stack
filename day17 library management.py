"""#sets
    #empty set representation
        #s=set()
        #s1={}
    #read set of numbers
        #s=set(map(int,input("enter the numbers").split()))
    #read set of string
        #s=set(input("enter the string").split())
    #set operations
        #union
        #intersection
        #difference
        #symmetric difference
    #set checking operations    
        #subset
        #superset
        #disjoint
    #remove set of element
        #remove(element)
        #discard(element)
        #clear()
        #pop()
    #set dont allow duplicate elements
    #set is unordered    
s1={1,2,3,4,5,"hi",1,2,3,"e"}
print(s1)
    #set doesnt allow list as a element
s1={1,2,3,4,5,"hi",1,2,3,"e",[1,2,3,]}
    #set doesnt allow dictionary as a element
s1={1,2,3,4,5,"hi",1,2,3,e,[1,2,3,],{1:2,3:4}}

    #adding elements to set
        #add(element): it adds element to set is not in the set otherwise nothing
        #update(iterator): it adds multiple elements in iterator
s1={1,2,3,4}
s1.add(10)
s1.add(1)
print(s1)
s1.update([5,3,5])
print(s1)
    #removing element from set
        #remove(element): it removes element from set if element is not in the set then it shows error
        #discard(element): it removes element from set if element is not in the set then it shows nothing
        #clear(): it removes all elements from set
        #pop(): it removes random element from set
s1={1,2,3,4,5}
s1.remove(1)
print(s1)
s1.discard(2)
print(s1)
s1.pop()
print(s1)    #set operations
        #union
            #s1.union(s2): it returns union of s1 and s2
        #intersection
            #s1.intersection(s2): it returns intersection of s1 and s2
        #difference
            #s1.difference(s2): it returns difference of s1 and s2
        #symmetric difference
            #s1.symmetric_difference(s2): it returns symmetric difference of s1 and s2
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.union(s2)) # |
print(s1.intersection(s2)) # &
print(s1.difference(s2)) # -
print(s1.symmetric_difference(s2)) # ^"""


#small program
#book management using sets and dictionary
#set: it stores book reg number
#dictionary: it stores book and details information
#actions
    # 1. Add books
    # 2. Delete books
    # 3. Total books
    # 4. All books
    # 5. borrow book

# Book Management System using Set and Dictionary
# set: stores unique book IDs
book_ids = set()
# dictionary: stores book details with book_id as key
# value will be another dictionarybook_ids = set()
book_details = {}
def add_book():
    book_id = input("Enter book ID: ")
    if book_id in book_ids:
        print("Book ID already exists!")
        return
    book_details[book_id] = {
        "name": input("Enter book name: "),
        "author": input("Enter book author: "),
        "year": input("Enter year of publish: "),
        "status": "Available"
    }
    book_ids.add(book_id)
    print("Book added successfully!")
def delete_book():
    book_id = input("Enter book ID to delete: ")
    if book_id in book_ids:
        book_ids.remove(book_id)
        del book_details[book_id]
        print("Book deleted successfully!")
    else:
        print("Book ID not found!")
def total_books():
    print("Total books:", len(book_ids))
def display_books():
    if not book_details:
        print("No books available.")
        return
    for bid, details in book_details.items():
        print(f"\nBook ID: {bid}")
        print("Name:", details["name"])
        print("Author:", details["author"])
        print("Year:", details["year"])
        print("Status:", details["status"])
def borrow_book():
    book_id = input("Enter book ID to borrow: ")
    if book_id in book_ids:
        if book_details[book_id]["status"] == "Available":
            book_details[book_id]["status"] = "Borrowed"
            print("Book borrowed successfully!")
        else:
            print("Book already borrowed!")
    else:
        print("Book ID not found!")
def menu():
    print("\n1. Add book")
    print("2. Delete book")
    print("3. Total books")
    print("4. All books")
    print("5. Borrow book")
    print("6. Exit")
if __name__ == "__main__":
    while True:
        print("\nWelcome to Book Management System")
        menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_book()
        elif choice == 2:
            delete_book()
        elif choice == 3:
            total_books()
        elif choice == 4:
            display_books()
        elif choice == 5:
            borrow_book()
        elif choice == 6:
            print("Thank you for using Book Management System")
            break
        else:
            print("Invalid choice! Please try again.")


