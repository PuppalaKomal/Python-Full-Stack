# Online shopping cart
# create a class Product with:
#     attribute:name,price
#     method:get_details() ->return product details
#     create another class shopping cart:
#         attributes:list of products:
#         method:add_product(Product)
#         method:total_price()->return total price of products in cart
#         create 3 products and add them to the cart and print the total bill
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"{self.name} - ${self.price}"
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        return sum(product.price for product in self.products)

# Create products
product1 = Product("Laptop", 1000)
product2 = Product("Mouse", 25)
product3 = Product("Keyboard", 50)

# Create shopping cart and add products
cart = ShoppingCart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

# Print total bill
print("Total bill:", cart.total_price())

# Bank account with encapsulation:
#     create a class BankAccount with:
#     attributes:account_number,__balance
#     methods:deposit(amount),withdraw(amount),get_balance()
#     deposit 5000 and withdraw 2000 and print the balance
    
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited ${amount}. New balance: ${self.__balance}"

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        return f"Withdrew {amount}. New balance: ${self.__balance}"

    def get_balance(self):
        return self.__balance
# Create a bank account and deposit and withdraw some amounts
account = BankAccount("1234567890")
account.deposit(5000)
account.withdraw(2000)
print("Current balance:", account.get_balance())
