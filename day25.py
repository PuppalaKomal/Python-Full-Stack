# Books and users
from ast import main
from day23 import User


books = {
    1: ["Python Basics", "Guido van Rossum", 10],
    2: ["Learning Java", "James Gosling", 8],
    3: ["C Programming", "Dennis Ritchie", 12],
    4: ["C++ Primer", "Bjarne Stroustrup", 7],
    5: ["Data Structures", "Mark Allen Weiss", 9],
    6: ["Algorithms", "Robert Sedgewick", 6],
    7: ["Operating Systems", "Abraham Silberschatz", 5],
    8: ["Computer Networks", "Andrew S. Tanenbaum", 11],
    9: ["Database Systems", "Raghu Ramakrishnan", 10],
    10: ["Software Engineering", "Ian Sommerville", 8],

    11: ["Web Development", "Jon Duckett", 15],
    12: ["HTML & CSS", "Jon Duckett", 14],
    13: ["JavaScript Guide", "Douglas Crockford", 9],
    14: ["React Explained", "Zac Gordon", 6],
    15: ["Node.js Essentials", "Ethan Brown", 7],
    16: ["Django for Beginners", "William Vincent", 8],
    17: ["Flask Web Dev", "Miguel Grinberg", 10],
    18: ["Full Stack Python", "Matt Makai", 5],
    19: ["PHP Basics", "Rasmus Lerdorf", 12],
    20: ["Laravel Up & Running", "Matt Stauffer", 6],

    21: ["Machine Learning", "Tom Mitchell", 4],
    22: ["Deep Learning", "Ian Goodfellow", 3],
    23: ["AI Basics", "Stuart Russell", 6],
    24: ["Data Science Handbook", "Jake VanderPlas", 8],
    25: ["Statistics for Data Science", "Peter Bruce", 9],
    26: ["Pandas in Action", "Boris Paskhaver", 7],
    27: ["NumPy Guide", "Travis Oliphant", 10],
    28: ["TensorFlow Basics", "Martin Görner", 5],
    29: ["PyTorch Essentials", "Soumith Chintala", 6],
    30: ["ML with Python", "Sebastian Raschka", 7],

    31: ["Cloud Computing", "Rajkumar Buyya", 9],
    32: ["AWS Fundamentals", "Ben Piper", 8],
    33: ["Azure Basics", "Scott Duffy", 6],
    34: ["Google Cloud Guide", "Dan Sullivan", 5],
    35: ["DevOps Handbook", "Gene Kim", 7],
    36: ["Docker Deep Dive", "Nigel Poulton", 10],
    37: ["Kubernetes Guide", "Kelsey Hightower", 6],
    38: ["CI/CD Pipelines", "Jez Humble", 4],
    39: ["Linux Basics", "Brian Ward", 12],
    40: ["Unix Power Tools", "Jerry Peek", 8],

    41: ["Cyber Security", "William Stallings", 6],
    42: ["Ethical Hacking", "Kevin Mitnick", 9],
    43: ["Network Security", "Charlie Kaufman", 7],
    44: ["Cryptography", "Bruce Schneier", 5],
    45: ["Malware Analysis", "Michael Sikorski", 3],
    46: ["Digital Forensics", "Eoghan Casey", 4],
    47: ["Penetration Testing", "Georgia Weidman", 6],
    48: ["Security Operations", "Chris Sanders", 8],
    49: ["Web App Security", "Andrew Hoffman", 7],
    50: ["SOC Analyst Guide", "Joseph Muniz", 5],

    51: ["Agile Project Management", "Ken Schwaber", 10],
    52: ["Scrum Guide", "Jeff Sutherland", 12],
    53: ["Kanban Explained", "David Anderson", 9],
    54: ["Product Management", "Marty Cagan", 6],
    55: ["Business Analysis", "Debra Paul", 8],
    56: ["IT Service Management", "Jan Van Bon", 5],
    57: ["ITIL Foundation", "Axelos", 7],
    58: ["System Design", "Alex Xu", 6],
    59: ["Clean Code", "Robert C. Martin", 11],
    60: ["Refactoring", "Martin Fowler", 8],

    61: ["Design Patterns", "Erich Gamma", 9],
    62: ["Object-Oriented Design", "Grady Booch", 6],
    63: ["UML Distilled", "Martin Fowler", 7],
    64: ["Microservices", "Sam Newman", 5],
    65: ["REST APIs", "Leonard Richardson", 8],
    66: ["GraphQL Guide", "Eve Porcello", 6],
    67: ["System Architecture", "Len Bass", 4],
    68: ["Enterprise Java", "Rod Johnson", 7],
    69: ["Spring Boot", "Craig Walls", 9],
    70: ["Hibernate Basics", "Gavin King", 6],

    71: ["Mobile App Development", "Chris Griffith", 8],
    72: ["Android Programming", "Big Nerd Ranch", 10],
    73: ["iOS Development", "Paul Hudson", 7],
    74: ["Flutter Guide", "Eric Windmill", 6],
    75: ["React Native", "Nader Dabit", 5],
    76: ["Kotlin in Action", "Dmitry Jemerov", 7],
    77: ["Swift Programming", "Chris Lattner", 6],
    78: ["UI/UX Design", "Don Norman", 9],
    79: ["Human Computer Interaction", "Alan Dix", 4],
    80: ["Design Thinking", "Tim Brown", 8],

    81: ["Big Data Analytics", "Viktor Mayer-Schonberger", 5],
    82: ["Hadoop Guide", "Tom White", 6],
    83: ["Spark in Action", "Jean-Georges Perrin", 7],
    84: ["Kafka Essentials", "Neha Narkhede", 4],
    85: ["Data Warehousing", "Ralph Kimball", 6],
    86: ["ETL Processes", "Rick Sherman", 5],
    87: ["SQL Mastery", "Alan Beaulieu", 12],
    88: ["NoSQL Databases", "Pramod Sadalage", 7],
    89: ["MongoDB Basics", "Kristina Chodorow", 8],
    90: ["Redis Guide", "Salvatore Sanfilippo", 4],

    91: ["Blockchain Basics", "Don Tapscott", 6],
    92: ["Ethereum Guide", "Vitalik Buterin", 5],
    93: ["Smart Contracts", "Andreas Antonopoulos", 4],
    94: ["FinTech Essentials", "Susanne Chishti", 7],
    95: ["Digital Payments", "Chris Skinner", 6],
    96: ["E-commerce Systems", "Gary Schneider", 8],
    97: ["Supply Chain IT", "Sunil Chopra", 5],
    98: ["ERP Systems", "Monk & Wagner", 6],
    99: ["CRM Software", "Paul Greenberg", 7],
    100: ["IT Governance", "Peter Weill", 4]
}

