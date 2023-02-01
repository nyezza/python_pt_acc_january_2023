# first_name, last_name ,age, grade

# OOP = Object Oriented Programming
# write Cleaner Code 
# DRY
# Model real life
student_1 = {'first_name': "John", 'last_name':"Wick",'age':45,'grade':9.8}
student_2 = {'first_name': "Jack", 'last_name':"Sparrow",'age':56,'grade':8.9}
student_3 = {'first_nme': "Mary", 'last_name':"Jones",'age':35,'gade':9.7}

# -Class = template or the blueprint for cerating a new objects (students)

# BMW WV Renaut = car FACTORIES => Constructor

class Student:

    # - Class Attribute
    school = "MIT Junior"

    # Constractor
    def __init__(self,first_name, last_name,age,grade):
        # -Instance-Attribues--
        #  Attributes are what the object (student can have) characteristics ==> nouns
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade = grade

    # - Methods  == Functions inside the class
    # Methods are what the object (student) can do => actions => verbs
    def increase_age(self,years):
        self.age += years
        return self

    # * This is a classmethod decorator= @classmethod => I am Modifining class attribute
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    # * This is a static method it will no change anything it's only for display or validations
    @staticmethod
    def display_info(self):
        print(f"Student name is {self.first_name} {self.last_name} he is {self.age} years old and he had {self.grade} points in Algos")
        return self

    @staticmethod
    def will_pass(self):
        print(self.grade> 6.0)
        return self

# Alex = Object = Instance of the class Student
alex = Student("Alex","Taylor", 47, 8.25)
maxi = Student("Max","Taylor", 32, 5.5)
# Chaining Methods
# alex.display_info().increase_age(10).display_info().increase_age(1).increase_age(100).display_info().increase_age(8000).display_info()

maxi.change_school("California TECH")
print(isinstance(alex,Student))
print("Max == ",maxi.school)
print("Alex == ",alex.school)

# Attributes = Instance Attributes (defined inside the contructor)
#              Class Attributes defined befor the contructor


# Methods = Instance methods (to modify instabce attributes (Construcotr = def __init__)) No decorator
#           Class Methods (to modify or change class Attributes) with decorator @classmethod
#           Static Method (cannot change or modify anything) with decorator @staticmethod