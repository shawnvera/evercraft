#Agile stories#

    ##Iteration 1##

    As a character I want to have a name so that I can be distinguished from other characters

    As a character I want to have an alignment so that I have something to guide my actions

    As a combatant I want to have an armor class and hit points so that I can resist attacks from my enemies

    As a combatant I want to be able to attack other combatants so that I can survive to fight another day

    As an attacker I want to be able to damage my enemies so that they will die and I will live

    As a character I want to have several abilities so that I am not identical to other characters except in name

    As a character I want to apply my ability modifiers improve my capabilities in combat so that I can vanquish my enemy with extreme prejudice

    As a character I want to accumulate experience points (xp) when I attack my enemies so that I can earn bragging rights at the tavern

    As a character I want my experience points to increase my level and combat capabilities so that I can bring vengeance to my foes

#Questions#

    -how to do standard ability values impact character interaction, if strength is 13 then do attack always hit on opponents with less than 13 armour?
    -what does each ability modify for each character?
    -how much exp do you gain once an enemy is defeated?

#Procedural#
    BEGIN
    INIT - declare variables
    END

#Functional#
    **Variables:**
        character, alignment, armor_class, hp, can_attack, can_be_damaged, ability_scores, ability_modifiers, can_gain_XP, can_level 



    **Functions:**
        set_character_name
        get_character_name
        set_character_alignment
        get_character_alignment
        attack(set_roll) hard coded
            output roll
        can_damage(roll):
            update enemy hp/armor
            if (roll) > enemy hp/armor
                subtract difference
            else
                "attack missed, S@#$T!"
        set_abilities
            all to default of 10 (Strength, Dexterity, Constitution, Widsom, Intelligence and Charisma)
        adjust_abilities()
            see modifier table: adjust abilities based on roll
                ie: strength_roll = 17, +3 to strength(current value is 10). new strength value is 13
        can_gain_exp
            if attack hits
                then gain 10 exp
            and if enemy is defeated, gain xp(what value?)
            else no exp
            
        
        
            




#OOP#

    **Classes:**

            class Character:
                def __init__(self, name):
                    self.name = 
                    "alignment": "good", "evil", "neutral"
                    "armor_class": 10
                    "hp": 5
                    "can_attack"
                    "can_be_damaged":
                    "ability_scores":
                    "ability_modifiers"
                    "can_gain_XP"
                    "can_level"
                    roll: 20
                    xp: 0
                    level: 1


                c = Character()

                c.name
                c.xp

                separate class that interacts with the Character class?