"""#add two numbers using function
def add(a,b):
    return a+b
print(add(10,20))

#add 3 numbers using function
def add(a,b,c):
    return a+b+c
print(add(10,20,30))

#add 4 numbers using function
def add(a,b,c,d):
    return a+b+c+d
print(add(10,20,30,40))

#default arguments
# adding n number in a single function
def add(a,b,c=0,d=0):
    return a+b+c+d
print(add(1,2,3,4))
print(add(1,2,3))
print(add(1,2,4))"""

"""#default arguments
# multiplication n number in a single function
def add(a,b,c=1,d=2):
    return a*b*c*d
print(add(1,2,3,4))
print(add(1,2,3))
print(add(1,2,))

#variable length of positional argument
def add(a, *args):
    print(a)
    print(args)
    s=0
    for num in args:
        s += num
    return s
print(add(1,2,3,4,5))
 
#list operations
#1 concatination
#2 repetation

#1 concatination
l1=[1,2,3]
l2=[3,2,1]
l3=l1+l2
print(l3)

#2repattion
l1=[1,2,3]
print(l1*2)
print(l1*3)

#add 100 element to the end of list
lst=[1,2,3]
print(lst+[100])"""

### list functions
lst=[1,2,3,4,4,5,6,6,7]
"""#append
print(lst.append(100))
print(lst)
#extend
lst.extend([200,300,400])
print(lst)
#insert
lst.insert(3,50)
print(lst)"""

#pop
print(lst.pop(3))
#remove
lst.remove(2)
#delete
del lst[2:4]
print(lst)

#count
print(lst.count(6))
#index
print(lst.index(3))
#sort(assending)
lst.sort()
print(lst)
#sort(desending)
lst.sort(reverse=True)
print(lst)


##convert list of number into even list and odd list
lst=list(map(int,input("Enter list of numbers").split()))
even_list=[]
odd_list=[]
for num in lst:
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)
print("Even list: ",even_list)
print("Odd list: ",odd_list)
 
 
#marks analyser
#pass marks=35(+)
#fail marks=35(-)
marks=list(map(int,input("Enter marks: ").split()))
def marks_analyser(marks):
    if marks>=35:
        return "Pass"
    else:
        return "Fail"
print(marks_analyser(marks))

