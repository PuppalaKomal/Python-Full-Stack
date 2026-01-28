# Problem Solving
# 1 find length of number eg: 456=3
# 2 sum of digit in a number eg:123=6
# 3 reverse a number eg:321=123
# 4 armstrong number 

# 1 find length of number eg: 456=3
n=int(input("Enter a number: "))
count=0
if n<0:
    n=n*(-1)
while n>0:
    n=n//10
    count+=1
print(count)

# 2 sum of digit in a number eg:123=6
n=int(input("Enter a number: "))
s=0
while n>0:
    digit=n%10
    n=n//10
    s=s+digit
print(s)

#3 reverse a number eg:321=123
n=int(input("Enter a number: "))
s=0
while n>0:
    digit=n%10
    n=n//10
    s=s*10+digit
print(s)

# 4 armstrong number
