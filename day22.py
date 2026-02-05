#OOPS Concepts in Python
#1. Class - blue print of object
# #2. Object - instance of class
#3. Inheritance - child class can inherit the properties of parent class
#4. Polymorphism - same name different form
#5. Encapsulation - hiding the data and showing only the required details
#6. Abstraction - hiding the complexity and showing only the necessary details

# Class Syntax
# class Class_name:
#     Methods & Attributes
#     objects = Class_name()
#     objects.Method_name()

#Object Syntax
# object = Class_name()
# object.Method_name()

#Attributes
# class attribute -created inside the class
# instance attribute -created inside the constructor method


#class creation
# class class_name:
#     #attributes -what does class have
#     #methods -what does class do



#class student is created
#class attributes shares same data to all objects
#instance attributes are different for each object
class Student:
    #Class attribute
    school = "ABC School"
    #Constructor
    def __init__(self,name,age,cls):
        #instance attribute
        self.name = name
        self.age = age
        self.cls = cls
    #Method
    def details(self):
        return f"My name is {self.name} , I am {self.age} years old and I am in class {self.cls}"
    def update_school(cls,school_name):
        Student.school = school_name
#Object creation
s1=Student("Ravi",15,9)
s2=Student("Raju",16,10)
print(s1.name)
print(s2.name)
print(s1.school)
print(s2.school)
#Method calling
print(s1.details())
print(s2.details())
#updating instance attribute and class attributes outside the class
s1.school = "XYZ School"
s1.name= "Komal"
print(s1.school)
print(s2.school)
s1.update_school("DEF School")
print(s1.school)
print(s2.school)
