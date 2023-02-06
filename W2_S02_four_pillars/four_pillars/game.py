
# 4 Pillars of OOP
# - 1-- Encapsulation = Create Classes
# - 2--Inheritance                    
#  -3 - Polymorphism  =  many  + forms
# - 4 - Abstarction = Hide Comlexity 
class Human:

    # Constractor
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.strength = 10
        self.power = 10
        self.defense = 5
        self.weapons = []

    # Methods 
    def attack(self,target):
        print(f"[ATTACK] {self.name} is attacking {target.name}")
        # target.health= target.health - self.power
        target.defend((self.power+self.strength)/2) #! Abstraction
        # target.health -= (self.power+self.strength)/2 #  damage = 10


    def defend(self,damage):
        # 10 - 5
        damage -= self.defense
        self.health -= damage
        print(f"[DEFEND] {self.name} takes  {damage} DMG and now {self.health} HP")

# ! Inheritance 
class Barberian(Human):
    def __init__(self,name):
        super().__init__(name)
        self.strength += 20 #! Polymorphism
        self.rage = 30 #! Polymorphism

class Knight(Human):
    def __init__(self,name):
        super().__init__(name) # call my parent (Human)
        self.name = name
        self.health +=10
        self.defense += 50

    def heal(self):#! Polymorphism
        self.health += self.defense/5 #! Polymorphism
        print(f"[KNIGHT] {self.name} heams for {self.defense/5} and now has {self.health} HP") #! Polymorphism

class Seer:
    def __init__(self):
        self.mana = 50
        self.hidden_type = Barberian("No Name") #! Abstarction




alex = Human("Alex")

# print(f"Health  = {alex.health} \n Strength = {alex.strength} \nRage = {alex.rage}")

conan = Barberian("Conan")

# print(f"Name = {conan.name} \nHealth  = {conan.health} \nStrength = {conan.strength} \nRage = {conan.rage}")

# conan.attack(alex)
# print(f"Health  = {alex.health} \n Strength = {alex.strength}")

# print(isinstance(conan,Barberian))

mary = Seer()
print(mary.hidden_type.rage)
