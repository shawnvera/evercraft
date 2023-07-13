#MVP#

Two (2) iterations of the project should be completed by Friday

#MoSCow#

    Must haves:
        1. Pseudocode should follow the examples and step through each individual task.
        2. Code must be commented well.
        3. Tests should be written first, then code written to pass the tests.
    
    Should haves:
        1. iteration 3

    Could haves:
        1. iteration 4

    Won't haves:
        1. coded dice roll



**Iteration 1**

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


**Iteration 2**

#agile stories#

    1. As a player I want a character to have a class that customizes its capabilities so that I can play more interesting characters

    2. As a player I want to play a Fighter so that I can kick ass and take names

    3. As a player I want to play a Rogue so that I can defeat my enemies with finesse

    4. As a player I want to play a Monk so that I can enjoy being an Asian martial-arts archetype in a Medieval European setting

    5. As a player I want to play a Paladin so that I can smite evil, write wrongs, and be a self-righteous jerk

#Questions#
    - what is the best way to set class specific stat changes?
        -use object that stores data and modifies character?
        -loop through stats based on character "class type" and adjust values by checking "class type"?


#Procedural#

    BEGIN
    INIT create new class for Classes
    TEST test new classes do make changes to base attributes
    END

#Functional#

    the new class will modify the character
    
    class Class:
        attributes to be changed

    


#OOP#

    class Class:
    def __init__(self):
        self.fighter = {
            Character[strength] + 3
        }
        self.rogue = 0
        self.monk = {
            Character[hp + 1],

        }
        self.paladin = 0