"""#String Operations and functions
#String Concatination
s1= "k" 
s2= "om"
s3= "al"
s4=s1+s2+s3
print(s4)

#String Repeatation
print(s1*3)

###String Functions
#Case Conversion Functions lower(),upper(),title(),swapcase(),capitalize()
s="I am Pursuing Masters"
print(s.capitalize())
print(s.upper())
print(s.title())
print(s.lower())
print(s.swapcase())

###Sub String index find find(), strip(), split()
#find()
s="I am Pursuing Master"
print(s.find("a"))
print(s.find("a", 10 ))#starts from 10th position and finds the first occurence of the char

#strip() it removes the char at ends or  the space
s="@@@@@@@@@@I am Pursuing Master@@@@@@@@@@"
print(s)
print(s.strip())
print(s.lstrip("@"))
print(s.rstrip("@"))

#split()
s="@@@@@@@@@@Komal@@@@@@@@@@"
print(s)
print(s.split("a"))
print(s.split("m"))

#case checking function
s1= "k" 
s2= "OM"
s3= "al"
s4= "123"
s5= "ABC"
s6= "aBc123"
print(s1.islower())
print(s1.isupper())
print(s4.isdigit())
print(s6.alnum())
print(s5.isalpha())"""


#username and password validator using case check functions
#username
username=input("Enter username: ")
if len(username) >=8 and username[0].isalpha() : 
    for char in username:
        if char.isupper():
            has_upper=True
        elif char.islower():
            has_lower=True
        elif char.isdigit():
            has_digit=True
        elif char in ["_","@"]:
            has_special=True
    if has_upper and has_lower and has_digit and has_special:
        print("Username is valid!")
    else:
        print("Username is not valid!")
else:
    print("Username is not valid!")

#password 
password=input("Enter password: ")
if len(password) >=8 and password[0].isalpha() : 
    for char in password:
        if char.isupper():
            has_upper=True
        elif char.islower():
            has_lower=True
        elif char.isdigit():
            has_digit=True
        elif char in ["_","@"]:
            has_special=True
    if has_upper and has_lower and has_digit and has_special:
        print("Password is valid!")
    else:
        print("Password is not valid!")
else:
    print("Password is not valid!")


#class explanation of username and password validation 
s=input("Enter a string: ")
validation_string="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890@_"
if len(s)>=8:
    if s[0].isupper() or s[0].islower():
        for i in range(1,len(s)):
            if s[i] not in validation_string:
                print("Invalid String")
                break
        else:
            print("Valid String")
    else:
        print("Invalid String")
else:
    print("Invalid String") 