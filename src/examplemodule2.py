from examplemodule1 import Character

class Monk(Character):
    base_att_roll_on_level = 1 

    def __init__(self, level=1, roll=19, armor_class=10):
        super().__init__(armor_class)
        self.hp = 6

    # Functions

    def mon_base_roll(self, level):
         
        if self.level == 2:
            self.base_att_roll_on_level = self.base_att_roll_on_level + 1

       
        if self.level == 3:
            self.base_att_roll_on_level = self.base_att_roll_on_level + 1


    def monk_hp(self, level, hp):
       
        if self.level == 2:
            self.hp = self.hp + 6
    
        if self.level == 3:
            self.hp = self.hp + 6

    
        
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
       

# Functions

# Feature: Characters have classes

# Monk




# Fighter

def test_attack_fighter_level():
    fight = Fighter()
    fight.level = 2
    
    if fight.level == 2:
        fight.roll = fight.roll + 1

    fight.level = 3
    if fight.level == 3:
        fight.roll = fight.roll + 1

    assert fight.roll == 21

def test_hp_fighter_level():
    f = Fighter()
    f.level = 2

    if f.level == 2:
        f.hp = f.hp + 10

    f.level = 3

    if f.level == 3:
        f.hp = f.hp + 10

        assert f.hp == 30

# Rogue

def test_rogue_alignment():
    rog = Rogue()

    assert rog.alignment != "good"

# Paladin

def test_paladin_hp():
    pal = Paladin()
    pal.level = 2

    if pal.level == 2:
        pal.hp = pal.hp + 8

    pal.level = 3
    if pal.level == 3:
        pal.hp = pal.hp + 8

    assert pal.hp == 26
    
def test_paladin_alignment():
    pal = Paladin()

    assert pal.alignment == "good"

def test_base_roll():
    pal = Paladin()

    pal.level = 2
    if pal.level == 2:
        pal.base_att_roll_on_level = pal.base_att_roll_on_level + 1

    pal.level = 3
    if pal.level == 3:
        pal.base_att_roll_on_level = pal.base_att_roll_on_level + 1

    assert pal.base_att_roll_on_level == 3