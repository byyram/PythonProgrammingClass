import random

def roll_dice():
    num_one = random.randrange(1,7)
    num_two = random.randrange(1,7)

    sum = num_one + num_two

    return num_one, num_two, sum

def display_dice():
    print(roll_dice())

display_dice()
