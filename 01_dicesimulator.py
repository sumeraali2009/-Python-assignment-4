import random

def roll_dice():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    return roll1, roll2

for i in range(3):
    roll1, roll2 = roll_dice()
    print(f"Roll {i+1}: Die 1 = {roll1}, Die 2 = {roll2}")

