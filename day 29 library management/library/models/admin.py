# import user class
from library.models.user import User

# create aadmin class
class Admin(User):
    def __init__(self, userid ,password ,email ,name):
        super.__init__(userid ,password ,email ,name)
        self.role="Admin"
    # manage_books
    def manage_books(self):
        return True