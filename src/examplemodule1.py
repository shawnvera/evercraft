class Character:
        def __init__(self):
                self.name = "Cletus"
                self.alignment = ("good", "evil", "neutral")
                self.armor_class = 10
                self.hp = 5
                self.attack_power = 5
                self.roll = 19
                self.attributes = {
                    "strength": 10,#mod(),
                    "dexterity": 10,
                    "constitution": 10,
                    "wisdom": 10,
                    "intelligence": 10,
                    "charisma": 10
                }
        
        # def get_name(self, n):
        #     self.name = "Cletus"


        # def set_name(self, n):
        #     self.name = n

        # def set_alignment(self, alignment):
        #     self.alignment = "good", "evil", "neutral"
        
        # def armor_class(self, armor_class):
        #     self.armor_class = 10

        # def hp(self, hp):
        #     self.hp = 5

        def mod():
            strength = 10
            for i in range(20):
                yield strength + 4

