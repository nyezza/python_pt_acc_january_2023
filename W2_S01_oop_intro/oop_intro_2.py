dog_1 = {
    "name": "Mike",
    "age":4,
    "color": "brown"
}

class Dog:
    # Constructor
    def __init__(self,n,a,c):
        #Attributes--Values
        self.name = n
        self.age = a
        self.color = c

koke = Dog("Koke",5,"black")
lana = Dog("Lana",3,"gray")
print(f"The Dog name is {koke.name}, he is  {koke.age} old and he has {koke.color} hair color 🐶")
print(f"The Dog name is {lana.name}, he is  {lana.age} old and he has {lana.color} hair color 🐶")