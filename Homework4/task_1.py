import random
players = int(input("Please enter players numbers: "))
for i in range(players):
    first_dice = random.randint(1,6)
    second_dice = random.randint(1,6)
    print(first_dice, second_dice)