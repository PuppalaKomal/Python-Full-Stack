#Nested loops
#printing tables using nested loops
"""for i in range(1,4):
    for j in range(1,21):
        print(f"{i} * {j} ={i*j}")
    print("**********************************************")
    
#printing numbers horizontally
for i in range(1,11):
    print(i,end=" , ")
    
#print table using function
n=int(input("Enter the number: "))
def print_table(n):
    for i in range(1,21):
        print(f"{n} * {i} ={n*i}")
print_table(n)"""


#printing patterns using nested loops 
# ******
n=int(input("Enter the number of rows: "))
for i in range (1,n+1):
    print("*",end=" ")
#star 
n=int(input("Enter the number of rows: "))
for i in range (1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()
    
for i in range (5):
    for j in range(5):
        if i==j or j== 5-1-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


### 1 1 1 1 
### 2 2 2 2
### 3 3 3 3
### 4 4 4 4
for i in range (5):
    for j in range(5):
        print(i+1,end=" ")
    print()
    
### 1 2 3 4 
### 1 2 3 4
### 1 2 3 4
### 1 2 3 4
for i in range (5):
    for j in range(5):
        print(j+1,end=" ")
    print()
    
    
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for i in range(5):
    for j in range(5):
        if i>j or i==j:
            print(i+1,end=" ")
    print()
    
# *        *
# *  *     *
# *    *   *
# *      * *
# *        *
for i in range(5):
    for j in range(5):
        if i==j or j==0 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#  * * * * * *     
#  *
#  * * * * * *
#            *
#  * * * * * *
n = 6

for i in range(n):
    for j in range(n):
        if (
            i == 0 or                      # top row
            i == n - 1 or                  # bottom row
            (i == 5 // 2) or               # middle row
            (j == 0 and i <= 5 // 2) or    # left vertical (top half)
            (j == n - 1 and i >= 5 // 2)   # right vertical (bottom half)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