users={
    1001:{"name":"komal","books_id":[91,99,87]},
    1002:{"name":"Dhanush","books_id":[92,100,86]},
    1003:{"name":"Siri","books_id":[91,99,87]}
}
# Person Class
class Person():
    # Constructor
    def __init__(self,id:int,name:str):
        self.id=id
        self.name=name
# Book Class
class Book():
    # constructor
    def __init__(self,id:int,name:str,author:str):
        self.id=id
        self.name=name
        self.author=author
#  Users Class        
class Users(Person):
    #Constructors
    def __init__(self,id:int,name:str,borrowed_books:list):
        super().__init__(id,name)
        self.borrowed_books=borrowed_books
        pass
# Admin Class
class Admin(Person):
    #constructor
    def __init__(self,id:int,name:str):
        super().__init__(id,name)
    def add_Book(self,book_obj:Book,quantity:int):
        if book_obj.id not in books:
            books[book_obj.id]={"name":book_obj.name,"author":book_obj.author,"quantity":quantity}
            return f"{book_obj.name} added successfully."
        else:
            return f"{book_obj.name} already exists."
    def add_user(self,user_obj:User):
        if user_obj.id not in users:
            users[user_obj.id]={"name":user_obj.name,"books_id":[]}
            return f"{user_obj.name} added successfully."
        else:
            return f"{user_obj.name} already exists."
    def delete_book(self,bookid):
        if bookid in books:
            books.pop(bookid)
            return f"{bookid} deleted successfully."
        else:
            return f"{bookid} does not exist."
    def borrow_book(self,userid,*bookids):
        if userid in users:
            available_books=[]
            unavailable_books=[]
            for bookid in bookids:
                if bookid in books:
                    quantity=books[bookids][2]
                    if quantity>0:
                        books[bookid][2]-=1
                        users[userid]["book_id"].append(bookid)
                        available_books.append({bookid:books[bookid[0]]})
                    else:
                        unavailable_books.append({bookid:books[bookid[0]]})
                else:
                    unavailable_books.append({bookid:books[bookid[0]]})
            return f"Availble books are : {available_books} and unavailable books are: {unavailable_books}"
        return f"User not found"
    def return_book(self,userid,*bookids):
        if userid in users:

            for bookid in bookids:
                if bookid in books and users[userid]['books_id']:

                    books[bookid][2]+=1
                    users[userid]["book_id"].remove(bookid)
            return f"All books are returned successfully!" 
        return f"User not found"
    def all_book(self):
        return books
    def total_users(self):
        return len(users)
if __name__ == "__main__":
    print("Welcome to Library! ")
    admin=Admin(1,"Suma")
    while True:
        print("Select Your Operations:\n 1. Add Book \n 2. Register User \n 3. Borrow Book \n 4. Return Book \n 5. Display All Books \n 6. Display Total Users \n 7. Delete book \n 8. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            bookid=int(input("Enter book id: "))
            book_name=input("Enter Book name: ")
            book_author=input("Enter Author name: ")
            stock=int(input("Enter book quantity: "))
            book_object=Book(id=book_id,name=book_name,author=book_author) 
            admin.add_Book(book_obj=book_object,quantity=stock)
        if choice==2:
            userid=int(input("Enter User Id: "))
            username=input("Enter Username: ")
            user_object=User(id=userid,name=username)
            print(admin.add_user(user_obj=user_object))
        elif choice==3:
            print("You selected borrow book choose book of your desire")
            userid=int(input("Enter User id: "))
            book_ids=list(map(int,input("Enter book ids: ").split()))
            print(admin.borrow_book(userid,*book_ids))
        elif choice==4:
            print("You selected return book choose book of your desire")
            userid=int(input("Enter User id: "))
            book_ids=list(map(int,input("Enter book ids: ").split()))
            print(admin.return_book(userid,*book_ids))
        elif choice==5:
            print("You have chose to view the books available ")
            print(f"book_id        |Book name:                  |,Author:         |,Quantity:       ")
            all_books=admin.all_book()
            for bookid,details in all_books.items():
                print(f"Book id: {bookid} | Book name: {details[0]} | Author: {details[1]} |  Quantity: {details[2]}")
            # print(admin.all_book())
        elif choice==6:
            print("Total users in library are:")
            print(admin.total_users())
        elif choice==7:
            print("You have chose to delete a book")
            bookid=int(input("Enter book id to delete book : "))
            print(admin.delete_book(bookid=bookid))  
        elif choice==8:
            print("Thank you for using library management system")
            break
        else:
            print("Invalid choice")
