from Database.connection import DatabaseConfig  
class Login:
    def __init__(self,account:int, password:str):
        self.account = account
        self.password = password
    def login(self):
        try:
            db = DatabaseConfig()
            conn = db.connection()
            #Check weather account exists or not
            get_password_query = """SELECT password FROM users WHERE account = %s"""
            cursor.execute(get_password_query,(self.account,))
            db_password = cursor.fetchone()
            #check db and password
            if db_password and db_password[0] == self.password:
                return True
            else:
                return False
        except Exception as e:
            return f"Something wrong in bank/login.py: {e}"
