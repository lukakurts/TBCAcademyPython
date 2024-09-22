import random
numbers = random.randrange(1,14)
color = random.choice(['clubs', 'diamonds', 'hearts', 'spades'])

if numbers == 1:
    print("A", color)
elif numbers == 11:
    print("J", color)
elif numbers == 12:
    print("Q", color)
elif numbers == 13:
    print("K", color)
else:
    print(numbers, color)