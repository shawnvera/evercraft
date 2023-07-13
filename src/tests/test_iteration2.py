from examplemodule1 import Character
from examplemodule2 import Monk
from examplemodule2 import Fighter
from examplemodule2 import Rogue
from examplemodule2 import Paladin

def test_class():
    monk = Monk()
    char = Character()

    
    assert monk.hp == 6

def test_attack_fighter_level():
    fight = Fighter()
    fight.level = 2
    if fight.level == 2:
        fight.roll + 1

    assert fight.roll == 20