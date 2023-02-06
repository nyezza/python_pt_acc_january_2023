
class Knight(Human):
    def __init__(self,name):
        super().__init__(name) # call my parent (Human)
        self.name = name
        self.health +=10
        self.defense += 50

    def heal(self):#! Polymorphism
        self.health += self.defense/5 #! Polymorphism
        print(f"[KNIGHT] {self.name} heams for {self.defense/5} and now has {self.health} HP") #! Polymorphism