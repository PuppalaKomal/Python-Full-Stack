# create user class
class User:
    def __init__(self, userid:int, email:str, password:str, name:str):
        self.userid=userid
        self.password=password
        self.email=email
        self.name=name
        self.role="user"
        self.is_active=True
        
    # display user details
    def display_setails(self):
        user={}
        user["userid"]=self.userid
        user["email"]=self.email
        user["role"]=self.role 
        # user["is_active"]=self.is_active
        return user
    # can manage books
    def manage_books(self):
        return False
    # login check
    def login_auth(self,password):
        return self.password==password
           
    