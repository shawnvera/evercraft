class Character:
        def __init__(self):
                self.name = "Cletus"
                self.alignment = ("good", "evil", "neutral")
                self.armor_class = 10
                self.hp = 5
                self.attack_power = 5
                self.roll = 20
        
        def set_name(self, n):
            self.name = n

        def set_alignment(self, alignment):
            self.alignment = "good", "evil", "neutral"
        
        def armor_class(self, armor_class):
            self.armor_class = 10

        def hp(self, hp):
            self.hp = 5

