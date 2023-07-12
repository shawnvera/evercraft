from examplemodule1 import Character
 

# test feature create a character
# can get a name 
# can set a name 

#Feature: Create a Character

def test_get_name():
    char = Character()
    assert char.name == "Cletus"

def test_set_name():
    char2 = Character()
    char2.name = "Better Cletus"
    assert char2.name == "Better Cletus" 

# Feature: Alignment

def test_set_alignment():
    ali = Character()
    ali.alignment = "good"
    assert ali.alignment == "good"

def test_get_alignment():
    ali = Character()
    ali.alignment = "good"
    assert ali.alignment == "good"

# can you run both at the same time?
# seems to work at the same time
def test_set_get_alignment():
    ali = Character()
    ali.alignment = "good"
    assert ali.alignment == "good"

# Feature: Armor class and hit points

def test_armor_class():
    armor = Character()
 
    assert armor.armor_class == 10

def test_hp():
    hp = Character()
    
    assert hp.hp == 5

# Feature: player attack

def test_attack_power():
     ap = Character()
     goblin = Character()

     assert ap.roll >= goblin.armor_class
        
# Feature Character can be damaged

def test_attack_damage():
     ad = Character()
     goblin = Character()

     
     if (ad.roll >= goblin.armor_class):
        goblin.hp -= 1
     assert goblin.hp == 4