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
    armor.armor_class = 10
    assert armor.armor_class == 10

def test_hp():
    hp = Character()
    hp.hp = 5
    assert hp.hp == 5

