from bank import CreateAccount, Login
from database import CreateTables
if __name__ == "__main__":
    print("Welcome to the bank")
    print("select an option\n1. Create Account\n2. Login")
    choice = int(input())
    if choice == 1:
        username=input("Enter your username: ")
        email=input("Enter your email: ")
        phone=input("Enter your phone: ")
        initial_deposite=input("Enter your initial deposite amount: ")
        password=input("Enter your password: ")
        create_account_obj=CreateAccount(name=username,email=email,phone=phone,balance=initial_deposite,password=password)
    elif choice == 2:
        account=input(int("Enter your account number: "))
        password=input("Enter your password: ")
        login_obj=Login(account,password)
        login_val = login_obj.login()
        while login_val == True:
            print(f"Welcome user {account}")
            print("Operations\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Transfer\n5. Mini Statement\n6. logout")
        if login_val == False:
            print("Invalid credentials")
        else:
            print(login_val)
