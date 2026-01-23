"""Write a Python program to print "Hello Python"?
    Write a Python program to do arithmetical operations addition and division.?
    Write a Python program to find the area of a triangle?
    Write a Python program to swap two variables?
    Write a Python program to generate a random number?"""


#Write a Python program to print "Hello Python"?
print("Hello Python")

#Write a Python program to do arithmetical operations addition and division.?
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
print("The sum of a,b is:",a+b)
print("the quotient when a is divided by b is:",a/b)

#Write a Python program to find the area of a triangle?
b=int(input("Enter the value of base: "))
h=int(input("Enter the value of height: "))
area_of_triangle=0.5*b*h
print("the area of triangle when base is",b,"and height is",h,"is",area_of_triangle)

#Write a Python program to swap two variables?
a=int(input("Enter a number:"))
b=int(input("Enter another number: "))
a,b=b,a
print("The values of a,b after swapping is: ",a,b)

#Write a Python program to generate a random number?
import random
print(random.randint(0,100))
    