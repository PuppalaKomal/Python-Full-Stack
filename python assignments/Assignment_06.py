# Write a Python Program to Display Fibonacci Sequence Using Recursion?
# Write a Python Program to Find Factorial of Number Using Recursion?
# Write a Python Program to calculate your Body Mass Index?
# Write a Python Program to calculate the natural logarithm of any number?
# Write a Python Program for cube sum of first n natural numbers?

# Write a Python Program to Display Fibonacci Sequence Using Recursion?
"""n=int(input("Enter the number of terms: "))
a=0
b=1
print(a, end=" , ")
print(b, end=" , ")
for i in range(2,n):
    c=a+b
    print(c ,end=" , ")
    a=b
    b=c
    
# Write a Python Program to Find Factorial of Number Using Recursion
n=int(input("Enter a number: "))
if n<0:
    print("The factorial doesnt exist for negitive number")
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("The factorial of",n,"is",fact)"""
    
# Write a Python Program to calculate your Body Mass Index?
height=float(input("Enter your height in meters: "))
weight=float(input("Enter your weight in kilograms: "))
gender=input("Enter your gender: ")
BMI=weight/(height**2)
if gender=="male":
    if BMI<18.5:
        print("Underweight")
    elif BMI>=18.5 and BMI<24.5:
        print("Normal")
    elif BMI>=24.5 and BMI<29.9:
        print("Overweight")
    else:
        print("Obesity")
elif gender=="female":
    if BMI<18.5:
        print("Underweight")
    elif BMI>=18.5 and BMI<24.5:
        print("Normal")
    elif BMI>=24.5 and BMI<29.9:
        print("Overweight")
    else:
        print("Obesity")
    
