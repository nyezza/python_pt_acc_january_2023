from human import Human

class Barberian(Human):
    def __init__(self,name):
        super().__init__(name)
        self.strength += 20 #! Polymorphism
        self.rage = 30 #! Polymorphism

conan = Barberian("Conan")
print(conan.strength)