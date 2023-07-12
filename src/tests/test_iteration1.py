from examplemodule1 import Character
 

# test feature create a character
# can get a name 
# can set a name 

def test_get_name():
    char = Character()
    assert char.name == "Cletus"

def test_set_name():
    char2 = Character()
    char2.name = "Better Cletus"
    assert char2.name == "Better Cletus" 