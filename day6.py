#check the whether the number entered is even,odd,+ve,-ve  using nested if else statemen
'''n=int(input("Enter a number: "))
if n%2==0:
    if n>-1:
        print("Entered number is +ve even")
    else:
        print("Entered number is -ve even")
else:
    if n>-1:
        print("Entered number is +ve odd")
    else:
        print("Entered number is -ve odd")
        
#Loops 
#check which one is even number and odd number in the give list of numbers
lst=[2,4,3,5,6,7,9]
for num in lst:
    if num%2==0:
        print(num,"Number is even")
    else:
        print(num,"Number is odd")
print("Program is done! ")

##check for +ve and -ve numbers
lst=[2,4,-3,-5,6,-7,-9]
for num in lst:
    if num>-1:
        print(num,"Number is Positive")
    else:
        print(num,"Number is Negitive")
print("Program is done! ")

#print 1to20 numbers using rane function
for num in range (1,21,1):
    print(num)'''
    
#print even numbers from 1 to 20
for num in range(0,21,2):
    print(num,end=", ")