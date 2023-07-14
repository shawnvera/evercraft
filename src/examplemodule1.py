class Character:
        def __init__(self, level = 1, roll = 19, armor = 10):
                self.name = "Cletus"
                self.alignment = ("good", "evil", "neutral")
                self.armor_class = 10
                self.hp = 5
                self.attack_power = 5
                self.roll = 19
                self.attributes = {
                    "strength": 10,
                    "dexterity": 10,
                    "constitution": 10,
                    "wisdom": 10,
                    "intelligence": 10,
                    "charisma": 10
                }
                self.xp = 0
                self.level = 1
                self.type = ['Monk', "Paladin", "Fighter", "Rogue"]

#         def get_name():
#             char = Character()
           

#         def set_name(name):
            
#             char2.name = "Better Cletus"
            

# # Feature: Alignment

# def test_set_alignment():
#     ali = Character()
#     ali.alignment = "good"
#     assert ali.alignment == "good"

# def test_get_alignment():
#     ali = Character()
#     ali.alignment = "good"
#     assert ali.alignment == "good"

# # can you run both at the same time?
# # seems to work at the same time
# def test_set_get_alignment():
#     ali = Character()
#     ali.alignment = "good"
#     assert ali.alignment == "good"

# # Feature: Armor class and hit points

# def test_armor_class():
#     armor = Character()
 
#     assert armor.armor_class == 10

# def test_hp():
#     hp = Character()
    
#     assert hp.hp == 5

# # Feature: player attack

# def test_attack_power():
#      ap = Character()
#      goblin = Character()

#      assert ap.roll >= goblin.armor_class
        
# # Feature Character can be damaged

# def test_attack_damage():
#      ad = Character()
#      goblin = Character()

     
#      if (ad.roll >= goblin.armor_class):
#         goblin.hp -= 1
#      assert goblin.hp == 4

# # Feature: Character has abilities scores

# def test_attributes():
#     att = Character()
   

# # Feature: Character ability modifiers modify attributes

# def test_update_attributes():
#     mod = Character()

#     if (mod.roll == 19):
#         mod.attributes["constitution"] = 10 + 4
#     if mod.attributes["constitution"] == 14:
#         mod.hp = mod.hp + 4
   

# # Feature: A character can gain experience when attacking

# def test_gain_xp():
#     xp = Character()

#     if xp.roll >= xp.armor_class:
#         attack = True
#         xp.xp = xp.xp + 10
    

   

# # Feature: A character can level

# def test_can_level():
#     level = Character()

#     level.xp = 1000
#     if level.xp == 1000:
#         level.level = level.level + 1

  

# #Stat increases with test_can_level

# def on_level():
#     up = Character()
#     up.level = 2
#     if up.level == 2:
#         up.hp = up.hp + 5
#         up.attack_power = up.attack_power + 1



                