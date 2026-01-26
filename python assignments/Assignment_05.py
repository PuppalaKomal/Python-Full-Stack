###Write a Python Program to Find LCM?
###Write a Python Program to Find HCF?
###Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
###Write a Python Program To Find ASCII value of a character?
###Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?


###Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
"""def calculator():
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b== 0:
        return "division by zero not possible"
    return a/b
if __name__=="__main__":
    print("Welcome to small level calculator\n")
    n1=int(input("enter first number: "))
    n2=int(input("enter second number: "))
    print("1. addition\n 2. subtraction\n 3. multiplication\n 4. division")
    choice=int(input("enter your choice: "))
    if choice==1:
        print("result of addition is",addition(n1,n2))
    elif choice==2:
        print("result of subtraction is",subtraction(n1,n2))
    elif choice==3:
        print("result of multiplication is",multiplication(n1,n2))
    elif choice==4:
        print("result of division is",division(n1,n2))
    else:
        print("invalid choice") 

###Write a Python Program to Find LCM?
num1=int(input("Enter the first number: "))
num2=int(input("Enter the value of second number: "))
def find_lcm(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1
print("LCM is:", find_lcm(num1, num2))"""

###Write a Python Program to Find HCF?
num1=int(input("Enter the first number: "))
num2=int(input("Enter the value of second number: "))
def find_hcf(a, b):
    smaller = min(a, b)
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf
print("HCF is:", find_hcf(num1, num2))
