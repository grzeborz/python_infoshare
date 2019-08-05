import random

class Dice(object):
    """
    throw an dice and get the score
    """
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.choice(range(1, self.sides + 1))

class Character(object):
    """
    class contain characteristics and methods to use
    """
    def __init__(self, health = 10, strength = 5, damage = 2, armor = 5):
        """
        characeeristics of a character
        """
        self.strength = strength
        self.health = health
        self.damage = damage
        self.armor = armor
        self.character_state = "Alive"

    def __str__(self):
        return "I am a game character %s, my health value: %s" % (self.__class__.__name__, self.health)

    def attack(self, target_character, dice_def):
        if (dice_def > 3):
            print(f"Roll defence dice is: {dice_def}, You were able to parry attack")
            pass
        else:
            print(f"This is attack of character class {self.__class__.__name__}")
            target_character.defend(self.damage)

    def defend(self, damage):
        damage_to_health = max(damage - self.armor, 0)
        self.armor = max(self.armor - damage, 0)
        self.health = max(self.health - damage_to_health, 0)
        if (self.health == 0):
            print(f"Your health is equal: {self.health} YOU ARE DEAD. END OF GAME")
            self.character_state = "Dead"
            # raise RuntimeError("YOU ARE DEAD. You can't kill dead")
            # exit(0)

class Barbarian(Character):
    """

    """
    def __init__(self, health=10, strength=5 , damage =2, armor=5, anger=1):
        super().__init__()
        self.anger = anger

    def attack(self, target_character, dice_def):
        """
        modified attack for barbadian
        :param target_character:
        :param dice_def:
        :return:
        """
        print(f"This is attack of character class {self.__class__.__name__}")
        if (dice_def > 3):
            print(f"Roll defence dice is: {dice_def}, You were able to parry attack")
            pass
        else:
            target_character.defend(self.damage + self.anger)
            super().attack(target_character, dice_def)