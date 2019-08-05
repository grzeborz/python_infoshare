from day10.game import Dice, Character, Barbarian

player = Character(20)
enemy = Character()
simple_dice = Dice()

print(f"Before enemy attack your player has armor: {player.armor} and health: {player.health}")
# simple_dice = Dice()
#
# print(f"Rolled with number: {simple_dice.roll()}")

roll_dice = int(simple_dice.roll())
first_move = enemy.attack(player, roll_dice)

print(f"After enemy attack your player has armor: {player.armor} and health: {player.health}")
print(player)

# for x in range(60):
#     roll_dice = int(simple_dice.roll())
#     if player.character_state == "Dead":
#         break
#     enemy.attack(player, roll_dice)

barbarian = Barbarian()

roll_dice = int(simple_dice.roll())

barbarian.attack(player, roll_dice)

print(f"After enemy attack your player has armor: {player.armor} and health: {player.health}")