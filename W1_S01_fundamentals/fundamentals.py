# This is a comment 

"""
    Mulit lines
    comment 
    Doc String
"""
# variable  it's a placeholder a value (bocket)

variable_name = "value"

TEST_VAR = "Global"

# Data types

# Strings
name = "Alex"

#Numbers => integers & floats

age = 29 
grade = 7.2

# Boolen
test_result = False

is_happy = True

#- NoneType is a defined datatype 
empty_value = None

# Array in JS == List in python
#          0 1 2 3 4 5 
numbers = [1,2,3,4,5,6]

numbers.append(900)
numbers.append(-3)
# print(numbers)
numbers.pop(2)
# print(numbers)
# length
# print("the length of the list = ", len(numbers))

# Objects in JavaScript == Dictionnaries (Pandas, Numpy) 

student = {
    # - Key       Value
    'first_name':"Mark",
    'last_name':"Taylor",
    'age':28,
    'grades':[7.5,8.25,[25,8,["Steve", "Alex"]]],
    'is_happy':True
}
# print(student['grades'][2][2][1])

# print(f"My name is {student['first_name']} {student['last_name']} .")


# Tuples 
"""
Immutable ''lists'' !CANNOT BE CHANGED
"""

tup = (1,7,9)

# tup[0] = 9

tup = (9,5,7)