from bank import CreateAccount, Login, Balance
from database import CreateTables






# main
if __name__ == "__main__":
    CreateTables
    print("Welcome to the Online banking")
    print("Select Your choice \n 1. Create New Account \n 2. Login")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        username = input("Enter Your name:")
        email = input("Enter your email:")
        ph = input("Enter Mobile number:")
        initial_deposite = int(input("Enter your initial deposite amount:"))
        password = input("Enter your new password:")
        create_account_obj = CreateAccount(name=username, 
                                           email=email, 
                                           phone=ph, 
                                           balance=initial_deposite, 
                                           password=password)
        print(create_account_obj.create_new_account())

    elif choice == 2:
        account = int(input("Enter your account number:"))
        password = input("Enter your password:")
        login_obj = Login(account=account, password=password)
        login_val = login_obj.login()
        while login_val == True:
            print(f"Welcome user {account}")
            print("Operations \n 1. Balance Enquiry " \
            "\n 2. Withdraw \n 3. Deposite \n 4. Transfer \n 5. Ministatement \n 6. Logout")
            choice = int(input("Enter your choice:"))
            if choice == 1:
                balance_obj = Balance(account=account)
                print(balance_obj.get_balance())
        if login_val == False:
            print("Check your Login credentials")
        else:
            print(login_val)