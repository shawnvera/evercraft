from examplemodule1 import Character
from examplemodule2 import Monk
from examplemodule2 import Fighter
from examplemodule2 import Rogue
from examplemodule2 import Paladin

# Feature: Characters have classes

# Monk

def test_mon_base_roll():
    mon = Monk()

    mon.level = 2
   
    if mon.level == 2:
        mon.base_att_roll_on_level = mon.base_att_roll_on_level + 1

    mon.level = 3
    if mon.level == 3:
        mon.base_att_roll_on_level = mon.base_att_roll_on_level + 1

    assert mon.base_att_roll_on_level == 3

def test_monk_hp():
    mon = Monk()

    mon.level = 2
    if mon.level == 2:
        mon.hp = mon.hp + 6
    
    mon.level = 3
    if mon.level == 3:
        mon.hp = mon.hp + 6
    
    assert mon.hp == 18


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