# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
"""num=4
n= 1
for i in range(num):
    for j in range(num):
        print(n,end="\t")
        n+=1
    print()


#  + + + + 
#  - - - -
#  + + + +
#  - - - -
num=4
for i in range(num):
    for j in range(num):
        if i%2==0:
            print("+",end="\t")
        else:
            print("-",end="\t")
    print()
# +  -  +  -
# -  +  -  +
# +  -  +  -
# -  +  -  +

num=4
for i in range(num):
    for j in range(num):
        if (i+j)%2==0:
            print("+",end="\t")
        else:
            print("-",end="\t")
    print()


#  1
#  2 3 
#  4 5 6 
#  7 8 9 10
num=4
n=1
for i in range(num):
    for j in range(i+1):
        print(n,end="\t")
        n+=1
    print()

#  0  1  0  1
#  1  0  1  0 
#  0  1  0  1
#  1  0  1  0
num=4
for i in range(num):
    for j in range(num):
        if (i+j)%2==0:
            print("0",end="\t")
        else:
            print("1",end="\t")
    print()

# * * * *  
# *     *
# *     * 
# * * * *
n=4
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="\t")
        else:
            print(" ",end="\t")
    print()
    
# * * * *  
# * + + *
# * + + * 
# * * * *
n=4
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="\t")
        else:
            print("+",end="\t")
    print()

# *
# * *
# *   *
# * * * *
n=6
for i in range(n):
    for j in range(n):
        if i==n-1 or i==j or j==0  :
            print("*",end="\t")
        else:
            print(" ",end="\t")
    print()"""

#  * * * *
#    *   *                                      
#      * *
#        *
n=4
for i in range(n):
    for j in range(n):
        if j==n-1 or i==j or i==0  :
            print("*",end="\t")
        else:
            print(" ",end="\t")
    print()