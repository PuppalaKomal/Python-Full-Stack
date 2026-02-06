class User:
    def __init__(self,email:str,username:str,password:str):
        self.email=email
        self.username=username
        self.password=password
    def Details(self):
        return f"Username is {self.username} and email is {self.email}"  
class Admin:
    def __init__(self,email:str,username:str,password:str):
        self.email=email
        self.username=username
        self.password=password
    def Details(self):
        return f"Username is {self.username} and email is {self.email}"
    def total_income(self,income):
        return f" My income is: {income}"
    def Total_users(self,users_count):
        return f" I am a Admin and My total users are: {users_count}"
user1=User("abc@gmail.com","abc","abcd")
print("User details are: ",user1.Details())
admin1=Admin("def@gmail.com","def","defh")
print("Admin details are: ",admin1.Details())
print("Admin total Income is: ",admin1.total_income(1000000))
print(user1.username)
print(admin1.username)

# Inheritance
    #getting properties and behaviours of the parent class(User) to the child class(Admin)

#parent class implementation without child class implementation
class User():
    def __init__(self,email:str,username:str,password:str):
        self.email=email
        self.username=username
        self.password=password
    def Details(self):
        return f"Username is {self.username} and email is {self.email}"    
class Admin(User):
    pass
    # def __init__(self,email:str,username:str,password:str):
    #     self.email=email
    #     self.username=username
    #     self.password=password
    # def Details(self):
    #     return f"Username is {self.username} and email is {self.email}"
    # def total_income(self,income):
    #     return f" My income is: {income}"
    # def Total_users(self,users_count):
    #     return f" I am a Admin and My total users are: {users_count}"
user1=User("abc@gmail.com","abc","abcd")
print("User details are: ",user1.Details())
admin1=Admin("def@gmail.com","def","defh")
print("Admin details are: ",admin1.Details())
# print("Admin total Income is: ",admin1.total_income(1000000))
print(user1.username)
print(admin1.username)


class User():
    def __init__(self,email:str,username:str,password:str,age:int):
        self.email=email
        self.username=username
        self.password=password
        self.age=age
    def Details(self):
        return f"Username is {self.username} email is {self.email} and my age is {self.age}"
    
class Admin(User):
    pass
    def __init__(self,email:str,username:str,password:str,total_users:int):
        self.email=email
        self.username=username
        self.password=password
        self.total_users=total_users       
    # def Details(self):
    #     return f"Username is {self.username} and email is {self.email}"
    # def total_income(self,income):
    #     return f" My income is: {income}"
    def users(self,total_users):
        return f" I am a Admin and My total users are: {total_users}"
user1=User("abc@gmail.com","abc","abcd",30)
print("User details are: ",user1.Details())
admin1=Admin("def@gmail.com","def","defh",10)
admin1.age=10
print("Admin details are: ",admin1.Details())
print(admin1.users(10))
admin1.age=10
# print("Admin total Income is: ",admin1.total_income(1000000))
print(user1.username)
print(admin1.username)

# super()
class User():
    def __init__(self,email:str,username:str,password:str):
        self.email=email
        self.username=username
        self.password=password
    def Details(self):
        return f"Username is {self.username} email is {self.email}"
    
class Admin(User):
    pass
    def __init__(self,email:str,username:str,password:str,total_users:int):
        super().__init__(username,email,password)    
    # def Details(self):
    #     return f"Username is {self.username} and email is {self.email}"
    # def total_income(self,income):
    #     return f" My income is: {income}"
    def users(self,total_users):
        return f" I am a Admin and My total users are: {total_users}"
user1=User("abc@gmail.com","abc","abcd")
print("User details are: ",user1.Details())
admin1=Admin("def@gmail.com","def","defh",10)
admin1.age=10
print("Admin details are: ",admin1.Details())
print(admin1.users(10))
admin1.age=10
# print("Admin total Income is: ",admin1.total_income(1000000))
print(user1.username)
print(admin1.username)
