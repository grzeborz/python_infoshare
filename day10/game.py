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

    def attack(self, target_character):
        target_character.defend(self.damage)

    def defend(self, damage):
        damage_to_health = max(damage - self.armor, 0)
        self.armor = max(self.armor - damage, 0)
        self.health = self.health - damage_to_health





# simple_dice = Dice()
#
# print(f"Rolled with number: {simple_dice.roll()}")