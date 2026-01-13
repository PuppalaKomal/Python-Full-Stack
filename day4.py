#*******Conditional Statements*******
#if the number is zero, then print " Entered Number is Zero"

#if Condition
"""n = int(input("Enter a Number: "))
if n ==0:
    print("Entered number is zero")
print("Program is done")

#if else condition
n = int(input("Enter a Number: "))
if n == 0:
    print("Entered number is zero")
else:
    print("Entered number is not zero")

#2nd Approach
n = int(input("Enter a Number: "))
if n != 0:
    print("Entered number not zero")
else:
    print("Entered number is  zero")
    
#Check for Even or Odd Number
n = int(input("Enter a Number: "))
if n%2==0:
    print("Entered Number is Even") 
else:
    print("Entered number is odd")"""   

#check the whether the number entered is 0,+ve,-ve
n = int(input("Enter a Number: "))
if n%2==0 and n>0:
    print("Entered number is Positive and Even")
elif n%2==0 and n<0:
    print("Entered number is Negitive and Even")
elif n%2 !=0 and n>0 :
    print("Entered Number is Positive and Odd ")
else :
    print("Enterned number is Negivtive and Odd ")
    
