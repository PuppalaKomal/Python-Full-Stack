#execption handeling
    #errors:
        #syntax error(compile time error)
        #runtime error(exeption)
            # 1 try: 
            # 2 except
            # 3 else
            # 4 finally
            
 # EG run time error
try:
    a=10
    b=0
    c=a/b
    print(c)
except:
     print("something is not right")
     
#EG compile time error(syntax error)
#syntax error :
# if 1==0
# print(0)

# #syntax error  ""
# print("hello)

# syntax error )
# print("Hello"

#EG runtime error (type error)
# t=(1,2,3,4)
# t[0]=100
# print(t)

#EG runtime error (intendation error)
# if 1==0:
# print(1)

#zerodivisonerror
# try:
#     a=10
#     b=2
#     c=a/b
#     print(c)
# except :
#     print("Something is wrong")
    
# try:
#     a=10
#     b=0
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("Zero division is not possible")
# except:
#     print("Something else is wrong")
    
try:
    a=10
    c=a+"hi"
    print(c)
except ZeroDivisionError:
    print("Zero division is not possible")
except:
    print("Something else is wrong")
    