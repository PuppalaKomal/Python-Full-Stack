# Encapsulation
#  keep all attributes and methods in single unit that is class the main aim of encapsulation is to restrict the direct access of the class members(attributes and methods)
#  the restriction of access by using access modifiers:
#       1.public
#       2.protected (_)
#       3.private     (__)

class Bank():
    bank_name="Fraud Bank"
    def __init__(self,username,password,amount):
        self.username=username  #public
        self._password=password #protected 
        self.__amount=amount    #private
    def balance(self):
        return f"Current Balance is {self.__amount}"
    def withdraw(self,withdraw_amount):
        if self.__amount>=withdraw_amount:
            self.__amount>=withdraw_amount
            return f"{withdraw_amount} amount withdrew successfully and balance amount is {self.__amount}"
        return "Insufficient Balance"
    def deposite(self,deposite_amount): #public method
        self.__amount+=deposite_amount
        return f"{deposite_amount} amount deposited successfully and current balance is {self.__amount}"
    def __total_users(self): #private method
        return "Total users are 98"
user=Bank("Komal","komal_123",100000)
user.balance
print(user.balance())
print(user.withdraw(50000))
print(user._password)
# name mangling
#   accessing the private attributes, methods outside the class
print(user._Bank__amount)



# Absraction
#   abstraction means hiding the function implementation and showing the function decleartion
#         1.concrete method 
#         2.abstract method  
#Example
# from abc import ABC, abstractmethod
# class car(ABC):
#     @abstractmethod
#     def engine(self):
#         pass
#     @abstractmethod
#     def start(self):
#         pass
#       @abstractmethod
#      def breaks(self):
#         pass    
# class honda(car):
#     def engine(self):
#         #logic
#         pass
#     def start(self):
#         #logic
#         pass
#     def seats(self):
#         #logic
#         pass
#we cant create object for abstract class
