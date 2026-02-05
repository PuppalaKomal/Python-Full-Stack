# write a python program to find the sum of a given number
    #test case:
        #input:456
        #output:15
n=int(input("Enter a number: "))
s=0
while n>0:
    s+=n%10
    n//=10
print(s)

# write a python program to reverse given number
    #test case:
        #input:456
        #output:654
n=int(input("Enter a number: "))
s=0
while n>0:
    s=s*10+n%10
    n//=10
print(s)

# write a python program to check the given number is armstorng number or not
    #test case:
        #input:153
        #output:153 is armstrong number 
n=int(input("Enter a number: "))
s=0
while n>0:
    s+=n**3
    n//=10
print(s)

# write a python program to find the sum of first N natural numbers
    #test case:
        #input:5
        #output:15
n=int(input("Enter a number: "))
s=0
while n>0:
    s+=n
    n-=1
print(s)
 
# write a python program to find the number of digits
    #test case:
        #input:456
        #output:3
n=int(input("Enter a number: "))
s=0
while n>0:
    s+=1
    n//=10
print(s)

# write a python program to find the sum of all elements in  lis    #test case:
        #input:[10,1,20,2,30]
        #output:63
l=[10,1,20,2,30]
s=0
for i in l:
    s+=i
print(s)

# write a python program to print the frequency of each element in the list
    #test case:
        #input:[1,2,2,3,3,3]
        #output:1=1,2=2,3=3
l=[1,2,2,3,3,3]
d={}
for i in l:
    d[i]=d.get(i,0)+1
print(d)
