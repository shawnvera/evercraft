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

# Feature: Character has abilities scores

def test_attributes():
    att = Character()
    assert att.attributes["wisdom"] == 10

# Feature: Character ability modifiers modify attributes

def test_update_attributes():
    mod = Character()

    if (mod.roll == 19):
        mod.attributes["constitution"] = 10 + 4
    if mod.attributes["constitution"] == 14:
        mod.hp = mod.hp + 4
    assert mod.hp == 9
    assert mod.attributes["constitution"] == 14

# Feature: A character can gain experience when attacking

def test_gain_xp():
    xp = Character()

    if xp.roll >= xp.armor_class:
        attack = True
        xp.xp = xp.xp + 10
    

    assert xp.xp == 10

# Feature: A character can level

def test_can_level():
    level = Character()

    level.xp = 1000
    if level.xp == 1000:
        level.level = level.level + 1

    assert level.level == 2