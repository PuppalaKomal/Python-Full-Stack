#checking the number is even or odd using functions
num=int(input("Enter a number: "))
def even_check(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
if even_check(num)=="even":
    print("Number is even")
else:
    print("Number is odd")

#find the string lenght without len()
string=input("Enter a string: ")
count=0
for each in string:
    count+=1
    print(count)
    
"""##types of arguments
    postitional argument
    default argument
    keyword argument
    variable lenghts positinal of agrument
    variable length of keyword argument"""
    
#positional arguments
#subtraction of two numbers
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
def subtraction(n1,n2):
    res=n1-n2  
    return res
print(subtraction(a,b)) #try inverse of a,b to b,a and check result
 
#keyword arguments
#subtraction of two numbers
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
def subtraction(n1,n2):
    res=n1-n2  
    return res
print(subtraction(n1=a,n2=b))
print(subtraction(n2=a,n1=b))

#list properties
#indexing
my_list=[1,2,3,4,4.543,"hello","hi"]
print(my_list)
print(my_list[0])
print(my_list[-3])
print(my_list[1:])
print(my_list[:4])
print(my_list[1:4])

#muteable
my_list=[1,2,3,4,4.543,"hello","hi"]
my_list[0]=10
print(my_list)

#accessing elements in a nested list
my_list=[1,2,3,[4,5,6],7,8]
print(my_list[3])
print(my_list[3][2])

my_list=[1,2,3,[4,5,6,["k","o","m"]],7,8]
print(my_list[3])
print(my_list[3][2])

#reading list of elements form user
l=map(int,input("Enter elements of list: ").split())
print(type(l),l) #input 1,2,3,4,5

#read list of numbers if numer is even add 0.5 and if the number is odd add one
#my_list=[1,2,3,4,5]
my_list=list(map(int,input("Enter elements of list: ").split()))
for i in range (0,len(my_list)):
    if my_list[i]%2==0:
        my_list[i]=my_list[i]+0.5
    else:
        my_list[i]=my_list[i]+1
print(my_list[i])