
from 
# test feature create a character
# can get a name 
# can set a name 

def test_get_name(name):
    char = Character()
    assert char.name == name

def test_set_name(name):
    char.name = name
    assert char.name == name 