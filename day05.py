#checking weather the number  is +ve,-ve or 0
n=int(input("Enter the number: "))
if n>0:
    print(n," is positive")
elif n==0:
    print("Entered number is zero")
else:
    print(n," is negetive")
    
#checking weather the entered number is factor of 5 or not
n=int(input("Enter a number: "))
if n%5==0:
    print(n," is divisible by 5")
else:
    print(n," Is not divisible by 5")
    
#check weather the number is : factor of 3,factor of 5,factor of both 3 and 5, not factor of both 3 and 5
n=int(input("Enter a number:  "))
if n%3==0 and n%5==0:
    print(n," is factor of both 3 & 5")
elif n%3==0:
    print(n," is factor of 3 ")
elif n%5==0:
    print(n," is factor of 5")
elif n%3!=0 and n%5!=0:
    print(n," is not factor of both 3 and 5")

#Finding the biggest number amoungst the entered 3 values
a=int(input("Enter value for a: "))
b=(int(input("Enter value for b: ")))
c=(int(input("Enter the value for c: ")))
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("The largest number is:", largest)
