"""#find topper from a list of students
#take number of students input
#for each student 
#take input as follows
#name -six subject marks
#take 10 students
#find total students average marks
#find each subject average marks
stdnts=[]
telugu=[]
english=[]
hindi=[]
maths=[]
science=[]
social=[]
evs=[]
total_marks=[]
percentage=[]
for i in range(10):
    name=input("Enter the name of the student: ")
    print("Enter marks")
    telugu.append(int(input("Telugu: ")))
    english.append(int(input("English: ")))
    hindi.append(int(input("Hindi: ")))
    maths.append(int(input("Maths: ")))
    science.append(int(input("Science: ")))
    social.append(int(input("Social: ")))
    evs.append(int(input("EVS: ")))
    total_marks.append(telugu[i]+english[i]+hindi[i]+maths[i]+science[i]+social[i]+evs[i])
    percentage.append(total_marks[i]/7)
    stdnts.append(name)
print(stdnts)
print(telugu)
print(english)
print(hindi)
print(maths)
print(science)
print(social)
print(evs)
print(total_marks)
print(percentage)
print("Topper is",stdnts[percentage.index(max(percentage))],"with",max(percentage),"percentage")
print("Average marks of students is",sum(total_marks)/10)
print("Average marks of telugu is",sum(telugu)/10)
print("Average marks of english is",sum(english)/10)
print("Average marks of hindi is",sum(hindi)/10)
print("Average marks of maths is",sum(maths)/10)
print("Average marks of science is",sum(science)/10)
print("Average marks of social is",sum(social)/10)
print("Average marks of evs is",sum(evs)/10)
print("Average marks of students is",sum(total_marks)/10)"""

#who is topper
print("Welcome to the who is the topper")
n=int(input("Enter the number of students: "))
names=[]
marks=[]
class_marks=[]
percentage=[]
print("Enter the all students marks")
for i in range(n):
    print(f'Enter the student {i+1}marks: ')
    name=input("Enter the name of the student: ")
    print("Enter the Telugu,English,Hindi,Maths,Science,Social marks as per the order")
    Telugu,English,Hindi,Maths,Science,Social=map(int,input().split()[:6])
    total_marks=Telugu+English+Hindi+Maths+Science+Social
    std_percent=(total_marks/600)*100
    #storing data into lists
    names.append(name)
    marks.append([Telugu,English,Hindi,Maths,Science,Social])
    class_marks.append(total_marks)
    percentage.append(std_percent)
#print the topper details
print("Topper in the class")  
top_marks=max(class_marks)
topper_pos=[]  
for i in range(n):
    if class_marks[i]==top_marks:
        topper_pos.append(i)
#print the topper etails
for i in range(len(topper_pos)):
    print("Name of the student is: ",name[i])
    print("Marks of the student is: ",marks[i])
#each student marks
for i in range(n):
    print("Name of the student is: ",name[i],"and Marks is: ",marks[i])
    
    
#find the smallest value in the list without using build in functions 
#find the largest value in the list
#find length of list

#find the smallest value in the list without using build in functions 
lst=[200,60,30,40,50]
smallest=lst[0]
for i in range(1,len(lst)):
    if lst[i]<smallest:
        smallest=lst[i]
print("Smallest value in the list is: ",smallest)

#find the largest value in the list
lst=[200,60,30,40,50]
largest=lst[0]
for i in range(1,len(lst)):
    if lst[i]>largest:
        largest=lst[i]
print("Largest value in the list is: ",largest)

#find length of list
lst=[200,60,30,40,50]
length=0
for i in lst:
    length+=1
print("Length of the list is: ",length)
