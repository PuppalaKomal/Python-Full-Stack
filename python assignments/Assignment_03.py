"""Write a Python Program to Check if a Number is Positive, Negative or Zero?
    Write a Python Program to Check if a Number is Odd or Even?
    Write a Python Program to Check Leap Year?
    Write a Python Program to Check Prime Number?
    Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?"""

#Write a Python Program to Check if a Number is Positive, Negative or Zero?
num=int(input("Enter a number: "))
if num>0:
    print("The number is positive")
elif num<0:
    print("The number is negative")
else:
    print("The number is zero")

#Write a Python Program to Check if a Number is Odd or Even?
num=int(input("Enter a number: "))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")
    
#Write a Python Program to Check Leap Year?
year=int(input("Enter a year: "))
if year%4==0 and year%100!=0 or year%400==0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")

#Write a Python Program to Check Prime Number?
num=int(input("Enter a number: "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("The number is not prime")
            break
        else:
            print("The number is prime")
else:
    print("The number is not prime")

#Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?"""
for num in range(1,10001):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
