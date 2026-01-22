# get number of student in the class
n=int(input("Enter number of students in the class: "))
present_count=0
absent_count=0
rollnumber=1
while rollnumber <= n:
    print("Enter",rollnumber,"is present of absent and select following options" "Enter 1 or 2 \n 1. Present \n 2. Absent  ")
    status=input()
    #check sratus
    if status == "1":
        present_count += 1
        rollnumber += 1
    elif status == "2":
        absent_count += 1
        rollnumber += 1
    else:
        print("Please select either 1 or 2 options")
print("Total students in the class: ",n) 
print("Number of students present in class is: ",present_count)
print("Number of students absent in the class is : ",absent_count)
percentage = (present_count/n)*100
print("Attendence Report: ",percentage)