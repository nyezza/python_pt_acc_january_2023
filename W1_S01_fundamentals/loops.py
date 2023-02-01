"""
range => function will return a squence of integers 
range(start,stop,step)
    start = inclusive , optional and default value = 0
    stop = exclusive ,required
    step increment can be + or - dafult = 1
    Example 
        range(0,10,1) => (0,1,2,3,4,5,6,7,8,9)
        range(0,10,2) => (0,2,4,6,8)
        range(10) => (0,1,2,3,4,5,6,7,8,9)
"""

# for i in range(10,0,-1):
#     print(i)

super_heros = ["batman", "spiderman", "thor", "wonder woman", "jedi"]

student = {
    'first_name':"Mark",
    'last_name':"Taylor",
    'age':28,
    'grades':[7.5,8.25,[25,8,["Steve", "Alex"]]],
    'is_happy':True
}

# for hero in super_heros:
#     print(hero)

# for key,value in student.items():
#     print(f"{key} == {value}")

# for key in student.keys():
#   print(key)

# for value in student.values():
#   print(value)

# x = 5
# while x> 0:
#     print("Yes")
#     x -=1
age = 80
# Conditionals

if (age > 18) & (age < 60) :
    print("Welcome To the Club")
elif age == 80 :
    print("Call the Plolice")
else :
    print("You need to go home")