#File Handling in python
    #File Operations
        #Open File #file_obj=open("filename","mode")
        #Reading Files
        #Writing Files
        #Closing Files
#File Modes
    #r - Read Mode : reading contents from file
    #w - Write Mode : writing contents to file
    #a - Append Mode : appending contents to file (adds new content to the existing content)
    #x - Create Mode : creating a new file 
    #t - Text Mode : text mode for reading or writing
    #b - Binary Mode : binary mode for reading or writing
    #+ - Update Mode : update mode for reading and writing
# #write mode
# f=open("sample.txt","w")
# string="""My Name is Komal
#             I am learning Python?"""
# f.write(string)
# f.close()
# print("Content added successfully")

# #append mode
# f=open("sample.txt","a")
# string="""java programming"""
# f.write(string)
# f.close()
# print("Content added successfully")

# r+ mode
f=open("sample.txt","r+")
string="""java programming"""
f.write("SQL query language")
content=f.read()
print(content)
f.close()
print("Content added successfully")
