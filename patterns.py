''''* * * *
    * * * *
    * * * *
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
for i in range(rows):
    for j in range(columns):
        print("*",end=" ")
    print()'''

''''* 
    * *
    * * * 
    * * * *

star=int(input("Enter number of Rows: "))
for i in range(0,star+1):
    for j in range(i):
        star += 1
        print("*", end=" ")
    print ()
        
    1
    1 2
    1 2 3
    1 2 3 4'''

rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
       