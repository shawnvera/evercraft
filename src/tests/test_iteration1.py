from examplemodule1 import Character
 

# test feature create a character
# can get a name 
# can set a name 

#Feature: Create a Character

def test_get_name():
    char = Character()
    assert char.name == "Cletus"

def test_set_name():
    char = Character()
    char.set_name('Better Cletus')
    #char2.name = "Better Cletus"
    assert char.name == "Better Cletus" 

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

def test_can_attack():
     ap = Character()
     goblin = Character()
     ap.can_attack(10, 20)

     assert ap.attack == True
     
        
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
    mod.update_attributes(19, "constitution")

    assert mod.attributes["constitution"] == 14

# Feature: A character can gain experience when attacking

def test_gain_xp():
    xp = Character()
    xp.gain_xp(True, 10)
    
    assert xp.xp == 10

# Feature: A character can level

def test_can_level():
    level = Character()
    level.can_level(1000)

    # level.xp = 1000
    # if level.xp == 1000:
    #     level.level = level.level + 1

    assert level.level == 2

#Stat increases with test_can_level

def test_on_level():
    up = Character()
    up.level = 2
    up.on_level(2, 5, 5)
    
    # if up.level == 2:
    #     up.hp = up.hp + 5
    #     up.attack_power = up.attack_power + 1

    assert up.hp == 10
    assert up.attack_power == 6


