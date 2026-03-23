from Database.connection import DatabaseConfig
class CreateAccount:
    def __init__(self,name,email,password,phone,balance):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.balance = balance
    def create_new_account(self):
        try:    
            db_config=DatabaseConfig()
            cursor=db.config.cursor()
            check_user_query="""select * from users where email=%s"""
            cursor.execute(check_user_query,(self.email,))
            if cursor.fetchone():
                return "User already exists"
            else:
                _user_query="""insert into users (name,email,phone) values (%s,%s,%s)"""
                cursor.execute(insert_user_query,(self.name,self.email,self.password,self.phone))
                db_config.commit()
                get_accountNO_query="""select * from users where email=%s"""
                cursor.execute(get_accountNO_query,(self.email,))
                account_number= cursor.fetchone()[0]
                return "User created successfully and account number is {account_number}"
            #adding password,balance to the  account 
            query="""insert into accounts (account,password,balance) values (%s,%s,%s)"""
            cursor.execute(query,(account_number,self.password,self.balance))
            cursor.execute(add_transaction_query,(account_number,"credit",self.balance))
            db_config.commit()
            cursor.close()
            db_config.close()
        except Exception as e:
            return f"Something wrong in bank/Register.py: {e}"
    def __str__(self):
        return f"{self.name} {self.email} {self.phone}"
    