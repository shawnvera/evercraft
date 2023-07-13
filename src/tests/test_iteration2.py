from examplemodule1 import Character
from examplemodule2 import Monk

def test_class():
    monk = Monk()
    char = Character()

    if monk.level == 2:
        hp_on_level()
    
    assert char.hp == 11

# def test_