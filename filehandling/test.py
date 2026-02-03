#counting target element
lst=[1,2,3,1,2,3,1]
target=int(input("Enter the target element: "))
def count_target(lst,target):
    count=0
    for i in lst:
        if i==target:
            count+=1
    return count
result=count_target(lst,target)
print(result)