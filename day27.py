# Write a progam to:
#   1.store student marks using a dictionary
#   2.accept student name as input
#   3.handle the missing student using exception handling

# write a program to :
#    1.accept two sets of integers from user
#    2.display the union, intersection, difference of the set

# write a program to:
#    1.read a file named data.txt
#    2.count number of lines 
#    3.handle file not found safely

# write a program to:
#    1.store book details in a dictionary
#    2.save them in a JSON file
#    3.read back ad display the contents


# Write a progam to:
#   1.store student marks using a dictionary
#   2.accept student name as input
#   3.handle the missing student using exception handling
student_marks = {"John": 85, "Emma": 92, "Mike": 78, "Sara": 95} 
try:
    name = input("Enter student name: ")
    marks = student_marks[name]
    print(f"{name} got {marks} in the exam.")
except KeyError:
    print("Student not found. Please enter a valid name.")

# write a program to :
#    1.accept two sets of integers from user
#    2.display the union, intersection, difference of the set
set1 = set(map(int, input("Enter elements for set 1 separated by space: ").split()))
set2 = set(map(int, input("Enter elements for set 2 separated by space: ").split()))

print("Union of sets:", set1.union(set2))
print("Intersection of sets:", set1.intersection(set2))
print("Difference of sets (set1 - set2):", set1.difference(set2))

# write a program to:
#    1.read a file named data.txt
#    2.count number of lines 
#    3.handle file not found safely
try:
    with open("data.txt", "r") as file:
        lines = file.readlines()
        print("Number of lines:", len(lines))
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")

# write a program to:
#    1.store book details in a dictionary
#    2.save them in a JSON file
#    3.read back ad display the contents
import json
books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
]
with open("books.json", "w") as file:
    json.dump(books, file, indent=4)
with open("books.json", "r") as file:
    data = json.load(file)
    print(data)
