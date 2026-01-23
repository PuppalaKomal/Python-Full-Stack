"""Write a Python program to convert kilometers to miles?
Write a Python program to convert Celsius to Fahrenheit?
Write a Python program to display calendar?
Write a Python program to solve quadratic equation?
Write a Python program to swap two variables without temp variable?"""


#Write a Python program to convert kilometers to miles?
km=float(input("Enter the value of km to change into miles: "))
miles=km*0.621371
print("The value of",km,"km in miles is",miles)

#Write a Python program to convert Celsius to Fahrenheit?
f=float(input("Enter the value for fahrenheit to convert into celsius: "))
c=(f-32)*5/9
print("The value of",f,"fahrenheit in celsius is",c)

#Write a Python program to display calendar?
import calendar
year=int(input("Enter the year to display the calendar: "))
print(calendar.calendar(year))

#Write a Python program to solve quadratic equation?
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

def equation(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        print("No real roots")
    elif d == 0:
        root = -b / (2 * a)
        print("One real root:", root)
    else:
        root1 = (-b + d ** 0.5) / (2 * a)
        root2 = (-b - d ** 0.5) / (2 * a)
        print("Two real roots")
        print("The roots are:", root1, "and", root2)
if a == 0:
    print("Not a quadratic equation (a cannot be 0)")
else:
    equation(a, b, c)

#Write a Python program to swap two variables without temp variable?
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
a, b = b, a
print("The value of a after swapping is: ", a)
print("The value of b after swapping is: ", b)
