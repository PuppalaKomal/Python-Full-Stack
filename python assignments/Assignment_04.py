###Write a Python Program to Find the Factorial of a Number?
###Write a Python Program to Display the multiplication Table?
###Write a Python Program to Print the Fibonacci sequence?*
###Write a Python Program to Check Armstrong Number?*
###Write a Python Program to Find Armstrong Number in an Interval?*
###Write a Python Program to Find the Sum of Natural Numbers?

###Write a Python Program to Find the Factorial of a Number?
"""n=int(input("Enter a number: "))
if n<0:
    print("The factorial doesnt exist for negitive number")
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("The factorial of",n,"is",fact)
    
###Write a Python Program to Display the multiplication Table?
n=int(input("Enter a number which you want to display the multiplication table: "))
for i in range (1,21):
    print(n,"x",i,"=",n*i)
    
##Write a Python Program to Find the Sum of Natural Numbers?
n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("The sum of first",n,"natural numbers is",sum)"""

###Write a Python Program to Print the Fibonacci sequence?*
n=int(input("Enter the number of terms: "))
a=0
b=1
print(a, end=" , ")
print(b, end=" , ")
for i in range(2,n):
    c=a+b
    print(c ,end=" , ")
    a=b
    b=c
    
###Write a Python Program to Check Armstrong Number?*
num = int(input("Enter a number: "))
digits = len(str(num))
result = 0
for d in str(num):
    result = result + (int(d) ** digits)
if result == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

