# # Function
# # - a set on instructions
# # - could tak a parameters

#! # - all functions or Methods Must Return Something (even it's None)

def say_hi():
    print("Hi")

# # ! INVOKE the function
# # say_hi()

def multiply(*args):
    a = 1
    for i in args:
        a *= i
    return a

print(multiply(2,3,4,5,852))

alex = {'id':1,'first_name':"Alex", 'last_name':"Max"}

def find_user(**kwargs):
    print(f'{kwargs["first_name"]}  ')

find_user(id= 2, first_name="Alex")


a = 30

def a_parent_function():
    a = 50
    def a_function():
        a = 22
        a = a + 2
        return a
    return a_function()

print(a_parent_function()) #22
print(a) #30

# Start with the local 
# Parent local scope
# Global Scope