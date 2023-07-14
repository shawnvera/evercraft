class Character:
        def __init__(self, level = 1, roll = 19, armor_class = 10):
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
                self.attack = False


        def set_name(self, name):
            self.name = name
            

# Feature: Alignment

        def set_alignment(self, alignment):
            
            self.alignment = alignment

# Feature: player attack

        def can_attack(self, armor_class, roll):
            if roll >= armor_class:
                self.attack = True
            else: 
                self.attack = False

        
# # Feature Character can be damaged

        def attack_damage(self, att):
  
            if (self.attack == True):
                self.hp -= 1
            

# # Feature: Character has abilities scores

   

# # Feature: Character ability modifiers modify attributes

        def update_attributes(self, roll, attributes):

            if (self.roll == 19):
                self.attributes["constitution"] = 10 + 4
            if self.attributes["constitution"] == 14:
                self.hp = self.hp + 4
            if (self.roll == 19):
                self.attributes["strength"] = 10 + 4
            if (self.roll == 19):
                self.attributes["wisdom"] = 10 + 4
            if (self.roll == 19):
                self.attributes["charisma"] = 10 + 4
            if (self.roll == 19):
                self.attributes["dexterity"] = 10 + 4
            if (self.roll == 19):
                self.attributes["intelligence"] = 10 + 4
            
   

# # Feature: A character can gain experience when attacking

        def gain_xp(self, attack, xp):            
            if attack == True:
                self.xp = self.xp + 10
   

   

# # Feature: A character can level

        def can_level(self, xp):
            
            if self.xp >= 1000:
                self.level = self.level + 1

  

# #Stat increases with test_can_level

        def on_level(self, level, hp, attack_power):
            if self.level == 2:
                self.hp = self.hp + 5
                self.attack_power = self.attack_power + 1



                