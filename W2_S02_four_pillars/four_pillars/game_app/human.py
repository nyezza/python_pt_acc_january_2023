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