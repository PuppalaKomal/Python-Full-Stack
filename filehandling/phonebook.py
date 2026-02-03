
def add_contact(name:str,number:int):
    #check names exists in phone book
    #get file contacts
    try:
        with open("contacts.txt","r") as f:
            contact_lines=f.readlines()
    except :
        return "Error in add_contact"
    for contact in contact_lines:
        contact_name, contact_number=contact.split() 
        if contact_name==name:
            return "Contact Already Exists"
    #add contact to file contacts
    try:
        with open("contacts.txt","a") as f:
            f.write(f"\n{name} {number}")
            return "{name}'s contact has been updated"
    except :
        return "Error in add_contact" 
no=99631246
name="koaml"
print(add_contact(name,no))
            
# #update mob number in ph_book
def update_number(name:str,new_number:int):
    if name in ph_book:
        ph_book[name]=number
        #ph_book.update({name:number})
        print(f"{name} Contact Number Successfully Updated")
    else:
        print(f"{name} Contact Not Found")
# #delete contact from ph_book
# def delete_contact(name:str):
#     if name in ph_book:
#         del ph_book[name]
#         #ph_book.pop(name)
#         print(f"{name} Contact Successfully Deleted")
#     else:
#         print(f"{name} Contact Not Found")
# #get contact number by name
# def get_contact(name:str):
#     if name in ph_book:
#         print(f"{name} Contact Number is: {ph_book[name]}")
#     else:
#         print(f"{name} Contact Not Found")
#     #number=ph_book.get(name,"Contact Not Found")
#     #print("the contact number is: ",number)
# # print all contacts(name, number)
# def print_contacts():
#     if len(ph_book)==0:
#         print("Phone Book is Empty")
#     else:
#         print("Phone Book Contacts:")
#         for name,number in ph_book.items():
#             print(f"{name}:{number}")
# if __name__=="__main__":
#     print("Welcome to Phone Book App")
#     while True:
#         print("\n1. Add Contact\n2. Update Contact\n3. Delete Contact\n4. Get Contact\n5. Print Contacts\n6. Exit")
#         choice=int(input("Enter your choice: "))
#         if choice==1:
#             name=input("Enter name: ")
#             number=int(input("Enter number: "))
#             add_contact(name,number)
#         elif choice==2:
#             name=input("Enter name: ")
#             number=int(input("Enter number: "))
#             update_number(name,number)
#         elif choice==3:
#             name=input("Enter name: ")
#             delete_contact(name)
#         elif choice==4:
#             name=input("Enter name: ")
#             get_contact(name)
#         elif choice==5:
#             print_contacts()
#         elif choice==6:
#             print("Thank you for using Phone Book App")
#             break
#         else:
#             print("Invalid choice")  
