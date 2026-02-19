# import admin adn user models
from library.models import Admin ,User
class AuthServices:
    def __init__(self):
        self.users = {} 
        self.current_user = None 
    # Register User
    def RegisterUser(self, username:str, email:str, password:str):
        new_user_id=len(self.users)+1
        user_obj = User(user_id=new_user_id, username=username, email=email, password=password)
        self.users[new_user_id] = user_obj
        return f"Hello {username} registered successfully"
    # Register Admin    
    def RegisterAdmin(self, username:str, email:str, password:str):
        new_admin_id=len(self.users)+1
        admin_obj = Admin(user_id=new_admin_id, username=username, email=email, password=password)
        self.users[new_admin_id] = admin_obj
        return f"Hello {username} registered successfully"
    # Login user 
    def login(self,user_id,password):
        #check weather the user existes or not
        if user_id in self.users:
            user_obj: User = self.users[user_id]
            # check password o 
            if not user_obj.login_auth(password) == password:
                return "Invalid password"
            else:
                return True, f"Hello {user_obj.username} logged in successfully"
        else:
            return False, "User not found"
    # Login admin
    # Logout user/admin
