from examplemodule1 import Character

class Monk(Character):
    base_att_roll_on_level = 1 




    def __init__(self, level=1, roll=19, armor_class=10):
        super().__init__(armor_class)
        self.hp = 6
    #     self.attack_damage = 3
    #     self.base_att_roll_on_level = 1 
    #     self.type = "Chicken"
        
class Fighter(Character):
    def __init__(self, level=1, roll=19, armor_class=10):
        self.hp = 10
        self.attack_power = 6
        self.level = 1
        self.roll = 19

class Rogue(Character):
    
    def __init__(self, level =1, roll = 19, armor_class = 10):
        super().__init__(armor_class)
        self.alignment = ("evil", "neutral")
      
class Paladin(Character):
    base_att_roll_on_level = 1
    
    def __init__(self, level =1, roll = 19, armor_class = 10):
        super().__init__(armor_class)
        self.hp = 10
        self.alignment = ("good")
        self.level = 1
       
