import json
try:
    with open('contact.json','r') as file:
        data=json.load(file)
        print(data)
        # print(list(data))
except Exception as e:
    print(e)

# try:
#     with open('contact.json','r') as file:
#         data=json.dumps(file)
#         print(data)
#         # print(list(data))
# except Exception as e:
#     print(e)


#counting target element
lst=[1,2,3,1,2,3,1]
target=1
count=0
def count_target(lst,target):
    for i in lst:
        if i==target:
            count+=1
    return count
result=count_target(lst,target)
print(result)
