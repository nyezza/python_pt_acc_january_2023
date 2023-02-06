#

# OOP : Object Oriented Programming 
# clean code 
# DRY
# Model real life 

student_1 = {'first_name': "John", 'last_name':"Wick",'age':45,'grade':9.8}
student_2 = {'first_name': "Jack", 'last_name':"Sparrow",'age':56,'grade':8.9}
student_3 = {'first_nme': "Mary", 'last_name':"Jones",'age':35,'gade':9.7}

# Class  = template or blueprint to create objects

# Objects have carachteristics and actions

#  Attributes => what the object can have => nouns
#  Methods => what the object can do => verbs => function inside the class

class Student:
    # - Class Attribute belong to all objects the class
    school = "MIT"
    # Constractor initialize the new objects (Instance Method)
    def __init__(self,fn, ln,a,g):
        # -Instance Attibutes----Values
        self.first_name = fn 
        self.last_name = ln
        self.age = a
        self.grade = g
        # * self refers to the object
    # Instance Method
    def add_grade(self,rate):
        self.grade+=self.grade * rate

    # * cls refers to the class
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
    
    @staticmethod
    def can_hi_pass(grade,lowest_grade):
        if grade > lowest_grade:
            return True
        else:
            return False
    
alex = Student("Alex","Taylor", 32,5.7)
sarah = Student("Sarah","Rayes", 22,8.7)
# print(alex.grade)
alex.add_grade(0.5)
alex.change_school('Cali Tech')
print(alex.school)
print(sarah.school)
print(isinstance(alex,Student))

