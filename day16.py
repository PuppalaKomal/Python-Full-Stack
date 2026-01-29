"""#dictionary
details={"name":"komal","batch":"PFS47","course":"python"}
print(type(details))
print(details)

##accessing the values in dictionary
details={"name":"komal","batch":"PFS47","course":"python"}
print(details["name"])

##updating the dictionary values and items
details={"name":"komal","batch":"PFS47","course":"python"}
details["name"]="Komal Puppala"
print(details)

##adding new key value pair
##dict_object[key]=value
details={"name":"komal","batch":"PFS47","course":"python"}
details["age"]=18
print(details)

##removing the key value pair
##dict_object.pop(key)
details={"name":"komal","batch":"PFS47","course":"python"}
details.pop("course")
print(details)
 
#dictionary funtions
    #accessing values
    #get(key,default_value):it returns value if key is present in dictionary otherwise returns default value

details={"name":"komal","batch":"PFS47","course":"python"}
print(details.get("name"))
print(details.get("age",18))

#adding or updating items to dictionary
#update(dictionary):it adds or updates the key value pair in dictionary
details={"name":"komal","batch":"PFS47","course":"python","percentage":80}
marks={"python":90,"softskills":80,"aptitude":70,"percentage":80}
details.update(marks)
print(details)
print(marks)

#dictionary doesnt allows duplicates
details={"name":"komal","batch":"PFS47","course":"python","percentage":80,"percentage":90}
print(details)

#get dictionary keys and values
#keys()-It returns list of all dictinory keys
#values()-It returns list of all dictionary values
#items()-It returns all dictionary items as list of tuples of key value pairs
details={"name":"komal","batch":"PFS47","course":"python","percentage":80,"percentage":90}
print(details.keys())
print(details.values())
print(details.items())
print(type(details.keys()))
print(type(details.values()))
print(type(details.items()))

#deleting items form dictionary
#del dict_object[key]
#pop(key,default_value) : it removes the key value pair from dictionary
#popitems 
details={"name":"komal","batch":"PFS47","course":"python","percentage":80}
poped_value=details.pop("course")
print(poped_value)
print(details)
poped_value=details.pop("course",None)
print(poped_value)
del details["batch"]
print(details)

#len()
details={"name":"komal","batch":"PFS47","course":"python","percentage":80}
len(details)

#iterate dictionary iems
details={"name":"komal","batch":"PFS47","course":"python","percentage":80}
for item in details.items():
    print(f"{item[0]}:{item[1]}")

details={"name":"komal","batch":"PFS47","course":"python","percentage":80}
for key,value in details.items():
    print(f"{key}:{value}")
    
#membership checking
details={"name":"komal","batch":"PFS47","course":"python","percentage":80}
key="name"
if key in details:
    print("key is present ")
else:
    print("key is not present")"""

#-Phone book project
# CRUD Operations
#print all contacts(name, number)

#creating phone book
ph_book={}
def add_contact(name:str,number:int):
    #check names exists in phone book 
    if name not in ph_book:
        ph_book[name]=number
        print(f"{name} Contact Saved")
    else:
        print(f"{name} Contact Already Exists")
#update mob number in ph_book
def update_number(name:str,number:int):
    if name in ph_book:
        ph_book[name]=number
        #ph_book.update({name:number})
        print(f"{name} Contact Number Successfully Updated")
    else:
        print(f"{name} Contact Not Found")
#delete contact from ph_book
def delete_contact(name:str):
    if name in ph_book:
        del ph_book[name]
        #ph_book.pop(name)
        print(f"{name} Contact Successfully Deleted")
    else:
        print(f"{name} Contact Not Found")
#get contact number by name
def get_contact(name:str):
    if name in ph_book:
        print(f"{name} Contact Number is: {ph_book[name]}")
    else:
        print(f"{name} Contact Not Found")
    #number=ph_book.get(name,"Contact Not Found")
    #print("the contact number is: ",number)
# print all contacts(name, number)
def print_contacts():
    if len(ph_book)==0:
        print("Phone Book is Empty")
    else:
        print("Phone Book Contacts:")
        for name,number in ph_book.items():
            print(f"{name}:{number}")
if __name__=="__main__":
    print("Welcome to Phone Book App")
    while True:
        print("\n1. Add Contact\n2. Update Contact\n3. Delete Contact\n4. Get Contact\n5. Print Contacts\n6. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            name=input("Enter name: ")
            number=int(input("Enter number: "))
            add_contact(name,number)
        elif choice==2:
            name=input("Enter name: ")
            number=int(input("Enter number: "))
            update_number(name,number)
        elif choice==3:
            name=input("Enter name: ")
            delete_contact(name)
        elif choice==4:
            name=input("Enter name: ")
            get_contact(name)
        elif choice==5:
            print_contacts()
        elif choice==6:
            print("Thank you for using Phone Book App")
            break
        else:
            print("Invalid choice")  # Added missing space after "Invalid"
        




