import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")
    print(f"Total: {total}")

roll_dice()

